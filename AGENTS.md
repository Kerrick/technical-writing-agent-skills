# Working in this repo

Read [README.md](README.md) for what this is, [method/README.md](method/README.md) for how the method runs, and [CONTRIBUTING.md](CONTRIBUTING.md) before adding a run. This file is the rules an agent breaks without being told.

## Rules

- **Runs are records.** Never edit a run's `baseline/`, `pipeline/` or findings files. Fix only line citations in `PLACEMENT.md`.
- **Prompts are the method as it now stands.** Changing a prompt in `method/prompts/` changes the next run. Say why in the commit, and record any difference a past run had in that run's `README.md`, not in the prompt.
- **Keep runs comparable.** Don't change `method/sources.toml` sources, scopes or commits, or `evals/developer-docs/`, as part of a run.
- **Never install the baseline or a developer-docs skill while running the method**, this repo's included. Install only `method/vendor/agent-skills`.
- **`skills/developer-docs/` changes only when a run's evals beat it.** `skills/readme-rewrite/` isn't made by the method and changes the ordinary way.
- **Python only**, run with `uv run`, standard library first. No shell scripts. Each mise task runs exactly one script in `method/scripts/`.
- **No fixed paths or baseline line numbers in prompts.** Use the `${SLOTS}` in method/README.md, and describe a baseline rule by what it says.
- **Pin to public, exact versions:** full commit hashes reachable upstream, exact tool versions. Prefer the newest stable release.
- **Run `mise run check` before every commit**, and test a script by running it the way an agent would.

## Gotchas

- Any edit to a skill's `SKILL.md` above a cited line shifts every `PLACEMENT.md` citation after it. Run `mise run check` and fix the citations.
- zsh doesn't split an unquoted variable into words, so `cmd=$(…); $cmd` or `$dirs` passed as several arguments fails. Run such commands under `bash -c`.
- A new file that quotes a source needs its own entry in `REUSE.toml` and an opening notice naming the source, holder and license, like the existing findings files.
- `leak_check.py` matches whole words, so "trust" and "member" don't trip on "rust" and "ember". Add a source's own terms with `--names`.
