# Contributing

The default developer-docs skill was made for Claude Opus 5.5 at medium effort. On Claude Sonnet 5.5 it beat a skill the method made for Sonnet itself, 80% of assertions to 51%. So the first thing to learn about another model is whether the default helps it. Evals answer that, at a small fraction of a run's cost.

## Most wanted

1. **Evals of the default on another model.** Run `evals/developer-docs/` with the default skill and with no skill on any model, any effort level, any provider, as [Evaluating](method/README.md#evaluating) describes. That shows what that model's users should install. Wanted especially: Fable 5.2, Astra 6.2, Sol 6.2, Gemini 4 Neon.
2. **More iterations of the existing evals.** Iteration 1 ran once per setup; the method asks for three before trusting the differences.
3. **A run on a model at least as strong as Claude Opus 5.5.** Such a run could make a better default. A run on a smaller model made a variant that did worse than the default on that model, so check the default there first.
4. **Real-task results.** You used a skill to document a real project; tell us what happened, recorded as [Evaluating](method/README.md#evaluating) describes for real tasks.

## Contributing a run

Follow [Repeating it](method/README.md#repeating-it) in method/README.md. Expect a dozen or so long sessions; most of the cost is the reading forks, one per source, each of which reads up to about half its context window of documentation.

A pull request for a run adds one folder, `runs/<provider>-<model>-<version>-<effort>/`, containing:

- `README.md`, like [the first run's](runs/claude-opus-5.5-medium/README.md): model, effort, context window, harness and version, sub-agent model, the value of each slot, and anything you did differently from the method as written.
- `baseline/<name>/`, the baseline skill exactly as the model wrote and named it.
- `pipeline/`, with every intermediate file, and `pipeline/findings/` with one file per source.
- `skill/developer-docs/` and `PLACEMENT.md`. (The first run has no `skill/` folder only because its skill is the current default, in `skills/developer-docs/`.)
- `workspace/`, if you ran the evals.

Before opening it, run:

```
mise run check
```

(Or `uv run method/scripts/check.py` without mise.) It runs the agent-skills validator and the leak check on every skill, the placement check on every run, and `reuse lint`.

For `reuse lint` to pass, add your findings files to `REUSE.toml` the way the first run's are, each with its source's copyright holder and license, and give each findings file the same opening notice.

## Rules that keep runs comparable

- **Same sources, scopes, commits and prompts.** Change only what the slots stand for. If something has to change (a source is gone, a scope won't fit your model's window), say what and why in your run's README.
- **Same evals.** Don't edit `evals/developer-docs/` as part of a run. Propose eval changes in their own pull request, since they affect every run.
- **No developer-docs skill or baseline installed while you run it**, including this repo's. Install only `method/vendor/agent-skills`.
- **Don't change the default.** `skills/developer-docs/` changes only when a run's evals beat the current default's, in a pull request of its own.

## Other changes

Fixes to the method, the scripts, the docs or readme-rewrite are welcome as ordinary pull requests. readme-rewrite isn't made by the method, so it changes the ordinary way. A change to a prompt changes what the next run does, so explain what went wrong with the old wording.

## License

By contributing, you dedicate your contribution to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt), like the rest of the repo. Quoted source material in findings files keeps its source's license, as [Licensing](README.md#license) describes.
