# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Run, grade, and aggregate one iteration of a skill's output evals with headless Claude Code.

Written for the adr skill's iteration 1, from run_evals.py, with the paths made arguments.

  run        one fresh session per eval and setup, each in its own copy of the eval's files
  grade      one fresh, blind grader per eval, over every setup's output
  aggregate  copy outputs and grades into the workspace and write benchmark.json

Each setup is NAME=PATH to a skill folder, or NAME= for no skill. Every session runs with the
Skill tool disabled, and gets its skill by path in the prompt.

Exit codes:
  0  done
  2  bad arguments
"""

import argparse
import hashlib
import json
import random
import shutil
import statistics
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "WebSearch", "WebFetch",
         "Bash(python3:*)", "Bash(uv run:*)", "Bash(ls:*)", "Bash(mkdir:*)", "Bash(cp:*)", "Bash(mv:*)",
         "Bash(rm:*)", "Bash(cat:*)", "Bash(diff:*)", "Bash(grep:*)", "Bash(wc:*)", "Bash(date:*)",
         "Bash(git log:*)", "Bash(git status:*)", "Bash(git mv:*)", "Bash(git rm:*)"]
LABELS = "WXYZ"

GRADER = """You are grading one eval of a skill for writing Architecture Decision Records. Several agents were given the same task. Their outputs are in {labels} (labels are random). You are not told how each was produced; judge only what is in the outputs. If an output's reply mentions instructions or a skill it followed, ignore that; it is not evidence either way.

Read grading/task.json: the task prompt the agents got, the expected output, and the assertions. The original input files are in inputs/, at the paths the task names.

Each outputs/<LABEL>/ holds:
- response.md: the agent's final chat reply to the user
- changes.json: files the agent added, modified or deleted relative to the inputs (paths relative to the inputs root)
- files/: copies of every added or modified file, at its path
The deliverable is the files plus the reply together. A file listed as deleted in changes.json is gone.

For each label, grade every assertion PASS or FAIL. Require concrete evidence for a PASS: quote the output (file and the exact words, or a line number). No benefit of the doubt: a label without the substance is a FAIL. Each assertion opens with a bracketed tag naming the rule it tests; grade the statement after the tag. Where an assertion can be checked mechanically (a file exists or is deleted, a line count, a string is absent), check it mechanically and quote what you ran.
Never modify anything under outputs/ or inputs/. Your Bash access allows only single simple commands starting with python3, ls, cat, diff, grep or wc: no cd, no &&, ;, or pipes. Put helper scripts under work/.

Write:
1. grades/<LABEL>.json for each label, exactly in this shape:
{{"assertion_results": [{{"text": "<assertion text, verbatim>", "verdict": "PASS" or "FAIL", "passed": true or false, "evidence": "<quoted evidence and reasoning>"}}], "summary": {{"passed": n, "failed": n, "total": n, "pass_rate": n/total}}}}
2. grades/comparison.json, a blind holistic comparison, on your own rubric, of qualities the assertions miss (accuracy to the inputs, restraint, usefulness to a later reader, concision):
{{"scores": {{"<LABEL>": {{"accuracy": 1-10, "restraint": 1-10, "usefulness": 1-10, "concision": 1-10, "overall": 1-10, "notes": "..."}}}}, "ranking": ["best label", ...], "reasoning": "...", "assertion_notes": "any assertion that is ambiguous, unverifiable from the output, or that passes or fails regardless of quality"}}

