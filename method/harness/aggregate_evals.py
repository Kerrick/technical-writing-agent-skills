"""Copy runs and grades into the repo workspaces and write benchmark.json per suite."""
import json, shutil, statistics, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from orchestrate import SUITES, SCRATCH, REPO, collect_output  # noqa: E402


def stats(xs):
    xs = [x for x in xs if x is not None]
    if not xs:
        return {"mean": None, "stddev": None}
    return {"mean": round(statistics.mean(xs), 4), "stddev": round(statistics.pstdev(xs), 4) if len(xs) > 1 else 0.0}


def main():
    report = {}
    for suite, cfg in SUITES.items():
        ws = cfg["workspace"]
        ws.mkdir(parents=True, exist_ok=True)
        evs = json.loads(cfg["evals"].read_text())["evals"]
        per_eval, per_setup = {}, {s: {"pass": [], "time": [], "tokens": [], "out": [], "cost": [], "passed": 0, "total": 0} for s in cfg["setups"]}
        per_assertion = {}
        for ev in evs:
            name = f"eval-{ev['id']}-{cfg['names'][ev['id']]}"
            ed = ws / name
            gd = SCRATCH / "grading" / suite / name
            mapping = json.loads((SCRATCH / "mappings" / f"{suite}-{name}.json").read_text())
            inv = {v: k for k, v in mapping["mapping"].items()}
            per_eval[name] = {}
            for setup in cfg["setups"]:
                sd = ed / setup
                if sd.exists():
                    shutil.rmtree(sd)
                collect_output(suite, name, setup, sd / "outputs_tmp")
                (sd / "outputs").mkdir(parents=True)
                tmp = sd / "outputs_tmp"
                for item in tmp.iterdir():
                    shutil.move(str(item), sd / "outputs" / item.name)
                tmp.rmdir()
                base = SCRATCH / "runs" / suite / name
                shutil.copy2(base / f"{setup}.timing.json", sd / "timing.json")
                shutil.copy2(base / f"{setup}.prompt.txt", sd / "prompt.txt")
                g = json.loads((gd / "grades" / f"{inv[setup]}.json").read_text())
                n = len(g["assertion_results"])
                p = sum(1 for a in g["assertion_results"] if a["passed"])
                g["summary"] = {"passed": p, "failed": n - p, "total": n, "pass_rate": round(p / n, 4)}
                g["blind_label"] = inv[setup]
                (sd / "grading.json").write_text(json.dumps(g, indent=2))
                t = json.loads((sd / "timing.json").read_text())
                per_eval[name][setup] = {"passed": p, "total": n, "pass_rate": round(p / n, 4),
                                         "tokens": t["total_tokens"], "output_tokens": t["output_tokens"],
                                         "time_seconds": round(t["duration_ms"] / 1000, 1),
                                         "cost_usd": t.get("total_cost_usd")}
                ps = per_setup[setup]
                ps["pass"].append(p / n); ps["time"].append(t["duration_ms"] / 1000)
                ps["tokens"].append(t["total_tokens"]); ps["out"].append(t["output_tokens"])
                ps["passed"] += p; ps["total"] += n
                ps["cost"].append(t.get("total_cost_usd"))
                for i, a in enumerate(g["assertion_results"]):
                    per_assertion.setdefault(f"{name}#{i+1}", {"text": ev["assertions"][i]})[setup] = a["passed"]
            comp = json.loads((gd / "grades" / "comparison.json").read_text())
            comp["label_mapping"] = mapping["mapping"]
            comp["ranking_by_setup"] = [mapping["mapping"].get(l, l) for l in comp.get("ranking", [])]
            (ed / "comparison.json").write_text(json.dumps(comp, indent=2))
            (ed / "blind_mapping.json").write_text(json.dumps(mapping, indent=2))
            shutil.copy2(gd / "grader.timing.json", ed / "grader_timing.json")
        summary = {}
        for s, ps in per_setup.items():
            summary[s] = {"pass_rate": stats(ps["pass"]), "assertions_passed": ps["passed"], "assertions_total": ps["total"],
                          "pooled_pass_rate": round(ps["passed"] / ps["total"], 4),
                          "time_seconds": stats(ps["time"]), "tokens": stats(ps["tokens"]), "output_tokens": stats(ps["out"]), "cost_usd": stats(ps["cost"]),
                          "cost_usd_total": round(sum(c for c in ps["cost"] if c is not None), 4)}
        delta = {}
        pairs = [("sonnet_skill", "without_skill"), ("default_skill", "without_skill"), ("sonnet_skill", "default_skill"),
                 ("sonnet_skill", "sonnet_baseline"), ("sonnet_baseline", "without_skill")]
        for a, b in pairs:
            delta[f"{a}_minus_{b}"] = {k: round(summary[a][k]["mean"] - summary[b][k]["mean"], 4)
                                       for k in ("pass_rate", "time_seconds", "tokens", "cost_usd")}
        differing = {k: v for k, v in per_assertion.items() if len({v[s] for s in cfg["setups"]}) > 1}
        always_pass = [k for k, v in per_assertion.items() if all(v[s] for s in cfg["setups"])]
        always_fail = [k for k, v in per_assertion.items() if not any(v[s] for s in cfg["setups"])]
        bench = {"skill_name": suite, "iteration": 1, "model": "claude-sonnet-5-5", "effort": "medium", "grader_model": "claude-opus-5-5 (medium effort)",
                 "setups": {k: (str(v.relative_to(REPO)) if v else None) for k, v in cfg["setups"].items()},
                 "runs_per_setup_per_eval": 1,
                 "note": "Iteration 1: one run per setup per eval, so stddev is across evals, not repeated runs. Tokens are input + output + cache read + cache creation, summed over every model the session used. Every run is a fresh single-call session, so its cost is its result's total_cost_usd. Graders saw the four outputs under shuffled labels W-Z; blind_mapping.json gives the mapping.",
                 "run_summary": summary, "delta": delta, "per_eval": per_eval,
                 "assertions_differing": differing, "assertions_always_pass": always_pass, "assertions_always_fail": always_fail}
        (ws / "benchmark.json").write_text(json.dumps(bench, indent=2))
        report[suite] = bench
    print(json.dumps({s: {"summary": {k: (v["pooled_pass_rate"], v["pass_rate"]["mean"], v["tokens"]["mean"], v["time_seconds"]["mean"]) for k, v in b["run_summary"].items()},
                          "per_eval": b["per_eval"], "always_pass": b["assertions_always_pass"], "always_fail": b["assertions_always_fail"],
                          "differing": b["assertions_differing"]} for s, b in report.items()}, indent=1))


if __name__ == "__main__":
    main()
