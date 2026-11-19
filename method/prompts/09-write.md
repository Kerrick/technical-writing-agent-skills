# 9. Write

A **fresh session, not a fork**, on the target model and effort level, started in this repo. It has never seen the baseline, the findings, or the merge: its context is the agent-skills skill and `kept.md`, nothing else. A fork of the baseline's author would pull the baseline's structure and wording back in, which is exactly what this skill must leave out.

Before starting it, make sure neither the baseline nor any developer-docs skill is installed, including this repo's own `skills/developer-docs`. Otherwise its description is in the session's skill list, and the session could load it. The agent-skills skill, from `${AGENT_SKILLS}`, should still be installed.

This is the prompt as the method now stands. The first run's differed in two ways, recorded in its run README: its writer wrote the skill straight into the run folder, and its item 5 had the writer create the repo's shared `evals/developer-docs/` (4–5 output evals with assertions naming the rules they test, plus about 20 trigger queries). Every later run uses those evals unchanged.

```
Load the agent-skills skill and read all of its reference files in full. Then read ${WORK}/kept.md in full, and nothing else in that folder or in this repo's runs/ directory.

Write a new skill to ${RUN}/skill/developer-docs/, following the agent-skills skill and its references. Its readers are agents that already know standard technical writing practice. So:

1. Content: every rule in kept.md, and nothing else of substance. Each rule's Kind tells you how to treat it: "not commonly known" is new to the reader; "overrides common advice" replaces advice the reader probably follows, so state it plainly as the rule; "well known, often broken" is something the reader knows but skips; "set by the maintainer" is required by the person who owns the skill, so state it as written.
2. Backbone: a short workflow and a pre-publish checklist that the rules hang on. Put the "well known, often broken" rules in the checklist. Use each rule's "Applies to" to place it: rules for every page in SKILL.md; rules for one kind of page in a reference file for that kind, with SKILL.md saying when to read it. Turn each "Without it" into a gotcha where it's a mistake an agent would make. Add nothing else from your own knowledge beyond what the backbone needs to make sense. When in doubt, leave it out.
3. No placeholders: the skill must never tell an agent to write a placeholder, a question, or a note to the maintainer into a file. Where a rule says to mark or flag something for the maintainer, have the agent leave it out or raise it in chat instead.
4. Size: SKILL.md under 500 lines and 5,000 tokens. No reference file that nothing points to.
5. Frontmatter: name developer-docs; a description in imperative form that says when to use it, for developer-facing tutorials, guides, reference, explanations, books, courses and video scripts, including requests that don't say "docs", and says it's not for READMEs (readme-rewrite) or UI microcopy; metadata with author: Kerrick Long and version: "0.1".
6. Evals: don't write any. This repo's evals/developer-docs/ are shared by every run and must stay fixed.
7. Validate: run `uv run ${AGENT_SKILLS}/scripts/validate.py <skill dir>` and fix any errors until it passes.

Finish by writing ${RUN}/PLACEMENT.md: a table of each rule's kept.md number and heading, and where the skill states it, as a path and line relative to ${RUN}/skill/, such as `developer-docs/SKILL.md:24`, one or more per rule. Every rule must appear. Then report the line counts and the validator output.
```

Check:

- `uv run ${AGENT_SKILLS}/scripts/validate.py <skill dir>` passes.
- `uv run method/scripts/leak_check.py <skill dir>/SKILL.md <skill dir>/references/*.md` passes.
- `uv run method/scripts/check_placement.py ${RUN}/PLACEMENT.md ${WORK}/kept.md ${RUN}/skill` passes, and a sample of cited lines state their rule.
- The session's transcript shows it loaded only agent-skills and read only `kept.md`. (In Claude Code, transcripts are in `~/.claude/projects/<repo path>/*.jsonl`.)
- Delete anything the session's own testing left behind, such as `__pycache__/`.

The new skill becomes the default, copied into `skills/developer-docs/`, only if the evals show it beating the current default. The old default then moves to its own run's `skill/developer-docs/`.