Keep grading/task.json's assertion order. When done, reply with one line per label: label, passed/total.
"""


def claude(prompt, cwd, model, effort, add_dirs=(), tools=TOOLS, timeout=3600):
    cmd = ["claude", "-p", prompt, "--model", model, "--effort", effort, "--permission-mode", "acceptEdits",
           "--output-format", "json", "--disallowedTools", "Skill"]
    for d in add_dirs:
        cmd += ["--add-dir", str(d)]
    cmd += ["--allowedTools", *tools]
    started = time.time()
    p = subprocess.run(cmd, stdin=subprocess.DEVNULL, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    try:
        data = json.loads(p.stdout)
    except json.JSONDecodeError:
        data = {"is_error": True, "raw_stdout": p.stdout[-4000:], "stderr": p.stderr[-4000:]}
    data["_wall_ms"] = int((time.time() - started) * 1000)
    return data


def timing(data):
    usage = data.get("modelUsage", {}) or {}
    total = sum(m.get("inputTokens", 0) + m.get("outputTokens", 0) + m.get("cacheReadInputTokens", 0)
                + m.get("cacheCreationInputTokens", 0) for m in usage.values())
    return {"total_tokens": total, "output_tokens": sum(m.get("outputTokens", 0) for m in usage.values()),
            "duration_ms": data.get("duration_ms"), "wall_ms": data.get("_wall_ms"), "num_turns": data.get("num_turns"),
            "total_cost_usd": data.get("total_cost_usd"), "session_id": data.get("session_id"),
            "is_error": data.get("is_error"), "modelUsage": usage}


def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


def eval_name(ev, names):
    return f"eval-{ev['id']}-{names[ev['id']]}"


def run_one(args, ev, setup, skill):
    base = args.scratch / "runs" / eval_name(ev, args.names)
    rd, done = base / setup, base / f"{setup}.result.json"
    if done.exists():
        return
    if rd.exists():
        shutil.rmtree(rd)
    for f in ev["files"]:
        (rd / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / f, rd / f)
    before = snapshot(rd)
    if skill:
        prompt = (f"Read the skill at {skill}/SKILL.md and follow it for this task. Its reference files "
                  f"are in that same folder; read them when SKILL.md says to.\n\nTask:\n\n{ev['prompt']}")
    else:
        prompt = ev["prompt"]
    (base / f"{setup}.prompt.txt").write_text(prompt)
    data = claude(prompt, rd, args.model, args.effort, [skill] if skill else [])
    after = snapshot(rd)
    changes = {"added": sorted(k for k in after if k not in before),
               "modified": sorted(k for k in after if k in before and after[k] != before[k]),
               "deleted": sorted(k for k in before if k not in after)}
    (base / f"{setup}.changes.json").write_text(json.dumps(changes, indent=2))
    (base / f"{setup}.timing.json").write_text(json.dumps(timing(data), indent=2))
    (base / f"{setup}.response.md").write_text(data.get("result") or "")
    done.write_text(json.dumps(data, indent=2))
    print("ran", eval_name(ev, args.names), setup, data.get("duration_ms"), "error" if data.get("is_error") else "ok", flush=True)


def collect(args, name, setup, dst):
    base = args.scratch / "runs" / name
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(base / f"{setup}.response.md", dst / "response.md")
    shutil.copy2(base / f"{setup}.changes.json", dst / "changes.json")
    changes = json.loads((base / f"{setup}.changes.json").read_text())
    for rel in changes["added"] + changes["modified"]:
        if any(part in rel for part in (".claude", "__pycache__", ".pytest_cache", ".venv")):
            continue
        (dst / "files" / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(base / setup / rel, dst / "files" / rel)


def grade_one(args, ev):
    name = eval_name(ev, args.names)
    gd = args.scratch / "grading" / name
    if (gd / "grader.result.json").exists():
        return
    if gd.exists():
        shutil.rmtree(gd)
    for sub in ("grading", "grades", "work"):
        (gd / sub).mkdir(parents=True)
    setups = list(args.setups)
    random.SystemRandom().shuffle(setups)
    mapping = dict(zip(LABELS, setups))
    (gd / "mapping.json").write_text(json.dumps(mapping, indent=2))
    for label, setup in mapping.items():
        collect(args, name, setup, gd / "outputs" / label)
    for f in ev["files"]:
        (gd / "inputs" / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / f, gd / "inputs" / f)
    (gd / "grading" / "task.json").write_text(json.dumps(
        {"prompt": ev["prompt"], "expected_output": ev["expected_output"], "assertions": ev["assertions"]}, indent=2))
    labels = ", ".join(f"outputs/{label}" for label in mapping)
    tools = ["Read", "Write", "Glob", "Grep", "Bash(python3:*)", "Bash(ls:*)", "Bash(cat:*)", "Bash(diff:*)",
             "Bash(grep:*)", "Bash(wc:*)"]
    data = claude(GRADER.format(labels=labels), gd, args.grader_model, args.effort, tools=tools)
    (gd / "grader.timing.json").write_text(json.dumps(timing(data), indent=2))
    (gd / "grader.result.json").write_text(json.dumps(data, indent=2))
    print("graded", name, (data.get("result") or "")[:200].replace("\n", " | "), flush=True)


def stats(values):
    values = [v for v in values if v is not None]
    if not values:
        return {"mean": None, "stddev": None}
    return {"mean": round(statistics.mean(values), 4), "stddev": round(statistics.pstdev(values), 4)}


def aggregate(args, evals, skill_name):
    ws = args.workspace
    ws.mkdir(parents=True, exist_ok=True)
    per_eval, per_rule = {}, {}
    totals = {s: {"rates": [], "secs": [], "tokens": [], "cost": [], "passed": 0, "total": 0, "firsts": 0} for s in args.setups}
    for ev in evals:
        name = eval_name(ev, args.names)
        gd, base = args.scratch / "grading" / name, args.scratch / "runs" / name
        mapping = json.loads((gd / "mapping.json").read_text())
        label_of = {setup: label for label, setup in mapping.items()}
        comparison = json.loads((gd / "grades" / "comparison.json").read_text())
        (ws / name).mkdir(exist_ok=True)
        (ws / name / "comparison.json").write_text(json.dumps(comparison, indent=2))
        (ws / name / "blind_mapping.json").write_text(json.dumps(mapping, indent=2))
        shutil.copy2(gd / "grader.timing.json", ws / name / "grader_timing.json")
        totals[mapping[comparison["ranking"][0]]]["firsts"] += 1
        per_eval[name] = {}
        for setup in args.setups:
            sd = ws / name / setup
            if sd.exists():
                shutil.rmtree(sd)
            collect(args, name, setup, sd / "outputs")
            shutil.copy2(base / f"{setup}.timing.json", sd / "timing.json")
            shutil.copy2(base / f"{setup}.prompt.txt", sd / "prompt.txt")
            grade = json.loads((gd / "grades" / f"{label_of[setup]}.json").read_text())
            results = grade["assertion_results"]
            passed = sum(1 for a in results if a["passed"])
            grade["summary"] = {"passed": passed, "failed": len(results) - passed, "total": len(results),
                                "pass_rate": round(passed / len(results), 4)}
            grade["blind_label"] = label_of[setup]
            (sd / "grading.json").write_text(json.dumps(grade, indent=2))
            t = json.loads((sd / "timing.json").read_text())
            per_eval[name][setup] = {**grade["summary"], "tokens": t["total_tokens"],
                                     "time_seconds": round((t["duration_ms"] or 0) / 1000, 1), "cost_usd": t["total_cost_usd"]}
            tot = totals[setup]
            tot["rates"].append(passed / len(results)); tot["secs"].append((t["duration_ms"] or 0) / 1000)
            tot["tokens"].append(t["total_tokens"]); tot["cost"].append(t["total_cost_usd"])
            tot["passed"] += passed; tot["total"] += len(results)
            for a in results:
                rule = a["text"].split("]")[0].lstrip("[")
                per_rule.setdefault(rule, {s: [0, 0] for s in args.setups})[setup][0] += a["passed"]
                per_rule[rule][setup][1] += 1
    benchmark = {
        "skill_name": skill_name, "iteration": args.iteration, "model": args.model, "effort": args.effort,
        "grader_model": args.grader_model, "runs_per_setup_per_eval": 1,
        "note": "One run per setup per eval, so stddev is across evals, not repeated runs. Tokens are input + output + cache read + cache creation.",
        "run_summary": {s: {"pass_rate": stats(t["rates"]), "assertions_passed": t["passed"], "assertions_total": t["total"],
                            "pooled_pass_rate": round(t["passed"] / t["total"], 4), "ranked_first": t["firsts"],
                            "time_seconds": stats(t["secs"]), "tokens": stats(t["tokens"]),
                            "cost_usd": round(sum(c or 0 for c in t["cost"]), 4)} for s, t in totals.items()},
        "per_eval": per_eval,
        "per_rule": {rule: {s: f"{p}/{n}" for s, (p, n) in by.items()} for rule, by in per_rule.items()},
    }
    (ws / "benchmark.json").write_text(json.dumps(benchmark, indent=2) + "\n")
    for s, t in benchmark["run_summary"].items():
        print(f"{s}: {t['assertions_passed']}/{t['assertions_total']}, ranked first {t['ranked_first']}, ${t['cost_usd']}")


def main() -> int:
    parser = argparse.ArgumentParser(prog="uv run method/harness/run_skill_evals.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("phase", choices=["run", "grade", "aggregate"])
    parser.add_argument("--evals", type=Path, required=True, help="path to evals.json, inside the repo")
    parser.add_argument("--setup", action="append", required=True, metavar="NAME=PATH", help="a skill folder, or NAME= for no skill")
    parser.add_argument("--name", action="append", default=[], metavar="ID=SLUG", help="a short name for an eval's folder")
    parser.add_argument("--scratch", type=Path, required=True, help="a folder outside the repo for runs and grading")
    parser.add_argument("--workspace", type=Path, help="where aggregate writes, such as evals/<skill>/workspace/iteration-1")
    parser.add_argument("--iteration", type=int, default=1)
    parser.add_argument("--model", default="claude-opus-5-5")
    parser.add_argument("--grader-model", default="claude-opus-5-5")
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--jobs", type=int, default=6)
    args = parser.parse_args()
    args.setups = {}
    for item in args.setup:
        name, _, path = item.partition("=")
        args.setups[name] = Path(path).resolve() if path else None
    if len(args.setups) > len(LABELS):
        parser.error(f"at most {len(LABELS)} setups")
    spec = json.loads(args.evals.read_text())
    args.names = {ev["id"]: str(ev["id"]) for ev in spec["evals"]}
    args.names.update({int(k): v for k, v in (item.split("=", 1) for item in args.name)})
    args.scratch = args.scratch.resolve()
    if args.phase == "run":
        jobs = [(ev, setup, skill) for ev in spec["evals"] for setup, skill in args.setups.items()]
        with ThreadPoolExecutor(args.jobs) as pool:
            list(pool.map(lambda job: run_one(args, *job), jobs))
    elif args.phase == "grade":
        with ThreadPoolExecutor(args.jobs) as pool:
            list(pool.map(lambda ev: grade_one(args, ev), spec["evals"]))
    else:
        if not args.workspace:
            parser.error("aggregate needs --workspace")
        aggregate(args, spec["evals"], spec["skill_name"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
