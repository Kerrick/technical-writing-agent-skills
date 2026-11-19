# Run: Claude Sonnet 5.5, medium effort

The second run of the method, finished 2026-11-19, and the first run done headless: every step was a `claude -p` session, started, forked and checked by an orchestrating agent, with no person at the keyboard. Its skill is in [`skill/developer-docs/`](skill/developer-docs/). It is a variant for Sonnet 5.5, not the default; the default stays `skills/developer-docs/` until evals show otherwise.

## What was used

| | |
| - | - |
| Model | Claude Sonnet 5.5 (`claude-sonnet-5-5`), medium effort. The harness reported a 1,000,000-token context window for every session. |
| File listing (step 3) | Sub-agents of the same model, started with the Agent tool |
| Harness | Claude Code v2.1.311, `claude -p --model sonnet --effort medium --output-format json < /dev/null`, run from `${WORK}` |
| agent-skills | The copy in [`method/vendor/agent-skills/`](../../method/vendor/agent-skills/), installed at `~/.agents/skills/agent-skills` (checked identical before the run) |
| Sources | The seven in [`method/sources.toml`](../../method/sources.toml), cloned fresh with `method/scripts/fetch_sources.py` at the commits pinned there |

No developer-docs skill, technical-writing skill or baseline was installed at any point. The baseline was written into `${WORK}` and moved here before step 9.

## Slots as run

| Slot | Value in this run |
| - | - |
| `${SRC}` | `<scratchpad>/sonnet-run/sources` |
| `${WORK}` | `<scratchpad>/sonnet-run/work` |
| `${RUN}` | `runs/claude-sonnet-5.5-medium`, given to the writer as an absolute path |
| `${AGENT_SKILLS}` | `~/.agents/skills/agent-skills` |
| `${LISTER}` | `Sonnet` (the default) |

`<scratchpad>` was the orchestrating agent's session-specific temporary folder, outside every repository.

## Sessions

Thirteen sessions: the baseline session, eleven forks of its fork point (eight reading forks, the audit, the merge, the check), and the fresh writer. [`pipeline/sessions.md`](pipeline/sessions.md) lists every invocation with its session ID, step, usage, and how full the context was when it ended.

| | |
| - | - |
| Fork point | 65,485 tokens used of 1,000,000 |
| Reading forks after reading | 489K–743K tokens (React highest, Ember lowest) |
| Reading forks after comparing | 572K–813K tokens |
| Input tokens, all sessions | 108.1M, of which 102.4M were cache reads and 5.7M cache writes |
| Output tokens, all sessions | 820,591 |
| Wall time | About 1 hour 25 minutes, with the eight reading forks run in parallel |

No scope was changed, because the window matched the first run's and every scope fit: 0.95–1.46 MB per fork. The Django list came back as 85 files (the check says about 81) and the Rust list as 111 (the check says about 112; `SUMMARY.md` has 111). Every fork was checked against its list after reading: each had read every listed file through its last line.

## What's here

| Path | Step | What it is |
| - | - | - |
| `baseline/developer-docs/` | 2 | The skill the model wrote from memory: a 72-line `SKILL.md` and three references, 315 lines in all. The model named it `developer-docs` itself, the same name the method gives the finished skill. |
| `pipeline/findings/` | 4 | One comparison per source, with quoted evidence. Each opens with its source notice; the Rails and MDN files are under their sources' share-alike licenses, as `REUSE.toml` records. |
| `pipeline/abstracted-full.md` | 5 | The audit's anonymized rules: 127 checked by its count, 62 marked [revised], none removed |
| `pipeline/merged.md` | 6, 8 | The merge, after the check was applied: 30 kept (13 missed principles, 11 corrections, 6 baseline, often broken), 47 dropped |
| `pipeline/often-broken-check.md` | 7 | The check, with evidence: 47 entry-source pairs, 23 lapses, 2 deliberate, 22 unexamined; one correction candidate (command blocks) |
| `pipeline/for-the-writer.md` | 8 | The check's writer-safe section |
| `pipeline/kept.md` | 8 | The writer's only input: 33 rules, the 30 kept plus the 3 maintainer rules |
| `pipeline/sessions.md` | all | Every session ID, step and usage |
| `skill/developer-docs/` | 9 | The skill: `SKILL.md` (160 lines) and two references, `reference-pages.md` and `walkthroughs-and-books.md` |
| `PLACEMENT.md` | 9 | Where the skill states each rule. Paths are relative to `skill/`. |

