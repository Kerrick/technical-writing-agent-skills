# How the skill is made

The developer-docs skill holds only what one model, at one effort level, doesn't already do about documentation. This file explains how such a skill is made, how to make one for another model, and what the first run taught. To install and use the skills, see the [README](../README.md).

## Status

| | Claude Opus 5.5, medium |
| - | - |
| Steps 1–9: baseline, reading, audit, merge, check, writing | Done. The skill passes the agent-skills validator, the leak check and the placement check. |
| Output evals: new skill against baseline and no skill | Iteration 1, one run per setup: skill 87%, baseline 56%, no skill 46% of 71 assertions. Graders ranked the skill first in all five evals. In `workspace/iteration-1/`. |
| Trigger evals (`evals/developer-docs/eval_queries.json`) | Not yet run |
| Real tasks | Planned |

readme-rewrite isn't made by the method, so it has no run. Its iteration-1 evals, in `evals/readme-rewrite/workspace/iteration-1/`, passed 19 of 19 assertions, against 14 with no skill.

## Layout

| Path | What it is |
| - | - |
| `skills/developer-docs/` | The default developer-docs skill |
| `skills/readme-rewrite/` | The companion README skill. Not made by the method. |
| `skills/skill-authoring/` | The companion skill for writing skills. Not made by the method. |
| `runs/<run>/` | One run of the method for one model and effort level: its baseline, every intermediate file, and (unless it's the default) its own skill. `runs/claude-opus-5.5-medium/` is the first. |
| `evals/developer-docs/` | The evals every run is tested against: `evals.json`, `eval_queries.json` and their input files |
| `evals/readme-rewrite/` | readme-rewrite's evals |
| `evals/skill-authoring/` | skill-authoring's evals |
| `method/prompts/` | Every prompt as the method now stands, with `${SLOTS}`. Each run's README records where that run differed. |
| `method/sources.toml` | The seven sources (eight reading forks, since Rails is split in two): repositories, commits, paths, and every per-source prompt value |
| `method/sources.md` | Why each source and scope was chosen |
| `method/scripts/` | Fetching sources, filling prompts, extracting files and every check, in Python |
| `method/harness/` | Scripts agents wrote to drive headless runs and evals, kept as used |
| `mise.toml` | Tool versions and tasks: `mise run check`, `mise run fetch`, `mise run prompt` |
| `method/vendor/agent-skills/` | A pinned copy of the agent-skills skill, which steps 2 and 9 load |

## What it needs

Any agent harness that can do four things:

1. **Fork:** copy a session at a point, so many sessions start from the same state. (Claude Code: `/fork`.)
2. **Rewind:** return a session to an earlier message, dropping what came after. (Claude Code: press Esc twice, or `/rewind`.)
3. **Show context use:** how full a session's context is. (Claude Code: `/context`.)
4. **Run a cheaper sub-agent** for mechanical work like listing files. (Claude Code: a Sonnet sub-agent.)

Plus git, and either [mise](https://mise.jdx.dev/) or [uv](https://docs.astral.sh/uv/). `mise install` installs the pinned Python and uv. Every script in `method/scripts/` runs with `uv run`, which supplies Python on any platform, and every mise task is one of those scripts.

## Slots

The prompts use these, so they work on any machine:

| Slot | Meaning |
| - | - |
| `${SRC}` | The folder holding the source checkouts, cloned by `mise run fetch` |
| `${WORK}` | An empty working folder for this run, outside any skills folder |
| `${RUN}` | This run's folder: `runs/<provider>-<model>-<version>-<effort>/` in this repo |
| `${AGENT_SKILLS}` | `method/vendor/agent-skills/`, installed as a skill |
| `${LISTER}` | The cheaper sub-agent model that lists files to read (default: Sonnet) |

Don't fill them in by hand. `mise run prompt -- <step> [--source <key>] --src … --work … --run …` prints any step's prompt with every slot and per-source value filled in, and refuses if one is missing; `mise run prompt -- --help` lists the steps. `runs/claude-opus-5.5-medium/README.md` gives the values from the first run.

## Steps

Each step runs in one of three kinds of context, and what a context may see is the point of the design:

- **A fork of the baseline point:** the session that just wrote the baseline, forked before anything else is sent. It knows the baseline as its own beliefs.
- **A fresh session:** knows only what its prompt gives it.
- **A script:** no judgment at all.

| # | Step | Context | Reads | Writes |
| - | - | - | - | - |
| 1 | [Recall](prompts/01-recall.md) | New session | Nothing | Nothing |
| 2 | [Baseline](prompts/02-baseline.md) | Same session | The agent-skills skill | The baseline skill. **The fork point.** |
| 3 | [Reading order](prompts/03-reading-order.md) | One fork per source | A sub-agent's file list, then the pages | Nothing |
| 4 | [Compare](prompts/04-compare.md) | Same fork | The source's style guide | `${WORK}/<source>.md` |
| 5 | [Audit](prompts/05-audit.md) | New fork | All findings files, with quotes | `abstracted-full.md`: anonymized, no quotes |
| 6 | [Merge](prompts/06-merge.md) | New fork | `abstracted-full.md` only | `merged.md` |
| 7 | [Check "often broken"](prompts/07-check-often-broken.md) | New fork | `merged.md`, the findings, the source checkouts | `often-broken-check.md` |
| 8 | [Apply the check](prompts/08-apply-check.md) | Script, then the merge fork | `for-the-writer.md` only | Updated `merged.md`; then `kept.md` by script |
| 9 | [Write](prompts/09-write.md) | **Fresh session** | The agent-skills skill and `kept.md` only | `${RUN}/skill/developer-docs/` and `${RUN}/PLACEMENT.md` |
| 10 | [Evaluate](#evaluating) | Fresh sub-agents | One skill each (or none) | Outputs, grades, `benchmark.json` |

The rules that decide what goes into the skill are fixed in advance, in the merge prompt (step 6) and the check prompt (step 7):

- a rule needs two or more independent sources;
- conflicts resolve to the most specific rule none of the sources contradicts;
- nothing the baseline already states gets in, unless two or more sources break it by mistake rather than by design.

Fixing them in advance means the only judgment calls left are the ones written into those prompts, made by forks of the model being measured.

## What each context may see

The skill must carry ideas, not any source's wording, and must not restate the baseline. Two kinds of contamination are kept out:

- **Source wording.** Only steps 3–5 and 7 see the sources or quotes from them. Everything after that reads files made by `method/scripts/` or written under a no-quotes, no-names rule, and `method/scripts/leak_check.py` checks each of them.
- **The baseline.** The writer (step 9) is a fresh session, not a fork. A fork of the baseline's author would pull the baseline's structure and wording back into a skill meant to leave them out. Its only input, `kept.md`, has the baseline citations and process notes stripped out by `method/scripts/build_kept.py`. Neither the baseline nor any developer-docs skill may be installed while it runs, this repo's included.

## Evaluating

Iteration 1 has run for developer-docs and readme-rewrite, one run per setup. After it, six assertions in `evals/developer-docs/evals.json` that no output could pass were reworded: ones that needed a help channel or a page address no input gave, and ones that demanded one form (mutual links, a callout, a dedicated module) where the rule asks only for the effect. Iteration 1's grades used the earlier wording, which git history keeps. The procedure, following `method/vendor/agent-skills/references/evaluating-skills.md`:

1. For each eval in `evals/developer-docs/evals.json`, run fresh sessions, one per setup: the run's skill, the run's baseline, no skill, and the current default when the run isn't the default's. Each gets its own copy of the eval's input file. Record each run's tokens and duration when it finishes.
2. One fresh grader per eval sees the outputs under shuffled letters, not knowing which is which, plus the assertions. It writes `grading.json` per output with quoted evidence, and a blind comparison.
3. Aggregate pass rate, tokens and time per setup into `benchmark.json`, also broken down by each rule's Kind in the run's `kept.md`.
4. Run each setup three times before trusting the differences.

Put the workspace at `${RUN}/workspace/iteration-N/`. Keep `evals/developer-docs/` fixed across runs, or comparisons between models mean nothing. A run's skill replaces the default in `skills/` only if it beats it.

Real tasks count as evals too. For each, keep the target repo's commit, the brief word for word, the session ID, tokens and time, whether the skill triggered without being named, every correction given, and a separate commit for hand fixes. Then the task can be rerun with a later version of the skill, the baseline, or none.

## Repeating it

For another model, effort level or provider:

1. Clone this repo and run `mise install` (or install uv).
2. Fetch the sources: `mise run fetch -- <SRC>`. It makes shallow, sparse clones at the pinned commits, and leaves any existing checkout alone.
3. Make `runs/<provider>-<model>-<version>-<effort>/` and an empty `<WORK>` folder.
4. Install `method/vendor/agent-skills` as a skill. Uninstall every developer-docs skill and any baseline.
5. Run steps 1–2 on the target model at the target effort (`mise run prompt -- recall`, then `-- baseline`). Measure how much of the context the fork point already uses.
6. Run steps 3–9, getting each prompt from `mise run prompt`. For each source: `reading`, check the file list it prints a note about, then `after-reading` if the source has one, then `compare`. Move the baseline into `${RUN}/baseline/` before step 9.
7. Copy `<WORK>`'s files into `${RUN}/pipeline/`, with the findings in `${RUN}/pipeline/findings/`, write `${RUN}/README.md` the way the first run's does, and run `mise run check`.
8. Evaluate against the same `evals/developer-docs/`, and against the current default.

## Lessons from the first run

- **Measure before reading.** A reading fork needs room for its pages and then the comparison. In the first run, with a 1M-token window, about 1.2–1.5 MB of source fit, and two forks crashed above that. Check the fork point's context use first, keep each scope well under the rest, and check the sub-agent's file list (folder, count, skipped sections) before the fork reads anything.
- **Never compact a reading fork.** The comparison needs exact wording. If one runs out of room, rewind it to the reading-order message, narrow the scope, and fork that point again.
- **Check each findings file before ending its fork.** Run the leak check on its Abstracted section and verify two claims against the source. A fork can still fix a weak claim; once it's gone, nothing can.
- **Ask every source about mixing modes.** The baseline's "one kind of documentation per page" rule was the one real conflict. The template now asks every source for its position.
- **A reader judging the baseline sides with it.** Readers are forks of the baseline's author, so their "where the source falls short" group leans toward the baseline. Step 7 re-decides those items on evidence, and its "deliberate" test now requires a count and a contradiction of the rule ([why](prompts/07-check-often-broken.md#changes-since-the-first-run)).
- **Silence isn't a choice.** A style guide that doesn't forbid something hasn't endorsed it. Only templates, style guides, or a pattern on nearly every page of a kind count as deliberate.
- **The writer must not be the author.** The baseline's author is the best judge of what's redundant, and that judgment belongs in the merge. Writing belongs to a session that has never seen the baseline.
- **Stating isn't doing.** The merge's rule 4 drops a cluster the baseline already states. In the Sonnet 5.5 run, it dropped "show the problem or failure before the remedy", which four sources backed, because the baseline stated it. That baseline scored no better than no skill in evals, so Sonnet doesn't follow what it states, and the skill passed 51% of assertions on Sonnet, against 80% for the default made for Opus. Before trusting rule 4 for a new model, eval its baseline against no skill. If the baseline doesn't help, keep the stated rules too.
- **Evals favor the run they were written from.** `evals/developer-docs/` was written from the first run's rules, so it measures coverage of those rules. Read a later run's results with that in mind, and add assertions for a run's own rules before calling it worse.
- **Keep ad-hoc judgment out.** In the first run, a by-hand check of the "often broken" entries agreed with the checker fork on only 9 of 13, and the checker had the better evidence each time. Checks done outside a fixed prompt aren't repeatable for the next model, so every check is a prompt or a script.

## Licensing of the run files

The repo follows the [REUSE specification](https://reuse.software/): `REUSE.toml` gives each file's copyright and license, and `LICENSES/` holds every license text. Check it with `mise run check`, which runs `uvx reuse@6.2.0 lint` along with the other checks.

Everything is dedicated to the public domain under [CC0 1.0](../LICENSES/CC0-1.0.txt), except the files described below. Agents wrote most of the text and code, so how much copyright exists in it is unclear; CC0 waives whatever does.

The findings files in `runs/*/pipeline/findings/` quote their sources, and each opens with a notice naming its source, copyright holder and license. The quotes are short and used to compare and criticize. React (CC BY 4.0), Ember (MIT), Django (BSD 3-Clause), Rust (MIT or Apache-2.0) and PostgreSQL (PostgreSQL License) are permissive. Rails (CC BY-SA 4.0) and MDN (CC BY-SA 2.5) are share-alike, so the three files that quote them are licensed under those licenses. That applies per file, not to the rest of the repo.

`skills/readme-rewrite/` is licensed under [MIT-0](../LICENSES/MIT-0.txt), as its frontmatter says. `method/vendor/agent-skills/` is licensed under [CC BY 4.0](../LICENSES/CC-BY-4.0.txt). Its references are adapted from the Agent Skills documentation, and its `NOTICE.md` gives the credit and lists the changes.

Everything from `abstracted-full.md` onward, the skill included, contains no source wording; `method/scripts/leak_check.py` checks the files that matter.

## Variants for other models

`skills/developer-docs/` is the default, made for one model. Every other run's skill stays in its own `runs/<run>/skill/developer-docs/`, and is installed from a clone by path. A run's skill replaces the default only if it beats the default on the default's own model. A skill made for another model is a variant, not a replacement.

The first variant didn't earn its place. On Claude Sonnet 5.5, the default made for Opus 5.5 passed 80% of assertions, and the variant the method made for Sonnet passed 51%, no better than no skill. So before running the method for a model, run the evals of the default on it. Run the method itself mainly for a model at least as strong as the default's, where it could make a better default.

## Running it headless

Every step can run without a person at the keyboard, through Claude Code's command line (v2.1.311). These commands were tried for the first time with Claude Sonnet 5.5:

- Start a session with a known ID: `claude -p --model <model> --effort <level> --session-id <uuid> --output-format json "<prompt>" < /dev/null`.
- Continue it: `claude -p --resume <uuid> ... "<next prompt>"`.
- Fork it: `claude -p --resume <uuid> --fork-session ... "<prompt>"`. The fork starts from everything the session had, gets its own ID, and leaves the original unchanged. Forks don't see each other.
- Put the prompt right after `-p`. `--allowedTools` and `--add-dir` take several values, so a prompt placed after them is read as one of their values.
- Measure context from the session's transcript, not the JSON result: in Claude Code, the last assistant message's usage in `~/.claude/projects/<cwd>/<session>.jsonl`. The result's `usage` is summed over the session's calls. `modelUsage.<model>.contextWindow` gives the window.
- Count cost from running totals. A continued session's `total_cost_usd` and `modelUsage` are totals for the whole session so far, and a fork's include the session it was forked from. A session's cost is its last result's total, minus its parent's total at the fork point; adding up every result counts earlier calls again.
- Check a reading list before the fork reads it: run the reading-order message with `--max-turns 1`, check the list, then continue the session with: "The list is correct. Read every file on it, in that order, in full. Then wait for my next message."
- Give a session only the tools a step needs with `--allowedTools`, keep it to the run's folders with `--add-dir`, and run it from `${WORK}`.

For evals, start every run as a fresh session with `--disallowedTools Skill`, and give the skill by path in the prompt, so no installed skill can join the run.

What the first eval run learned about headless sessions:

- Use `--permission-mode acceptEdits` with an `--allowedTools` list. Never use `--dangerously-skip-permissions`: it removes every check, and Claude Code's auto mode blocks it anyway.
- Without a tool, a session can't do the work: without Write it can't save its output, and without the right Bash commands it can't run its examples. Allow `uv run --with <package>`, so a run can install what its examples need without touching the system. Expect compound commands such as `cd … && …` to be denied, and allow the simple ones a step needs.
- The eval prompts don't say where to save output. Add one sentence to every run's prompt, the same for every setup: "Save what you write as Markdown files in the outputs/ folder of the current directory."
- Take each run's tokens and time from the JSON result's `duration_ms` and `modelUsage`.

## Running it with Codex

The same mechanics work in OpenAI's Codex CLI (tried with codex-cli 0.170.0):

- Start a session: `codex exec --json -m <model> -c model_reasoning_effort=<level> -s <sandbox> --skip-git-repo-check "<prompt>" < /dev/null`. The first JSON event's `thread_id` is the session's ID.
- Continue it: `codex exec <options> resume <thread_id> "<prompt>"`. Fork it: `codex exec <options> fork <thread_id> "<prompt>"`. The options go before `resume` or `fork`, which reject them after. A fork recalls everything the session had, and forks don't see each other.
- Each `turn.completed` event reports `usage`. On a ChatGPT plan, Codex counts usage against the plan's limits rather than billing tokens, so check how much a step uses before running the rest.
- Models depend on how you sign in: with a ChatGPT account, `gpt-6.2-luna` was refused while `gpt-6-luna`, `gpt-reserve` and `gpt-6.2-sol` worked. `~/.codex/models_cache.json` lists what Codex offers.

## Next experiments

In order, each cheaper than the next, and each deciding whether the next is worth its cost:

1. **Fix rule 4, then rerun only the Sonnet run's merge, check and writer.** Keep a rule the baseline states unless evals show the baseline helps, and feed back the clusters it dropped as redundant. There's no rereading of sources, so it costs a few dollars. If the new skill closes the gap to the default on Sonnet (51% against 80%), the shortfall was the method, not Sonnet's reading.
2. **Run iterations 2 and 3 of the existing evals,** so the differences rest on three runs per setup.
3. **Then, if either points that way, a hybrid run:** the target model's baseline, with the strongest model reading, auditing, merging and writing. Forks can't cross models, so the readers would get the baseline's files as given context instead of forking its session. An all-Fable run would likely do worse for Opus and Sonnet: its baseline would state more rules, so rule 4 would drop rules that Fable states and smaller models don't follow.

The GPT-6-Luna trial (`runs/openai-gpt-6-luna-medium/`) found accurate but shallow findings, so a full run on a small model isn't on this list.

## Releasing

Both skills share the repository's version, in each `SKILL.md`'s `metadata.version`.

1. Set every skill's `metadata.version` to the new version, and run `mise run check`.
2. Build the ZIPs: `mise run release -- <version>`. It refuses if any skill is at another version, and writes one ZIP per skill to `dist/`, which git ignores.
3. Publish: `gh release create v<version> dist/*.zip --title v<version> --notes-file <notes>`.
