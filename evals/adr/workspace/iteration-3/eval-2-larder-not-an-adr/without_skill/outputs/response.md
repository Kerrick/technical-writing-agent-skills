I didn't write an ADR. I added both rules to `docs/design/cli-output.md` instead, because larder's own docs say they belong there:

- **The decision log is "one architecturally significant decision per record"** (README). The two existing ADRs, one SQLite file (0002) and integer base units (0006), are expensive to undo and were chosen over named alternatives. Sending all output through `say()` and abbreviating units are output conventions. Either one could be changed in an afternoon.
- **`cli-output.md` already covers this.** It lists the units larder prints and the colour behaviour that `say()` handles. ADR 0006 even links there for "how it prints them."
- **An ADR would need parts I don't have.** I wasn't there on Friday, so I'd have had to make up the options you weighed and why you rejected them.

What I added:

- **A new "Printing" section:** everything goes through `say()` in `src/larder/ui.py`, and no other module calls `print()`. It also gives the reason: `say()` is where colour gets switched off for pipes and `NO_COLOR`, so a bare `print()` skips that check.
- **A line under "Units":** units are always printed abbreviated (`1.5 kg`, never `1.5 kilograms`), and a count is a bare number. I didn't list the units again because the paragraph above already does. That list includes `mg`, which yours left out; I assumed the abbreviation rule covers it too.

The code already follows the first rule: the only `print()` under `src/` is the one inside `say()`.

If you still want an ADR, for example because the Friday discussion did weigh real alternatives, tell me what they were and I'll write it as `0007` in the same format as the others.