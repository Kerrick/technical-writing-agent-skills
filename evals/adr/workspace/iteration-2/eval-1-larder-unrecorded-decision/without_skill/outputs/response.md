I wrote the ADR: `evals/adr/files/larder/docs/decisions/0007-devices-share-a-pantry-through-the-users-file-sync.md`. It follows the format of 0002 and 0006. I also added a line in `docs/design/storage.md` that points the "Sharing a file between devices" section to it.

**The missing reasoning.** The notes give no reasons for Mira's choice and say "Nothing else was discussed for sync," so I didn't make any up:
- **Considered Options** lists only the chosen option. It says plainly that nobody evaluated a sync server or a merge, and gives no reasons against them.
- **Decision Drivers** uses the two drivers from ADR 0002 (nothing else to install, and users manage the data with their own tools). The ADR says these are borrowed from 0002 because this choice follows from them, not because anyone discussed them in March.
- **Confidence is medium**, because of issue 41 and because nothing was compared.
- A short note says the record was written in November 2026, after the decision.

**The rest:**
- **Consequences** covers issue 41. larder never merges conflict copies, and since 0.4.1 it refuses to start until you delete the extra ones, so whatever is in the deleted copy is lost unless someone enters it again. It also notes that larder only spots conflict copies whose names match one of three patterns.
- **Confirmation** points to `refuse_if_conflicted` and `tests/test_sync.py`. The tests only check that a Dropbox-style conflict copy is found. Nothing tests the `sync-conflict` or ` 2.db` name patterns, or the start-up refusal itself.

**Things to check:**
- **Number:** I used 0007 because the folder only has 0002 and 0006. If 0001 and 0003–0005 live somewhere else, make sure 0007 isn't already taken.
- **Decider and date:** I listed only Mira, dated 14 March 2026. Jun was at the meeting but the notes don't show them taking part in the decision. Add Jun if that's wrong.
- **A risk not in the ADR:** Sync services can damage a SQLite file by copying it mid-write. This is general knowledge, not anything recorded in the project, so I left it out. It may be worth looking into before someone revisits this decision.