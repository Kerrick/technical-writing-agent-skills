# Notice

Five files in `references/` are adapted from the Agent Skills documentation at [agentskills.io](https://agentskills.io), by the Agent Skills project contributors ([github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

| File | Source |
| - | - |
| `references/specification.md` | <https://agentskills.io/specification.md> |
| `references/writing-instructions.md` | <https://agentskills.io/skill-creation/best-practices.md> |
| `references/descriptions.md` | <https://agentskills.io/skill-creation/optimizing-descriptions.md> |
| `references/evaluating.md` | <https://agentskills.io/skill-creation/evaluating-skills.md> |
| `references/scripts.md` | <https://agentskills.io/skill-creation/using-scripts.md> |

Changes from the originals:

- All five: condensed into rules for an agent that already knows the format, with explanations it doesn't need removed; renamed; each opens with when to read it; docs-site markup removed; links to the other pages pointed at this skill's files; links to the `skill-creator` skill removed.
- `references/specification.md`: the field rules gathered into one table, the examples merged, and the validation command corrected to `uvx --from skills-ref@0.1.1 agentskills validate`, since the `skills-ref` package installs a command named `agentskills`.
- `references/writing-instructions.md`: the example code blocks replaced by one-line examples.
- `references/descriptions.md`: the Bash trigger-test script replaced by how to detect a skill load in Claude Code; the query count widened to 16–20; added a boundary with sibling skills to the description advice, near-misses from sibling skills to the queries, and the setup trigger tests need, with sibling skills installed.
- `references/evaluating.md`: evals moved outside the skill folder, and kept fixed once results exist; assertions name the rule they test; runs isolated by giving the skill by path with the skill tool disabled; a third setup (the baseline or previous version) added beside with-skill and without-skill; grading made blind across all setups; results broken down by rule and kind; three runs per setup; added fixtures with planted flaws, no placeholders in eval files, recording real tasks as evals and running sessions headless in Claude Code.
- `references/scripts.md`: the one-off runners gathered into a table, the language examples shortened, a default runner and language named, and added testing a script the way an agent runs it.

`SKILL.md`, `references/measured-build.md`, and this notice were written for this skill. `scripts/validate.py` is copied unchanged from the agent-skills skill, where it was written and offered under CC BY 4.0. It depends on, but does not include, the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) library (Apache-2.0). This skill is offered under CC BY 4.0 as a whole.

The material is provided as-is, without warranties, as stated in the license.
