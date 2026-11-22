I've written the ADR and a separate research note for the alternatives:

- `docs/decisions/0010-devices-share-the-database-file-through-the-users-own-sync-service.md`
- `docs/research/2026-11-22-device-sync-options.md`

**What the ADR says**

- **No comparison was made.** The only reason Mira gave on 14 March was that "the file is the whole pantry," so syncing the file syncs everything. The ADR says plainly that only this option was discussed. It doesn't claim the choice beats any alternative.
- **The alternatives come from research done today, not from March.** The ADR lists two other options: a sync server we run, and larder merging copies that have diverged. The ADR and the research note both say these were never weighed when the decision was made. Merging is a real possibility because the `events` table only ever gets new rows added. I didn't run any spikes, and the note says so.
- **Confidence is split in two.** It's high that a file in a synced folder works, since people have done it since 0.4. It's low that this is the best choice.
- **The costs are listed.** The main one is issue 41: when two devices write before syncing, the service keeps two copies. Since 0.4.1, larder refuses to start and asks the user to keep one, and the changes in the deleted copy are lost. The ADR also notes that larder only recognises three conflict-copy names, and that a service could upload the file mid-write.

**Things to check**

1. **The number.** There's no git repo here, so I couldn't search the history for the highest ADR number ever used. The highest I found is the deleted 0009, so I used 0010. Please run the `git log` check in your real repo before merging.
2. **Whether the conflict check actually runs.** `docs/design/storage.md` says larder runs `refuse_if_conflicted` on start, but nothing in this copy of the code calls it. `tests/test_sync.py` only tests that a Dropbox conflict copy is found. Nothing covers the iCloud or Syncthing names, or that the check runs on start. The ADR says that gap is open. It's worth confirming the call exists and adding a test.
3. **Status and date.** I set it to `accepted` with the date it was decided (2026-03-14). Mira is listed as decider and Jun as consulted. Mira should read it before it's merged, since it puts her decision on record.