# Technical writing agent skill

An [Agent Skill](https://agentskills.io) for developer-facing documentation (tutorials, how-to guides, reference, explanations, books, courses and video scripts), plus the method that made it.

The skill holds only what a given model doesn't already do: rules that seven famous documentation sets follow and the model's own idea of good docs leaves out, corrects, or knows but skips. It assumes its reader already knows standard technical writing practice. That gap differs by model and effort level, so each skill lives under the model it was made for: `<provider>/<model>/<version>/<effort>/`.

| Path | What it is |
| - | - |
| `claude/opus/5.5/medium/technical-writing/` | The skill, for Claude Opus 5.5 at medium effort, with its evals |
| `claude/opus/5.5/medium/baseline/technical-writing/` | The baseline: the skill the same model wrote from memory, which the new skill is defined against |
| `claude/opus/5.5/medium/pipeline/` | Every intermediate file, in the order the steps made them |
| `claude/opus/5.5/medium/pipeline/findings/` | One comparison per source, with quoted evidence (see [Licensing](#licensing)) |
| `claude/opus/5.5/medium/PLACEMENT.md` | Where the skill states each rule it was given |
| `prompts/` | Every prompt, word for word as run |
| `sources.md` | The seven sources: repositories, commits, scopes and per-source prompt values |
| `scripts/` | The extraction and check steps |

## Using the skill

Install it as a symlink, so improvements here reach every agent:

```
ln -s ~/Developer/technical-writing-agent-skill/claude/opus/5.5/medium/technical-writing ~/.agents/skills/technical-writing
```

Use it with the model and effort level it was made for. Never install the baseline at the same time: they share a name, and the new skill assumes its reader hasn't seen the baseline.

## Status

| Step | Done for Opus 5.5 medium? |
| - | - |
| Steps 1–9 below: baseline, reading, audit, merge, check, writing | Yes. The skill passes the validator, the leak check and the placement check. |
| Output evals: new skill against baseline and no skill | Not yet run. See [Evaluating](#evaluating). |
| Trigger evals (`evals/eval_queries.json`) | Not yet run. |
| Real tasks | Planned: docs for two of the author's repos. |

## The method

Each step runs in one of three kinds of context, and what a context may see is the point of the design:

- **A fork of the baseline point:** the session that just wrote the baseline, forked before anything else is sent. It knows the baseline as its own beliefs.
- **A fresh session:** knows only what its prompt gives it.
- **A script:** no judgment at all.

| # | Step | Context | Reads | Writes |
| - | - | - | - | - |
| 1 | [Recall](prompts/01-recall.md) | New session | Nothing | Nothing |
| 2 | [Baseline](prompts/02-baseline.md) | Same session | The agent-skills skill | The baseline skill. **The fork point.** |
| 3 | [Reading order](prompts/03-reading-order.md) | One fork per source | A Sonnet sub-agent's file list, then the pages | Nothing |
| 4 | [Compare](prompts/04-compare.md) | Same fork | The source's style guide | `findings/<source>.md` |
| 5 | [Audit](prompts/05-audit.md) | New fork | All findings files, with quotes | `abstracted-full.md`: anonymized, no quotes |
| 6 | [Merge](prompts/06-merge.md) | New fork | `abstracted-full.md` only | `merged.md` |
| 7 | [Check "often broken"](prompts/07-check-often-broken.md) | New fork | `merged.md`, the findings, the source checkouts | `often-broken-check.md` |
| 8 | [Apply the check](prompts/08-apply-check.md) | Script, then the merge fork | `for-the-writer.md` only | Updated `merged.md`; then `kept.md` by script |
| 9 | [Write](prompts/09-write.md) | **Fresh session** | The agent-skills skill and `kept.md` only | The skill, its evals, `PLACEMENT.md` |
| 10 | [Evaluate](#evaluating) | Fresh sub-agents | One skill each (or none) | Outputs, grades, `benchmark.json` |

The rules that decide what goes into the skill are fixed in advance, in the merge prompt (step 6) and the check prompt (step 7):

- a rule needs two or more independent sources;
- conflicts resolve to the most specific rule none of the sources contradicts;
- nothing the baseline already states gets in, unless two or more sources break it by mistake rather than by design.

Fixing them in advance means the only judgment calls left are the ones written into those prompts, made by forks of the model being measured.

### What each context may see

The skill must carry ideas, not any source's wording, and must not restate the baseline. Two kinds of contamination are kept out:

- **Source wording.** Only steps 3–5 and 7 see the sources or quotes from them. Everything after that reads files made by `scripts/` or written under a no-quotes, no-names rule, and `scripts/leak_check.py` checks each of them.
- **The baseline.** The writer (step 9) is a fresh session, not a fork. A fork of the baseline's author would pull the baseline's structure and wording back into a skill meant to leave them out. Its only input, `kept.md`, has the baseline citations and process notes stripped out by `scripts/build_kept.py`. No technical-writing skill may be installed while it runs.

## Evaluating

Not yet run. The plan, following agent-skills' `references/evaluating-skills.md`:

1. For each eval in `technical-writing/evals/evals.json`, run three fresh sub-agents: one told to read and follow the new skill's `SKILL.md`, one the baseline's, one with no skill. Each gets its own copy of the eval's input file. Record each run's tokens and duration from its completion notice; nothing else stores them.
2. One fresh grader per eval sees the three outputs as X, Y and Z, not knowing which is which, plus the assertions. It writes `grading.json` per output with quoted evidence, and a blind comparison.
3. Aggregate pass rate, tokens and time per setup into `benchmark.json`, also broken down by each rule's Kind in `kept.md`.
4. Run each setup three times before trusting the differences.

Put the workspace at `claude/opus/5.5/medium/workspace/iteration-N/`. The evals were written by the new skill's writer and test its rules. Keep them fixed when comparing models, or the comparison means nothing.

Real tasks count as evals too. For each, keep the target repo's commit, the brief word for word, the session ID, tokens and time, whether the skill triggered without being named, every correction given, and a separate commit for hand fixes. Then the task can be rerun with a later version of the skill, the baseline, or none.

## Repeating it

For another model, effort level or provider:

1. Make `<provider>/<model>/<version>/<effort>/` and an empty working folder. The prompts use `~/Developer/technical-writing-deltas/` as the working folder; change that path everywhere if you use another.
2. Uninstall any technical-writing skill.
3. Run steps 1–2 on the target model at the target effort. Move the baseline out of the installed skills folder into `baseline/` before step 9.
4. Run steps 3–9 with the same sources, scopes and commits from `sources.md`, and the same prompts. Change only paths and model names.
5. Copy the working folder's files into `pipeline/` (findings into `pipeline/findings/`).
6. Evaluate with the same eval set as earlier models.

## Lessons from the first run

- **Measure before reading.** One fork holds about 1.2–1.5 MB of source. Two forks crashed above that. Split or narrow any scope over about 1.2 MB, and check the Sonnet sub-agent's file list (folder, count, skipped sections) before the fork reads anything.
- **Never compact a reading fork.** The comparison needs exact wording. If one crashes, rewind it to the reading-order message (conversation only), narrow the scope, and fork that point again.
- **Check each findings file before ending its fork.** Run the leak check on its Abstracted section and verify two claims against the source. A fork can still fix a weak claim; once it's gone, nothing can.
- **Ask every source about mixing modes.** The baseline's "one mode per page" rule was the one real conflict. The first three forks had to be asked for their position afterwards. The template now asks.
- **A reader judging the baseline sides with it.** Readers are forks of the baseline's author, so their "where the source falls short" group leans toward the baseline. Step 7 exists to re-decide those items on evidence. Tighten its "deliberate" test as described in [its prompt](prompts/07-check-often-broken.md#tighten-deliberate-next-time).
- **Silence isn't a choice.** A style guide that doesn't forbid something hasn't endorsed it. Only templates, style guides, or a pattern on nearly every page of a kind count as deliberate.
- **The writer must not be the author.** The baseline's author is the best judge of what's redundant, and that judgment belongs in the merge. Writing belongs to a session that has never seen the baseline.
- **Keep ad-hoc judgment out.** In the first run, a by-hand check of the "often broken" entries agreed with the checker fork on only 9 of 13, and the checker had the better evidence each time. Checks done outside a fixed prompt aren't repeatable for the next model, so every check in the pipeline is now a prompt or a script.

## Licensing

The repo follows the [REUSE specification](https://reuse.software/): `REUSE.toml` gives each file's copyright and license, and `LICENSES/` holds every license text. Check it with `uvx reuse@6.2.0 lint`.

Everything is dedicated to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt), except the findings files described below. Agents wrote most of the text and code, so how much copyright exists in it is unclear; CC0 waives whatever does.

The findings files in `pipeline/findings/` quote their sources, and each opens with a notice naming its source, copyright holder and license. The quotes are short and used to compare and criticize. React (CC BY 4.0), Ember (MIT), Django (BSD 3-Clause), Rust (MIT or Apache-2.0) and PostgreSQL (PostgreSQL License) are permissive. Rails (CC BY-SA 4.0) and MDN (CC BY-SA 2.5) are share-alike, so the three files that quote them are licensed under those licenses. That applies per file, not to the rest of the repo.

Everything from `abstracted-full.md` onward, the skill included, contains no source wording; `scripts/leak_check.py` checks the files that matter.

## How this was made

> I use three words for how code and prose comes to exist. Code or prose I wrote, I typed by hand, with nothing generated. Code or prose I wrought, an AI agent generated while I iterated with it, and I reviewed every change before committing it, so I take responsibility for every diff. Code or prose I requested, an agent built with little or no review from me, in the style of a "dark factory."

I wrote the prompts that start the method: the recall and baseline prompts in `prompts/01-recall.md` and `prompts/02-baseline.md`, and the reading-order prompts in `sources.md`. Everything else I requested. Agents (Claude Opus 5.5, with Claude Sonnet 5.5 listing files to read) wrote both skills, the findings and pipeline files, the evals, the other prompts, `sources.md`, the scripts, `REUSE.toml` and this README. The idea of a skill made only of the gap between a model's own baseline and famous documentation is mine, and so is each decision along the way; much of the pipeline's design came from an agent's proposals that I accepted, changed or rejected. In place of my review stand the agent-skills validator, `scripts/leak_check.py`, `scripts/check_placement.py`, `reuse lint`, and an agent's spot checks of each findings file's evidence against its source checkout. Under [declare-ai](https://declare-ai.org/1.0.0/assess.html), this is creative assistance.