Check placement: `uv run method/scripts/check_placement.py runs/claude-sonnet-5.5-medium/PLACEMENT.md runs/claude-sonnet-5.5-medium/pipeline/kept.md runs/claude-sonnet-5.5-medium/skill`.

## Evals

Iteration 1, one run per setup, on Claude Sonnet 5.5 at medium effort, graded blind by Opus 5.5 against `evals/developer-docs/`:

| Setup | Assertions passed |
| - | - |
| This run's skill | 35 of 71 (51%) |
| This run's baseline | 36 of 71 (50%) |
| The default skill, made for Opus 5.5 | 57 of 71 (80%) |
| No skill | 37 of 71 (53%) |

Graders ranked the default first in all five evals. This run's skill holds 33 rules, against the default's 50, and lacks most of the teaching rules the evals check. Sonnet with no skill fails those rules too, so they were real gaps. `pipeline/merged.md` records why each went. Rule 4 dropped two as already stated by the baseline: "show the problem or failure before the remedy", which four sources backed, and "open with the outcome and close with a recap", which two backed. This run's baseline scored no better than no skill, so Sonnet doesn't do what its baseline says. Rule 2 dropped three more because only one source found each: prediction prompts, where to get help, and naming difficulty honestly. The evals were written from the first run's rules, which favors the default's coverage, but doesn't explain why Sonnet's own gaps went unfound. Results are in `workspace/iteration-1/`.

## How this run differed from the method as written

- **Headless, with limited tools.** Each session got `--allowedTools` for only what its step needed (file reading and writing, Grep and Glob; the Skill tool for steps 2 and 9; the Agent tool for step 3's file listing; Bash only for the writer, which runs the validator) and `--add-dir` for `${SRC}` and this repository. The step 1 session had no tools. The listing sub-agents still used Bash: a sub-agent's tools come from its own agent type, not from the parent's `--allowedTools`.
- **Step 1 produced no visible thinking.** The recall prompt asks the model to think of everything it knows and say OK. At medium effort the session replied "OK." in two seconds with zero thinking tokens. The prompt was sent as written and not repeated.
- **Checking the reading list needed an extra message.** The method says to check each sub-agent's file list before the fork reads anything. A headless fork reads in the same turn the list comes back, so every reading fork was first run with `--max-turns 1`, which stopped it after the listing sub-agent returned, the list was checked, and the fork was resumed with: "The list is correct. Read every file on it, in that order, in full. Then wait for my next message." The MDN fork's sub-agent ran in the background, the fork started reading as soon as the list arrived, and the turn cap caught it after 24 of 38 pages; its continuation said to read the files it had not read yet. The eight lists were right, so none was corrected.
- **The writer ran from `${WORK}`, not from this repository**, with the repository given through `--add-dir` and `${RUN}` as an absolute path, so that every session ran the same way.
- **The writer needed one follow-up message.** Its first `PLACEMENT.md` cited lines through a legend (`SKILL:24-25`, `REF:5-7`), which `check_placement.py` can't read. It was resumed with the check's command and output and asked to rewrite the citations as `file:line`, one line per citation, without touching the skill. It did, and the check passed.
- **The writer wrote `SKILL.md` and the references in one pass each.** The whole of step 9 took 88 seconds and 19 turns; the follow-up took 8 seconds.
- **The merge counted 131 rules where the audit counted 127.** The audit's total for source D omitted that source's second file's four corrections. The merge used its own count, and the orchestrator confirmed that all 131 rule IDs appear in exactly one cluster's member list.
- **The baseline was never installed and never edited.** It was written to `${WORK}/developer-docs/`, read in place by every fork, and moved to `baseline/` before step 9.
- Output evals and trigger evals haven't been run.
