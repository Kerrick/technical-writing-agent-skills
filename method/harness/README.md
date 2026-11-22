# Harness

Scripts agents wrote to drive headless sessions during the first runs and evals, kept as they were used. They aren't polished tools: each but `run_skill_evals.py` has a path or two from the machine it ran on, and expects the layout described in `method/README.md`. Start from them rather than from nothing.

| Script | Used for |
| - | - |
| `run_evals.py` | Iteration 1 of the Sonnet 5.5 evals: starts one headless session per eval and setup, then one blind grader per eval |
| `run_skill_evals.py` | Iteration 1 of the adr evals: `run_evals.py` with its paths made arguments, and the aggregation built in. Run it with `--help`. |
| `aggregate_evals.py` | Turns the grades and timings into `benchmark.json` |
| `run_session.py` | The Sonnet 5.5 run: starts, continues and forks `claude -p` sessions, and logs each to `sessions.md` |
| `verify_reads.py` | The Sonnet 5.5 run: confirms from a session's transcript that it read every listed file to its last line |
