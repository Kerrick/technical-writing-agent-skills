I wrote the ADR: `docs/decisions/0010-devices-share-the-database-file-through-the-users-file-syncing-service.md`.

**One thing to check:** I couldn't find anywhere in the code that calls `refuse_if_conflicted` (in `src/larder/sync.py`). `docs/design/storage.md` says larder checks for conflict copies on start, but there's no command or entry-point module in this folder to show it. It may be wired up somewhere this copy of the repo doesn't include. If it isn't, then the 0.4.1 fix for Issue 41 isn't active. The ADR's Confirmation section says no test checks that the check runs on start.

**Why it gets an ADR:** the need is one pantry on several devices. It depends on services outside the project's control (Dropbox, iCloud), and larder hadn't solved it before. Undoing it would mean building a sync layer and a service, which goes against ADR 0002's rule that nothing else has to be installed or run.

**Numbering:** the folder only goes up to 0006, but `docs/research/2026-06-12-barcode-lookup.md` mentions a deleted "former ADR 0009", so this one is 0010. There's no git history here, so I couldn't check whether any other deleted numbers were higher.

**What the record says, all from `notes/2026-03-sync.md`:**
- **Who decided:** Mira Okafor alone. Jun raised the question, wrote the docs and added the conflict check later, but didn't choose how sync works, so Jun isn't listed as a decider.
- **Options:** one. The ADR says no other option was weighed, and points to the note's "Nothing else was discussed for sync."
- **Reason:** the only one recorded is Mira's line "The file is the whole pantry," quoted word for word. I didn't add reasons like "simpler" or "cheaper," and the record doesn't claim this beats anything else.
- **Confidence:** the ADR says none was recorded. It then gives today's evidence: this works when one device writes between syncs, and loses writes when two devices write before syncing (Issue 41).

**What I inferred, and judgment calls:**
- **Bad consequence:** Dropbox, iCloud and Syncthing each name conflict copies their own way. A copy whose name isn't in the list in `src/larder/sync.py` goes unnoticed, and keeping that list current falls on the maintainers.
- **Later research (dated 2026-11-22):** these are alternatives from my own knowledge, not from anything the team discussed: a project-run sync server, cr-sqlite, libSQL replicas on Turso, and larder merging conflict copies itself. I didn't look them up or test them. Delete that section if you'd rather the record stick to the meeting.
- **Left out:** the risk that a syncing service copies the database file while it's half-written. It's plausible, but nothing in the repo shows it happening.
- **No revisit condition:** none was recorded, so I didn't make one up.
- **Front matter:** only `deciders`, to match the existing records, even though Jun was present.

**Other files I changed:**
- `docs/design/storage.md`: the section on sharing a file between devices now cites ADR 0010.
- `src/larder/sync.py`: the docstring at the top now cites ADR 0010 for why and `docs/design/storage.md` for how.
- There's no index file to update; the README just links to the folder.