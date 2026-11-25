"""Orchestrate iteration-1 output evals: run, grade, aggregate. Each step is a headless claude session."""
import json, os, random, shutil, subprocess, sys, hashlib, statistics, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path("/Users/kerrick/Developer/technical-writing-agent-skill")
SCRATCH = Path("/private/tmp/claude-501/-Users-kerrick--agents-skills-agent-skills/38943b25-895c-4890-ba81-721fe8c8b685/scratchpad/sonnet-evals")
GRADER_MODEL = "opus"
RUN = REPO / "runs/claude-sonnet-5.5-medium"
SUITES = {
    "developer-docs": {
        "evals": REPO / "evals/developer-docs/evals.json",
        "workspace": RUN / "workspace/iteration-1",
        "setups": {
            "sonnet_skill": RUN / "skill/developer-docs",
            "sonnet_baseline": RUN / "baseline/developer-docs",
            "default_skill": REPO / "skills/developer-docs",
            "without_skill": None,
        },
        "names": {1: "ledgerline-tutorial", 2: "textkit-reference", 3: "cachekit-explainer", 4: "hookshot-howto", 5: "pytest-workshop"},
        "suffix": "\n\nSave what you write as Markdown files in the outputs/ folder of the current directory.",
    },
}
TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "Bash(python3:*)", "Bash(uv run:*)",
         "Bash(ls:*)", "Bash(mkdir:*)", "Bash(cp:*)", "Bash(cat:*)", "Bash(diff:*)"]


