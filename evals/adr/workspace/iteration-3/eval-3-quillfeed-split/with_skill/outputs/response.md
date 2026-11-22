ADR 003 now holds only the storage decision. The table layout, file naming, retention and cleanup schedule are in a new design document, and the History section is gone.

**What I changed**
- **`doc/adr/003.md`** is down from 75 lines to 44. Every option, reason and consequence is kept word for word. I changed three things:
  - The title "Storage" named a topic, so I replaced it with the decision as the index already words it: "Article bodies are compressed files on disk, indexed in SQLite".
  - I added a line at the end of the outcome pointing to the design document.
  - I rewrote Confirmation, because it was wrong (see below).
- **`doc/design/storage.md`** is new, written in the style of `fetching.md`. The articles table, the indexes and the full-text search table moved over unchanged. The file naming is now a short list. Retention and the nightly cleanup are short sections, with the three cleanup steps numbered.
- **`src/quillfeed/store.py`**: two comments pointed to ADR 003 sections for how things work, and now point to the design document. The module comment still cites ADR 003, since that one is about why.
- **`doc/README.md`**: added the new design document to the Design list.

**Where each old section went**

| Old section | Now |
| - | - |
| Context, Drivers, Options, Outcome, Consequences | Kept in ADR 003 |
| Confirmation | Kept in ADR 003, rewritten to match the test |
| Table layout | `storage.md`, "The articles table" |
| File naming | `storage.md`, "Body files" |
| Retention | `storage.md`, "Retention" |
| Cleanup schedule | `storage.md`, "Nightly cleanup" |
| History | Deleted |

**Decisions you may want to undo**
- **I deleted History.** It held spike-run IDs, how the compression level was chosen (level 3 gave bigger files, level 19 was too slow), why the two-letter folders were added, and the 0.3.0 migration from BLOBs. It's history, not how things work now. This folder isn't a git repository, so check that your real repository's history still has that text before you merge.
- **I didn't keep the reason for zstd level 9.** It was a tuning choice, not part of the ADR's decision. If you want the reason on record, it could go in one sentence in `storage.md`.
- **I rewrote Confirmation.** It said `tests/test_store.py` fails if the database grows by more than 2 KB. The test only checks that a body's file goes in a folder named for the first two letters of its name. Confirmation now says that nothing checks the database size.

**Things I found but didn't fix**
- **ADR 002 no longer matches the code.** It says one poller thread walks every feed in turn. But `fetch.py`, `doc/design/fetching.md` and `notes/2026-10-fetch-queue.md` describe one queue and worker per host, which shipped in 0.8.0. That needs a new ADR to replace 002, and the comments in `fetch.py` that cite 002 need updating too.
- **Two tests cited as proof don't exist:** `tests/test_single_process.py` in ADR 001 and `tests/test_poller.py` in ADR 002.

I can take on either of those if you'd like.