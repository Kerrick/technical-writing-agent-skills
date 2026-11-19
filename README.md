# Technical writing agent skill

An [Agent Skill](https://agentskills.io) for developer-facing documentation: tutorials, how-to guides, API and CLI reference, explanations, books, courses and video scripts. This repo also holds the method that made it, so it can be made again for other models, and a companion skill, readme-rewrite, for the one kind of page technical-writing leaves out.

The skill holds only what a given model doesn't already do: rules that seven famous documentation sets follow and the model's own idea of good docs leaves out, corrects, or knows but skips. It assumes its reader already knows standard technical writing practice. That gap differs by model and effort level. The default skill was made for **Claude Opus 5.5 at medium effort**, and works best there.

## Install

With the [skills CLI](https://github.com/vercel-labs/skills), for any supported agent:

```
npx skills add Kerrick/technical-writing-agent-skill -g
```

It asks which skills and which agents to install for. `-g` installs for your user rather than one project. Add `--skill technical-writing` or `--skill readme-rewrite` to install just one.

With git, on macOS or Linux, clone the repo and link the skill into your agent's skills folder. Linking means a `git pull` updates it.

```
git clone https://github.com/Kerrick/technical-writing-agent-skill.git ~/src/technical-writing-agent-skill
ln -s ~/src/technical-writing-agent-skill/skills/technical-writing ~/.claude/skills/technical-writing
ln -s ~/src/technical-writing-agent-skill/skills/readme-rewrite ~/.claude/skills/readme-rewrite
```

That's the folder for Claude Code. Agents that read `~/.agents/skills` (Codex, for example) use that folder instead.

On Windows, clone the repo the same way, then copy the skill folder:

```
Copy-Item -Recurse skills\technical-writing $HOME\.claude\skills\
Copy-Item -Recurse skills\readme-rewrite $HOME\.claude\skills\
```

Copy them again after each `git pull`.

## The two skills

- **technical-writing** covers tutorials, how-to guides, reference, explanations, books, courses and video scripts. It was made by the method below, so it holds only what its model doesn't already do.
- **readme-rewrite** covers READMEs, which technical-writing deliberately leaves out: rewriting or substantially editing one so it serves marketing, onboarding and indexing, with every claim checked against the code. It wasn't made by the method. It was written by request, the ordinary way, and holds full instructions rather than a gap.

## Layout

| Path | What it is |
| - | - |
| `skills/technical-writing/` | The default technical-writing skill |
| `skills/readme-rewrite/` | The companion README skill. Not made by the method. |
| `runs/<run>/` | One run of the method for one model and effort level: its baseline, every intermediate file, and (unless it's the default) its own skill. `runs/claude-opus-5.5-medium/` is the first. |
| `evals/` | The evals every run is tested against: `evals.json`, `eval_queries.json` and their input files |
| `method/prompts/` | Every prompt as the method now stands, with `${SLOTS}`. Each run's README records where that run differed. |
| `method/sources.toml` | The seven sources: repositories, commits, paths, and every per-source prompt value |
| `method/sources.md` | Why each source and scope was chosen |
| `method/scripts/` | Fetching sources, filling prompts, extracting files and every check, in Python |
| `mise.toml` | Tool versions and tasks: `mise run check`, `mise run fetch`, `mise run prompt` |
| `method/vendor/agent-skills/` | A pinned copy of the agent-skills skill, which steps 2 and 9 load |

## Status

| | Claude Opus 5.5, medium |
| - | - |
| Steps 1–9: baseline, reading, audit, merge, check, writing | Done. The skill passes the agent-skills validator, the leak check and the placement check. |
| Output evals: new skill against baseline and no skill | Not yet run |
| Trigger evals (`evals/eval_queries.json`) | Not yet run |
| Real tasks | Planned |

## Help wanted: spend your tokens

Each model needs its own run, and a run takes a dozen or so long sessions. If you have tokens to spare on Fable 5.2, Sonnet 5.5, Astra 6.2, Sol 6.2, Gemini 4 Neon, or anything else, a run on your model is the most useful thing you can contribute. So is running the evals for the first run, which nobody has done yet. See [CONTRIBUTING.md](CONTRIBUTING.md).

## The method

### What it needs

Any agent harness that can do four things:

1. **Fork:** copy a session at a point, so many sessions start from the same state. (Claude Code: `/fork`.)
2. **Rewind:** return a session to an earlier message, dropping what came after. (Claude Code: press Esc twice, or `/rewind`.)
3. **Show context use:** how full a session's context is. (Claude Code: `/context`.)
4. **Run a cheaper sub-agent** for mechanical work like listing files. (Claude Code: a Sonnet sub-agent.)

Plus git, and either [mise](https://mise.jdx.dev/) or [uv](https://docs.astral.sh/uv/). `mise install` installs the pinned Python and uv. Every script in `method/scripts/` runs with `uv run`, which supplies Python on any platform, and every mise task is one of those scripts.

### Slots

The prompts use these, so they work on any machine:

| Slot | Meaning |
| - | - |
| `${SRC}` | The folder holding the source checkouts, cloned by `mise run fetch` |
| `${WORK}` | An empty working folder for this run, outside any skills folder |
| `${RUN}` | This run's folder: `runs/<provider>-<model>-<version>-<effort>/` in this repo |
| `${AGENT_SKILLS}` | `method/vendor/agent-skills/`, installed as a skill |
| `${LISTER}` | The cheaper sub-agent model that lists files to read (default: Sonnet) |

Don't fill them in by hand. `mise run prompt -- <step> [--source <key>] --src … --work … --run …` prints any step's prompt with every slot and per-source value filled in, and refuses if one is missing; `mise run prompt -- --help` lists the steps. `runs/claude-opus-5.5-medium/README.md` gives the values from the first run.

### Steps

Each step runs in one of three kinds of context, and what a context may see is the point of the design:

- **A fork of the baseline point:** the session that just wrote the baseline, forked before anything else is sent. It knows the baseline as its own beliefs.
- **A fresh session:** knows only what its prompt gives it.
- **A script:** no judgment at all.

| # | Step | Context | Reads | Writes |
| - | - | - | - | - |
| 1 | [Recall](method/prompts/01-recall.md) | New session | Nothing | Nothing |
| 2 | [Baseline](method/prompts/02-baseline.md) | Same session | The agent-skills skill | The baseline skill. **The fork point.** |
| 3 | [Reading order](method/prompts/03-reading-order.md) | One fork per source | A sub-agent's file list, then the pages | Nothing |
| 4 | [Compare](method/prompts/04-compare.md) | Same fork | The source's style guide | `${WORK}/<source>.md` |
| 5 | [Audit](method/prompts/05-audit.md) | New fork | All findings files, with quotes | `abstracted-full.md`: anonymized, no quotes |
| 6 | [Merge](method/prompts/06-merge.md) | New fork | `abstracted-full.md` only | `merged.md` |
| 7 | [Check "often broken"](method/prompts/07-check-often-broken.md) | New fork | `merged.md`, the findings, the source checkouts | `often-broken-check.md` |
| 8 | [Apply the check](method/prompts/08-apply-check.md) | Script, then the merge fork | `for-the-writer.md` only | Updated `merged.md`; then `kept.md` by script |
| 9 | [Write](method/prompts/09-write.md) | **Fresh session** | The agent-skills skill and `kept.md` only | `${RUN}/skill/technical-writing/` and `${RUN}/PLACEMENT.md` |
| 10 | [Evaluate](#evaluating) | Fresh sub-agents | One skill each (or none) | Outputs, grades, `benchmark.json` |

The rules that decide what goes into the skill are fixed in advance, in the merge prompt (step 6) and the check prompt (step 7):

- a rule needs two or more independent sources;
- conflicts resolve to the most specific rule none of the sources contradicts;
- nothing the baseline already states gets in, unless two or more sources break it by mistake rather than by design.

Fixing them in advance means the only judgment calls left are the ones written into those prompts, made by forks of the model being measured.

### What each context may see

The skill must carry ideas, not any source's wording, and must not restate the baseline. Two kinds of contamination are kept out:

- **Source wording.** Only steps 3–5 and 7 see the sources or quotes from them. Everything after that reads files made by `method/scripts/` or written under a no-quotes, no-names rule, and `method/scripts/leak_check.py` checks each of them.
- **The baseline.** The writer (step 9) is a fresh session, not a fork. A fork of the baseline's author would pull the baseline's structure and wording back into a skill meant to leave them out. Its only input, `kept.md`, has the baseline citations and process notes stripped out by `method/scripts/build_kept.py`. No technical-writing skill may be installed while it runs, this repo's included.

## Evaluating

Not yet run. The plan, following `method/vendor/agent-skills/references/evaluating-skills.md`:

1. For each eval in `evals/evals.json`, run three fresh sub-agents: one told to read and follow the run's skill, one the run's baseline, one with no skill. Each gets its own copy of the eval's input file. Record each run's tokens and duration when it finishes.
2. One fresh grader per eval sees the three outputs as X, Y and Z, not knowing which is which, plus the assertions. It writes `grading.json` per output with quoted evidence, and a blind comparison.
3. Aggregate pass rate, tokens and time per setup into `benchmark.json`, also broken down by each rule's Kind in the run's `kept.md`.
4. Run each setup three times before trusting the differences.

Put the workspace at `${RUN}/workspace/iteration-N/`. Keep `evals/` fixed across runs, or comparisons between models mean nothing. A run's skill replaces the default in `skills/` only if it beats it.

Real tasks count as evals too. For each, keep the target repo's commit, the brief word for word, the session ID, tokens and time, whether the skill triggered without being named, every correction given, and a separate commit for hand fixes. Then the task can be rerun with a later version of the skill, the baseline, or none.

## Repeating it

For another model, effort level or provider:

1. Clone this repo and run `mise install` (or install uv).
2. Fetch the sources: `mise run fetch -- <SRC>`. It makes shallow, sparse clones at the pinned commits, and leaves any existing checkout alone.
3. Make `runs/<provider>-<model>-<version>-<effort>/` and an empty `<WORK>` folder.
4. Install `method/vendor/agent-skills` as a skill. Uninstall every technical-writing skill.
5. Run steps 1–2 on the target model at the target effort (`mise run prompt -- recall`, then `-- baseline`). Measure how much of the context the fork point already uses.
6. Run steps 3–9, getting each prompt from `mise run prompt`. For each source: `reading`, check the file list it prints a note about, then `after-reading` if the source has one, then `compare`. Move the baseline into `${RUN}/baseline/` before step 9.
7. Copy `<WORK>`'s files into `${RUN}/pipeline/`, with the findings in `${RUN}/pipeline/findings/`, write `${RUN}/README.md` the way the first run's does, and run `mise run check`.
8. Evaluate against the same `evals/`, and against the current default.

## Lessons from the first run

- **Measure before reading.** A reading fork needs room for its pages and then the comparison. In the first run, with a 1M-token window, about 1.2–1.5 MB of source fit, and two forks crashed above that. Check the fork point's context use first, keep each scope well under the rest, and check the sub-agent's file list (folder, count, skipped sections) before the fork reads anything.
- **Never compact a reading fork.** The comparison needs exact wording. If one runs out of room, rewind it to the reading-order message, narrow the scope, and fork that point again.
- **Check each findings file before ending its fork.** Run the leak check on its Abstracted section and verify two claims against the source. A fork can still fix a weak claim; once it's gone, nothing can.
- **Ask every source about mixing modes.** The baseline's "one kind of documentation per page" rule was the one real conflict. The template now asks every source for its position.
- **A reader judging the baseline sides with it.** Readers are forks of the baseline's author, so their "where the source falls short" group leans toward the baseline. Step 7 re-decides those items on evidence, and its "deliberate" test now requires a count and a contradiction of the rule ([why](method/prompts/07-check-often-broken.md#changes-since-the-first-run)).
- **Silence isn't a choice.** A style guide that doesn't forbid something hasn't endorsed it. Only templates, style guides, or a pattern on nearly every page of a kind count as deliberate.
- **The writer must not be the author.** The baseline's author is the best judge of what's redundant, and that judgment belongs in the merge. Writing belongs to a session that has never seen the baseline.
- **Keep ad-hoc judgment out.** In the first run, a by-hand check of the "often broken" entries agreed with the checker fork on only 9 of 13, and the checker had the better evidence each time. Checks done outside a fixed prompt aren't repeatable for the next model, so every check is a prompt or a script.

## Licensing

The repo follows the [REUSE specification](https://reuse.software/): `REUSE.toml` gives each file's copyright and license, and `LICENSES/` holds every license text. Check it with `mise run check`, which runs `uvx reuse@6.2.0 lint` along with the other checks.

Everything is dedicated to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt), except the files described below. Agents wrote most of the text and code, so how much copyright exists in it is unclear; CC0 waives whatever does.

The findings files in `runs/*/pipeline/findings/` quote their sources, and each opens with a notice naming its source, copyright holder and license. The quotes are short and used to compare and criticize. React (CC BY 4.0), Ember (MIT), Django (BSD 3-Clause), Rust (MIT or Apache-2.0) and PostgreSQL (PostgreSQL License) are permissive. Rails (CC BY-SA 4.0) and MDN (CC BY-SA 2.5) are share-alike, so the three files that quote them are licensed under those licenses. That applies per file, not to the rest of the repo.

`skills/readme-rewrite/` is licensed under [MIT-0](LICENSES/MIT-0.txt), as its frontmatter says. `method/vendor/agent-skills/` is licensed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Its references are adapted from the Agent Skills documentation, and its `NOTICE.md` gives the credit and lists the changes.

Everything from `abstracted-full.md` onward, the skill included, contains no source wording; `method/scripts/leak_check.py` checks the files that matter.

## How this was made

> I use three words for how code and prose comes to exist. Code or prose I wrote, I typed by hand, with nothing generated. Code or prose I wrought, an AI agent generated while I iterated with it, and I reviewed every change before committing it, so I take responsibility for every diff. Code or prose I requested, an agent built with little or no review from me, in the style of a "dark factory."

I wrote the prompts that start the method: the recall and baseline prompts in `method/prompts/01-recall.md` and `method/prompts/02-baseline.md`, and the reading-order prompts in `method/sources.md`. Everything else I requested. Agents (Claude Opus 5.5, with Claude Sonnet 5.5 listing files to read) wrote the technical-writing skill and its baseline, the findings and pipeline files, the evals, the other prompts, `method/sources.md`, the scripts, `REUSE.toml` and this README. Agents also wrote readme-rewrite, at my request, outside this method. The idea of a skill made only of the gap between a model's own baseline and famous documentation is mine, and so is each decision along the way; much of the pipeline's design came from an agent's proposals that I accepted, changed or rejected. In place of my review stand the agent-skills validator, `method/scripts/leak_check.py`, `method/scripts/check_placement.py`, `reuse lint`, and an agent's spot checks of each findings file's evidence against its source checkout. Under [declare-ai](https://declare-ai.org/1.0.0/assess.html), this is creative assistance.
