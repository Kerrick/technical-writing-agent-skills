# Trial: GPT-6-Luna, medium effort

A partial run, to learn whether the method is worth running on a small model, on a ChatGPT Plus plan, through the Codex CLI (codex-cli 0.170.0). It stopped after one reading fork, by design.

| Step | Input tokens (cached) | Output tokens |
| - | - | - |
| 1–2, recall and baseline | about 253K (214K) | about 2.9K |
| 3, read the Ember Guides' Getting Started and Tutorial sections | 1.80M (1.67M) | 7.1K |
| 4, compare | 3.12M (2.97M) | 16.4K |

- **Window.** GPT-6-Luna's context window is 272K tokens, about 258K usable. A fork holds about 300 KB of documentation after the baseline and room to compare, so the trial read one coherent part of the Ember Guides, about 270 KB, instead of all of it.
- **Baseline.** `baseline/technical-writing/SKILL.md`, 85 lines, valid.
- **Findings.** `pipeline/findings/ember-guides-part1.md`. Its claims check out against the source, but it found six general principles, mostly from the Ember style guide, no corrections, and one shortfall. It missed the tutorial's most distinctive move, having learners do a task by hand before the abstraction that replaces it, though the pages it read show it repeatedly. From all of the Ember Guides, Claude Opus 5.5 found 14 principles and 8 corrections.
- **Verdict.** A full run on GPT-6-Luna isn't worth its cost. Evals of the default skill on it would show what its users should install.
