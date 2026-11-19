# 9. Write

A **fresh session, not a fork**, on the target model and effort level, started in this repo. It has never seen the baseline, the findings, or the merge: its context is the agent-skills skill and `kept.md`, nothing else. A fork of the baseline's author would pull the baseline's structure and wording back in, which is exactly what this skill must leave out.

Before starting it, make sure no technical-writing skill is installed (`ls ~/.agents/skills/technical-writing` should fail). Otherwise its description is in the session's skill list, and the session could load it.

```
Load the agent-skills skill and read all of its reference files in full. Then read ~/Developer/technical-writing-deltas/kept.md in full, and nothing else in that folder or in this repo's baseline/ directory.

Write a new skill to ~/Developer/technical-writing-agent-skill/claude/opus/5.5/medium/technical-writing/, following the agent-skills skill and its references. Its readers are agents that already know standard technical writing practice. So:

1. Content: every rule in kept.md, and nothing else of substance. Each rule's Kind tells you how to treat it: "not commonly known" is new to the reader; "overrides common advice" replaces advice the reader probably follows, so state it plainly as the rule; "well known, often broken" is something the reader knows but skips.
2. Backbone: a short workflow and a pre-publish checklist that the rules hang on. Put the "well known, often broken" rules in the checklist. Use each rule's "Applies to" to place it: rules for every page in SKILL.md; rules for one kind of page in a reference file for that kind, with SKILL.md saying when to read it. Turn each "Without it" into a gotcha where it's a mistake an agent would make. Add nothing else from your own knowledge beyond what the backbone needs to make sense. When in doubt, leave it out.
3. Size: SKILL.md under 500 lines and 5,000 tokens. No reference file that nothing points to.
4. Frontmatter: name technical-writing; a description in imperative form that says when to use it, for developer-facing tutorials, guides, reference, explanations, books, courses and video scripts, including requests that don't say "docs", and says it's not for READMEs (readme-rewrite) or UI microcopy; metadata with author: setdef and version: "0.1".
5. Evals: write evals/evals.json with 4–5 realistic prompts. Between them, cover the kinds of page the rules apply to. Each assertion names the rule it tests by its kept.md heading, and together they cover as many rules as can be checked from output. Where a prompt names a file, write that file under evals/files/ and list it in "files". Also write evals/eval_queries.json: about 20 trigger queries, half should-trigger and half near-miss should-not-trigger, as optimizing-descriptions.md describes.
6. Validate: run `uv run ~/.agents/skills/agent-skills/scripts/validate.py <skill dir>` and fix any errors until it passes.

Finish by writing ~/Developer/technical-writing-agent-skill/claude/opus/5.5/medium/PLACEMENT.md: a table of each rule's kept.md number and heading, and the file:line where the skill states it. Every rule must appear. Then report the line counts and the validator output.
```

Check:

- `uv run ~/.agents/skills/agent-skills/scripts/validate.py <skill dir>` passes.
- `python3 scripts/leak_check.py <skill dir>/SKILL.md <skill dir>/references/*.md` passes.
- `python3 scripts/check_placement.py <PLACEMENT.md> <kept.md> <model dir>` passes, and a sample of cited lines state their rule.
- The session's transcript (`~/.claude/projects/<repo path>/*.jsonl`) shows it loaded only agent-skills and read only `kept.md`.
- Delete anything the session's own testing left behind, such as `__pycache__/`.
