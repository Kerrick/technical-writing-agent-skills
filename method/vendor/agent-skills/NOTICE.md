# Notice

The files in `references/` are adapted from the Agent Skills documentation at [agentskills.io](https://agentskills.io), by the Agent Skills project contributors ([github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

| File | Source |
| - | - |
| `references/specification.md` | <https://agentskills.io/specification.md> |
| `references/best-practices.md` | <https://agentskills.io/skill-creation/best-practices.md> |
| `references/optimizing-descriptions.md` | <https://agentskills.io/skill-creation/optimizing-descriptions.md> |
| `references/evaluating-skills.md` | <https://agentskills.io/skill-creation/evaluating-skills.md> |
| `references/using-scripts.md` | <https://agentskills.io/skill-creation/using-scripts.md> |

Changes from the originals:

- Removed docs-site markup: `[card]` and `[tab]` blocks became plain content and `###` headings, and `theme=` and `highlight=` code-fence attributes were dropped.
- `references/using-scripts.md`: fixed the link to the `compatibility` field (added the missing `.md`).
- `references/specification.md`: corrected the validation command to `uvx --from skills-ref@0.1.1 agentskills validate`, since the `skills-ref` package installs a command named `agentskills`, and noted the bundled `scripts/validate.py`.

`SKILL.md` and `scripts/validate.py` were written for this skill and are offered under the same license. `scripts/validate.py` depends on, but does not include, the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) library (Apache-2.0).

The material is provided as-is, without warranties, as stated in the license.
