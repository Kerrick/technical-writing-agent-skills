I wrote the ADR: `docs/decisions/0010-devices-share-a-pantry-through-the-users-file-sync-service.md`. It follows the form of ADRs 0002 and 0006.

**What it records, all from `notes/2026-03-sync.md`:**
- **Decider:** Mira Okafor alone. Jun raised the problem, wrote the docs and added the conflict check, but didn't choose how sync works, so I didn't list Jun as a decider or as consulted.
- **Driver:** people asked how to use larder on a laptop and a desktop. The record says no other driver was recorded. I didn't carry over ADR 0002's "nothing else to install" driver, because the notes never give it as a reason here.
- **Options:** only the one chosen, with a line saying no other was weighed. That matches "Nothing else was discussed for sync."
- **Reason:** "The file is the whole pantry." The record says plainly that nothing was ever compared with this approach, so it doesn't claim the approach is better.
- **Downsides:** larder doesn't merge conflict copies, so one device's changes are lost (from issue 41). The conflict check also depends on how Dropbox, iCloud and Syncthing name their copies, which the project doesn't control.
- **Confidence:** none was recorded. The record says what `tests/test_sync.py` actually covers: it finds a Dropbox conflict copy and ignores other databases.
- **Gaps:** nothing tests the iCloud (`" 2.db"`) or Syncthing (`"sync-conflict"`) names. I also found no code in `src/` that calls `refuse_if_conflicted` when larder starts, so the record says nothing checks that it runs. `docs/design/storage.md` says it runs on start; you may want to check whether that call exists somewhere I didn't see.

**Judgment calls you may want to overturn:**
- **It earns an ADR.** Undoing it would mean building a sync layer and moving files that users already keep in their sync folders. It also relies on services outside your control.
- **Number 0010, not 0007.** `docs/research/2026-06-12-barcode-lookup.md` mentions a deleted "former ADR 0009". This folder isn't a git repo, so I couldn't check the history for anything higher.
- **The `date` is today (2026-11-22),** following the template's rule that it's the day the record was last updated. The March decision date and the 0.4 / 0.4.1 releases are under More Information.
- **No condition for revisiting it,** because none was recorded.

**Later research (dated 2026-11-22):** three alternatives, marked as found after the decision and never its reason: a sync server you run, SQLite's session extension, and cr-sqlite. The download of the full pages needed approval I didn't have, so I relied on summaries of the official pages. I kept those entries to plain paraphrased facts with no quotes; it's worth a quick look against the linked pages. I left out SQLite's warning about network filesystems. It's about network drives, not sync folders like Dropbox, so citing it would have stretched it.

**Other edits:** I added an ADR 0010 citation to the "Sharing a file between devices" section of `docs/design/storage.md` and to the docstring of `src/larder/sync.py`. There's no index file to update; the README links to the folder.