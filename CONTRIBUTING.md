# Contributing

The skill in this repo was made for one model at one effort level. Every other model needs its own run of the method, because the skill is only what that model doesn't already do. Runs cost a lot of tokens, which is where you come in.

## Most wanted

1. **Eval results for the existing run.** `runs/claude-opus-5.5-medium/` has never been evaluated, so nobody knows yet whether the method beats its own baseline. This is the single most useful contribution. See [Evaluating](README.md#evaluating).
2. **A run on another model.** Any model, any effort level, any provider. Wanted especially: Fable 5.2, Sonnet 5.5, Astra 6.2, Sol 6.2, Gemini 4 Neon.
3. **Real-task results.** You used the skill to document a real project; tell us what happened, recorded as [Evaluating](README.md#evaluating) describes for real tasks.

## Contributing a run

Follow [Repeating it](README.md#repeating-it) in the README. Expect a dozen or so long sessions; most of the cost is the reading forks, one per source, each of which reads up to about half its context window of documentation.

A pull request for a run adds one folder, `runs/<provider>-<model>-<version>-<effort>/`, containing:

- `README.md`, like [the first run's](runs/claude-opus-5.5-medium/README.md): model, effort, context window, harness and version, sub-agent model, the value of each slot, and anything you did differently from the method as written.
- `baseline/technical-writing/`, exactly as the model wrote it.
- `pipeline/`, with every intermediate file, and `pipeline/findings/` with one file per source.
- `skill/technical-writing/` and `PLACEMENT.md`.
- `workspace/`, if you ran the evals.

Before opening it, run:

```
mise run check
```

(Or `uv run method/scripts/check.py` without mise.) It runs the agent-skills validator and the leak check on every skill, the placement check on every run, and `reuse lint`.

For `reuse lint` to pass, add your findings files to `REUSE.toml` the way the first run's are, each with its source's copyright holder and license, and give each findings file the same opening notice.

## Rules that keep runs comparable

- **Same sources, scopes, commits and prompts.** Change only what the slots stand for. If something has to change (a source is gone, a scope won't fit your model's window), say what and why in your run's README.
- **Same evals.** Don't edit `evals/` as part of a run. Propose eval changes in their own pull request, since they affect every run.
- **No technical-writing skill installed while you run it**, including this repo's. Install only `method/vendor/agent-skills`.
- **Don't change the default.** `skills/technical-writing/` changes only when a run's evals beat the current default's, in a pull request of its own.

## Other changes

Fixes to the method, the scripts or the docs are welcome as ordinary pull requests. A change to a prompt changes what the next run does, so explain what went wrong with the old wording.

## License

By contributing, you dedicate your contribution to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt), like the rest of the repo. Quoted source material in findings files keeps its source's license, as [Licensing](README.md#licensing) describes.
