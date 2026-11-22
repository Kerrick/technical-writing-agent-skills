ADR 003 is now just the decision. The table layout, file naming, retention and cleanup schedule are in a new design doc, which matches the rule in `doc/README.md`: an ADR says why, a design doc says how.

**`doc/adr/003.md`**
- I renamed it from "Storage" to "Article bodies are compressed files on disk, indexed in SQLite", the title the ADR index in `doc/README.md` already used.
- It keeps the context, drivers, options, outcome, consequences and confirmation. I broke the long paragraphs into shorter ones but didn't change what they say.
- The History section mixed two things. The problem that started this (the BLOB backup ran into the morning fetch on 2 April and the reader stalled for 11 minutes) is now in Context, because it explains why the decision was needed. The rest of the history was tuning, so it went to the design doc.
- It now links to the design doc for the details.

**`doc/design/storage.md` (new)**
- Table layout, with the indexes as a list.
- File naming, with a note on why the two-hex-digit subfolders exist.
- Compression: the spike runs from History are now a small table showing why zstd level 9 won.
- Retention.
- Cleanup schedule, as three numbered nightly steps.
- A short note on the 0.3.0 migration from BLOBs.

**Other files**
- `doc/README.md`: added the new design doc under Design.
- `src/quillfeed/store.py`: two docstrings pointed at the ADR's "File naming" and "Retention" sections, which no longer exist. They now point to `doc/design/storage.md`.

**Separate issue, not fixed:** ADR 002 (one poller walking every feed) seems to have been replaced in October. `notes/2026-10-fetch-queue.md` and `doc/design/fetching.md` describe a queue and worker per host instead. But ADR 002 still says "accepted", and `fetch.py` still cites it. It probably needs a new ADR that supersedes 002. Want me to draft that?