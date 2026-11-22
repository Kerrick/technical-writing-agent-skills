I didn't write an ADR. I added Friday's decision to the existing design doc instead: `docs/design/cli-output.md`.

**Why it's not an ADR:** The ADR skill only records decisions that shape the system's structure and would be costly to undo. Its examples are a layer rewritten or users' data broken. These two rules are coding conventions. If you changed them later, you'd edit `say()` and a few strings, and nothing else in larder depends on them. Your two existing ADRs, 0002 and 0006, are the kind the skill means: undoing either would mean migrating every user's file. This doc already held the unit and colour rules, so these belong next to them.

**What I added:**
- **A new "Printing" section:** everything larder prints goes through `say()` in `src/larder/ui.py`, and code outside `ui.py` never calls `print()`. It also says why: colour is handled inside `say()`, so a bare `print()` would skip the colour rules.
- **A paragraph under "Units":** units are always printed abbreviated, never spelled out, e.g. `250 g` not `250 grams`.

**Calls you may want to overturn:**
- **`mg` is in the list.** You named g, kg, ml and l, but larder also accepts `mg`, so I listed it too.
- **Counts are a bare number.** I wrote that a count prints as a number with no unit. You didn't say this; I took it from the existing rule that a count is typed as a bare number.
- **Nothing enforces the rules yet.** The only `print()` in `src/` is the one inside `say()`, but no test or lint check stops a new one. A test that searches `src/` for `print(` outside `ui.py` would catch it. I can add that if you want.

I didn't add an ADR number or change any index or code citations.