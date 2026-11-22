I didn't write an ADR. I added both rules to `docs/design/cli-output.md` instead.

**Why not an ADR:** under the ADR skill, a decision only gets a record if it settles a requirement that shapes the system's structure and would be expensive to undo. Rules people look up while coding don't pass. "Use `say()`, not `print()`" and "abbreviate units" are rules like that. Changing either later means editing some strings and calls, not rewriting a layer or breaking anything users already have. The project's log is also meant to hold only architecturally significant decisions, so these would dilute it.

**What I changed in `docs/design/cli-output.md`:**
- **New "Printing" section:** everything larder prints goes through `say()` in `src/larder/ui.py`, and no other module calls `print()`. I checked the code, and the only `print()` is the one inside `say()`.
- **Added to "Units":** units are always printed abbreviated (`mg`, `g`, `kg`, `ml`, `l`), never spelled out, e.g. `250 ml`, not `250 millilitres`.

**Choices you may want to change:**
- I included `mg` in the list, even though you named only g, kg, ml and l, because the doc already lists it as an accepted unit.
- I didn't name who agreed on Friday or give a date, since that isn't recorded anywhere I could check.
- Nothing enforces either rule yet. The existing tests don't cover them. A test that fails if `print(` appears outside `ui.py` would cover the first rule, and I can add one if you want.

If you still want an ADR, I can write one. It would be `0010` or higher, because the research notes mention a deleted ADR 0009 and the skill never reuses a number.