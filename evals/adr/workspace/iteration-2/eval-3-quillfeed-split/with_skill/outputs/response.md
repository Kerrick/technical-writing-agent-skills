I split ADR 003 into a short decision record and a new design document. It is now about 45 lines and holds only the decision; the table layout, file naming, retention and cleanup schedule are in `doc/design/storage.md`.

**Where each section went**

| Old section of 003 | Now |
|---|---|
| Front matter, Context, Drivers, Options, Outcome, Confidence, Consequences | Still in `doc/adr/003.md`, word for word. I added one sentence at the end of the outcome pointing to the design doc. |
| Title "Storage" | Now "Article bodies are compressed files on disk, indexed in SQLite", the wording `doc/README.md` already used. The old title only named a topic. |
| Confirmation | Rewritten (see below). |
| Table layout | `doc/design/storage.md`, "Articles table" |
| File naming | `doc/design/storage.md`, "Body files" |
| Retention | `doc/design/storage.md`, "Retention" |
| Cleanup schedule | `doc/design/storage.md`, "Nightly cleanup", now a numbered list. It also says what the orphan-file sweep is for (files left behind by a crash). |
| History | Dropped. It's old trial runs and release numbers, which git keeps. The reasons that matter (41 GB vs 310 MB, 19 minutes vs 9 seconds to copy) were already in the outcome. The record of why zstd level 9 was picked over 3 and 19 is in git history only. |

**Other changes**
- **Code comments:** two docstrings in `src/quillfeed/store.py` cited sections of ADR 003 that no longer exist. They now cite `doc/design/storage.md`. The module docstring still cites ADR 003, because it says why the store is built this way.
- **Index:** `doc/README.md` now lists the new design doc.

**Judgment calls**
- **Confirmation was wrong.** It said `tests/test_store.py` fails if the database grows by more than 2 KB. The only test there checks that a body's file goes in a two-character folder and ends in `.zst`. The ADR now says nothing checks that bodies stay out of the database. If you want one, the test the old text described would be a good one to add.
- **Date:** I set the `date` field to 2026-11-22, since it records the day the ADR was last updated. Change it back to 2026-04-18 if your log uses it for the day the decision was made.
- **Not ADRs:** retention and the cleanup schedule are a product rule and a policy. That's why they went to the design doc rather than becoming ADRs of their own.

**Problems I found elsewhere but didn't change**
- **ADR 002 is out of date.** The code has had a queue per host since 0.8.0 (`src/quillfeed/fetch.py`, `notes/2026-10-fetch-queue.md`). `doc/design/fetching.md` and the docstrings in `fetch.py` still say this "follows ADR 002", which describes one poller. The fix is a new ADR 004 that states the per-host-queue decision in full, with deleting 002 and updating those citations in the same change. The October note already has the options and reasons. I can write it if you want.
- **Missing tests:** ADR 001 cites `tests/test_single_process.py` and ADR 002 cites `tests/test_poller.py`, and neither file exists.