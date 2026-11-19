# Reference entries: API, CLI, configuration, docstrings

Read this when writing reference entries or docstrings. These rules add to the ones in SKILL.md tagged for reference.

## Rules

**Document boundary behavior.** In every entry, state what happens on boundary and degenerate input: empty, missing, null, zero, negative, unnamed, non-ASCII, input that is already complete, and cases where nothing qualifies. Also state whether results arrive at once or later. State plainly any effect a reader might expect that does not happen. Choose examples on those boundaries, where readers would guess wrong, and show the exact result.

**State operational cost.** For each entry or option, state its cost: memory, speed, cost on large inputs, what it blocks or locks, and what other users or processes feel. Say whether it is safe for production, how much the choice actually matters, and which variant avoids the cost.

**Scale entries to their item.** Keep the section order fixed across entries of the same kind, but scale each entry to its item. Leave out sections and labels that would be empty instead of filling them with "None". Put many small items in one table, one row each: signature, a one-line description, and an example paired with its exact result. Variants and aliases share a row.

**End each entry with a set of task examples.** End an entry with a set of framed examples covering its common tasks and notable options, not a single minimal call.

## Gotchas

- Documenting only the happy path, so readers find the edge behavior in production.
- Documenting only what an entry does, so readers discover locking or memory costs in production.
- Giving every tiny function a full template full of "None" sections, burying the content.
- Ending an entry with one minimal call, so readers can't find the usage they need.
