I didn't write an ADR for this. Instead I added both rules to larder's existing design doc, `docs/design/cli-output.md`.

**Why not an ADR:** under the skill's test, an ADR has to resolve an architecturally significant requirement, and reversing it has to cost something real. These two rules don't meet that bar. "Route output through `say()`" and "abbreviate units" are conventions people check while they code, and undoing either is a quick find-and-replace. larder's README also keeps the two kinds of doc apart: `docs/decisions/` is for "one architecturally significant decision per record" and `docs/design/` explains "how each part works". As an ADR, this would mislead readers and agents about what the decision log is for.

**What I changed in `docs/design/cli-output.md`:**
- **Top of the doc:** everything larder prints goes through `say()` in `src/larder/ui.py`, and no other module calls `print()`.
- **Units section:** units are always printed abbreviated (`mg`, `g`, `kg`, `ml`, `l`), never spelled out. For example, `1.5 kg`, not `1.5 kilograms`. I included `mg` because larder already accepts it as input.

The code already follows the first rule: the only `print()` under `src/` is the one inside `say()`. If you want it enforced, a small test that fails when `print(` appears anywhere in `src/` outside `ui.py` would do it. I can add that if you like.

If you still want an ADR, tell me what was at stake on Friday: which options you weighed, and what would break or be expensive to change later. With that I can write a proper one.