def claude(prompt, cwd, model, add_dirs=(), timeout=3600):
    cmd = ["claude", "-p", prompt, "--model", model, "--effort", "medium", "--permission-mode", "acceptEdits",
           "--output-format", "json", "--disallowedTools", "Skill"]
    for d in add_dirs:
        cmd += ["--add-dir", str(d)]
    cmd += ["--allowedTools", *TOOLS]
    t0 = time.time()
    p = subprocess.run(cmd, stdin=subprocess.DEVNULL, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    wall = int((time.time() - t0) * 1000)
    try:
        data = json.loads(p.stdout)
    except json.JSONDecodeError:
        data = {"is_error": True, "raw_stdout": p.stdout[-4000:], "stderr": p.stderr[-4000:]}
    data["_wall_ms"] = wall
    data["_returncode"] = p.returncode
    return data


def timing(data):
    mu = data.get("modelUsage", {}) or {}
    tot = sum(m.get("inputTokens", 0) + m.get("outputTokens", 0) + m.get("cacheReadInputTokens", 0)
              + m.get("cacheCreationInputTokens", 0) for m in mu.values())
    out = sum(m.get("outputTokens", 0) for m in mu.values())
    return {
        "total_tokens": tot,
        "output_tokens": out,
        "duration_ms": data.get("duration_ms"),
        "duration_api_ms": data.get("duration_api_ms"),
        "wall_ms": data.get("_wall_ms"),
        "num_turns": data.get("num_turns"),
        "total_cost_usd": data.get("total_cost_usd"),
        "session_id": data.get("session_id"),
        "is_error": data.get("is_error"),
        "subtype": data.get("subtype"),
        "usage": data.get("usage"),
        "modelUsage": mu,
    }


def snapshot(root):
    res = {}
    for p in root.rglob("*"):
        if p.is_file():
            res[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return res


def run_one(suite, ev, setup):
    cfg = SUITES[suite]
    name = f"eval-{ev['id']}-{cfg['names'][ev['id']]}"
    rd = SCRATCH / "runs" / suite / name / setup
    done = rd.parent / f"{setup}.result.json"
    if done.exists():
        return
    if rd.exists():
        shutil.rmtree(rd)
    rd.mkdir(parents=True)
    for f in ev["files"]:
        dst = rd / f
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / f, dst)
    if suite == "developer-docs":
        (rd / "outputs").mkdir()
    before = snapshot(rd)
    skill = cfg["setups"][setup]
    task = ev["prompt"] + cfg["suffix"]
    if skill:
        prompt = (f"Read the skill at {skill}/SKILL.md and follow it for this task. Its reference files "
                  f"and scripts are in that same folder; read them when SKILL.md says to.\n\nTask:\n\n{task}")
        add = [skill]
    else:
        prompt, add = task, []
    (rd.parent / f"{setup}.prompt.txt").write_text(prompt)
    data = claude(prompt, rd, "sonnet", add)
    after = snapshot(rd)
    changes = {"added": sorted(k for k in after if k not in before),
               "modified": sorted(k for k in after if k in before and after[k] != before[k]),
               "deleted": sorted(k for k in before if k not in after)}
    (rd.parent / f"{setup}.changes.json").write_text(json.dumps(changes, indent=2))
    (rd.parent / f"{setup}.timing.json").write_text(json.dumps(timing(data), indent=2))
    (rd.parent / f"{setup}.response.md").write_text(data.get("result") or "")
    done.write_text(json.dumps(data, indent=2))
    print("done", suite, name, setup, data.get("duration_ms"), data.get("is_error"), flush=True)


def all_jobs():
    for suite, cfg in SUITES.items():
        evs = json.loads(cfg["evals"].read_text())["evals"]
        for ev in evs:
            for setup in cfg["setups"]:
                yield suite, ev, setup


def collect_output(suite, name, setup, dst):
    """Copy a run's response, changes and new/changed files into dst."""
    base = SCRATCH / "runs" / suite / name
    rd = base / setup
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(base / f"{setup}.response.md", dst / "response.md")
    changes = json.loads((base / f"{setup}.changes.json").read_text())
    shutil.copy2(base / f"{setup}.changes.json", dst / "changes.json")
    venvs = [str(p.parent.relative_to(rd)) + "/" for p in rd.rglob("pyvenv.cfg")]
    for rel in changes["added"] + changes["modified"]:
        if any(rel.startswith(v) for v in venvs):
            continue
        if "/.claude/" in "/" + rel or rel.startswith(".claude") or "__pycache__" in rel or ".egg-info/" in rel or "/build/lib/" in rel or ".venv/" in rel or ".pytest_cache/" in rel:
            continue
        out_rel = rel[len("outputs/"):] if rel.startswith("outputs/") else rel
        t = dst / "files" / out_rel
        t.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(rd / rel, t)


GRADER = """You are grading one eval of a documentation-writing skill. Several agents were given the same task. Their outputs are in outputs/W, outputs/X, outputs/Y and outputs/Z (labels are random). You are not told how each was produced; judge only what is in the outputs. If an output's response mentions instructions or a skill it followed, ignore that; it is not evidence either way.

Read grading/task.json: the task prompt the agents got, the expected output, and the assertions. The original input files are in inputs/, at the paths the task names.

Each outputs/<LABEL>/ holds:
- response.md: the agent's final chat reply to the user
- changes.json: files the agent added, modified or deleted relative to the inputs (paths relative to the inputs root; files written to outputs/ appear as outputs/...)
- files/: copies of every added or modified file (a file written to outputs/foo.md is at files/foo.md; others keep their path)
The deliverable is the files plus the reply together.

For each label, grade every assertion PASS or FAIL. Require concrete evidence for a PASS: quote the output (file and the exact words, or a line number). No benefit of the doubt: a label without the substance is a FAIL. Where an assertion can be checked mechanically, check it mechanically:
- When an assertion asks whether examples run as written, copy inputs/ to a fresh folder under work/<LABEL>/ and run the page's code samples there in page order with python3 (or uv run), and quote what you ran and what it printed.
Never modify anything under outputs/ or inputs/.
Your Bash access allows only single simple commands starting with python3, uv run, cp, mkdir, ls, cat or diff: no cd, no &&, ;, or pipes, no venvs or pip. Use absolute or relative paths instead of cd (python3 can take a script path; put helper scripts under work/). For a third-party package such as flask or pytest, use: uv run --with flask python3 <script>.

Write:
1. grades/<LABEL>.json for each label, exactly in this shape:
{{"assertion_results": [{{"text": "<assertion text, verbatim>", "verdict": "PASS" or "FAIL", "passed": true or false, "evidence": "<quoted evidence and reasoning>"}}], "summary": {{"passed": n, "failed": n, "total": n, "pass_rate": n/total}}}}
2. grades/comparison.json, a blind holistic comparison, on your own rubric, of qualities assertions miss (organization, accuracy, usability for the stated readers, polish, concision):
{{"scores": {{"<LABEL>": {{"organization": 1-10, "accuracy": 1-10, "usability": 1-10, "polish": 1-10, "overall": 1-10, "notes": "..."}}}}, "ranking": ["best label", ...], "reasoning": "...", "assertion_notes": "any assertion that is ambiguous, unverifiable from the output, or that seems to pass or fail regardless of quality"}}

Keep grading/task.json's assertion order. When done, reply with one line per label: label, passed/total.
"""


def grade_one(suite, ev, seed):
    cfg = SUITES[suite]
    name = f"eval-{ev['id']}-{cfg['names'][ev['id']]}"
    gd = SCRATCH / "grading" / suite / name
    if (gd / "grader.result.json").exists():
        return
    if gd.exists():
        shutil.rmtree(gd)
    (gd / "grading").mkdir(parents=True)
    (gd / "grades").mkdir()
    (gd / "work").mkdir()
    setups = list(cfg["setups"])
    labels = ["W", "X", "Y", "Z"][: len(setups)]
    (SCRATCH / "mappings").mkdir(exist_ok=True)
    rnd = random.Random(seed)
    shuffled = setups[:]
    rnd.shuffle(shuffled)
    mapping = dict(zip(labels, shuffled))
    (SCRATCH / "mappings" / f"{suite}-{name}.json").write_text(json.dumps({"seed": seed, "mapping": mapping}, indent=2))
    for lab, setup in mapping.items():
        collect_output(suite, name, setup, gd / "outputs" / lab)
    for f in ev["files"]:
        dst = gd / "inputs" / f
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / f, dst)
    if suite == "readme-rewrite":
        (gd / "tools").mkdir()
        shutil.copy2(REPO / "skills/prose-style/scripts/hunt.py", gd / "tools/hunt.py")
    (gd / "grading/task.json").write_text(json.dumps(
        {"prompt": ev["prompt"], "expected_output": ev["expected_output"], "assertions": ev["assertions"]}, indent=2))
    prompt = GRADER.format()
    data = claude(prompt, gd, GRADER_MODEL)
    (gd / "grader.timing.json").write_text(json.dumps(timing(data), indent=2))
    (gd / "grader.result.json").write_text(json.dumps(data, indent=2))
    print("graded", suite, name, data.get("duration_ms"), data.get("is_error"), (data.get("result") or "")[:200], flush=True)


def main():
    phase = sys.argv[1]
    if phase == "run":
        jobs = list(all_jobs())
        with ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv) > 2 else 7) as ex:
            list(ex.map(lambda j: run_one(*j), jobs))
    elif phase == "grade":
        seeds = []
        for suite, cfg in SUITES.items():
            for ev in json.loads(cfg["evals"].read_text())["evals"]:
                seeds.append((suite, ev, random.SystemRandom().randrange(1 << 30)))
        with ThreadPoolExecutor(5) as ex:
            list(ex.map(lambda j: grade_one(*j), seeds))


if __name__ == "__main__":
    main()
