I split ADR 003 in two. The ADR now holds only the storage decision, cut from 75 lines to 42. Table layout, file naming, retention and the cleanup schedule are in a new design doc. I kept the number 003, because that one decision still meets the bar for an ADR: undoing it would mean moving every stored body.

**Files changed**
- `doc/adr/003.md`: now holds just the decision. The title states the decision (it was just "Storage") and matches the index.
- `doc/design/storage.md` (new): how storage works today, written in the same style as `fetching.md`.
- `src/quillfeed/store.py`: the two docstrings that cited ADR 003's "File naming" and "Retention" sections now cite `doc/design/storage.md`. The module docstring still cites ADR 003, since it explains why.
- `doc/README.md`: added the new design doc to the Design list.

**Where each old section went**

| Old section | Now |
| - | - |
| Context, Drivers, Options, Outcome, Confidence, Consequences | Still in ADR 003, unchanged, plus one line pointing to the design doc |
| Confirmation | Still in ADR 003, rewritten (see below) |
| Table layout, File naming, Retention, Cleanup schedule | `doc/design/storage.md`, same content. I split the cleanup schedule into numbered steps. |
| History | Removed. It covered the BLOB start, the 2 April stall, spike run IDs, the zstd level 3/9/19 trials, when the folders were added, and the 0.3.0/0.5.0 migration. That's the story of how the team got here, and git keeps the old text. The design doc just says "zstd level 9". |

**Things to check**
- **Confirmation was false.** It said `tests/test_store.py` fails if the database grows by more than 2 KB. That test only checks that a body's file goes in a two-digit folder with a `.zst` suffix. The ADR now says that nothing checks the database stays small. Adding the 2 KB test would be the real fix.
- Dropping History also drops the reasons for level 9 over level 19 (storing took 60 ms per article at level 19, and the walk fell behind). If you'd like a one-line reason next to "level 9" in the design doc, I can add it.

**Out of scope, but you should know:** ADR 002 is out of date. It says one poller walks every feed. But `notes/2026-10-fetch-queue.md` records Dana deciding on 19 October to give each host its own queue, which shipped in 0.8.0. `doc/design/fetching.md` already describes per-host queues. To fix this, write a new ADR 004 restating the fetch decision and delete 002, then update `fetch.py`, `fetching.md` and the index. I can do that next if you'd like.