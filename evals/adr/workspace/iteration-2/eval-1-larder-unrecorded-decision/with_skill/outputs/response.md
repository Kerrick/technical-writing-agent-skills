I wrote the ADR: `docs/decisions/0010-devices-share-the-database-file-through-the-users-own-file-sync.md`. As you thought, the notes show nobody looked at anything else, so it lists one option and says plainly that no other was weighed.

**Why it's an ADR and not a design-doc entry:** it depends on things outside the project's control (Dropbox, iCloud and how they name conflict copies) and it shapes the system, since larder has no network code. Undoing it would mean building and running a sync server and merge logic, and moving users off files they already keep in Dropbox.

**Why it's number 0010:** the files only go up to 0006, but `docs/research/2026-06-12-barcode-lookup.md` mentions a "former ADR 0009". This folder isn't a git repo, so I couldn't check the history for higher numbers.

**What it says, and where each part comes from:**
- **Deciders:** Mira alone. Jun is listed under "informed" because Jun raised the question and wrote the docs.
- **Drivers:** the three users asking about using larder on two computers, and Mira's words "The file is the whole pantry", quoted exactly from the notes. The record gives no other reason, and the ADR says so. I didn't carry over ADR 0002's drivers; it is cited as context instead.
- **Confidence:** the notes give none, and the ADR says so. Issue 41 shows the file syncing between devices, and also shows the failure. The ADR makes no claim that this approach is better than anything else.
- **Bad consequences:** if two devices write before syncing, purchases in the copy the user doesn't keep are lost, because larder doesn't merge (issue 41). Maintainers also have to keep the list of conflict-copy name patterns (`MARKERS`) in `src/larder/sync.py` up to date with each service.
- **Later research (dated today):** the SQLite session extension and cr-sqlite. Both are clearly marked as found afterwards and not weighed. The fetch tool only gave me summaries and quotes of their pages; downloading the full pages needed shell approval I didn't have. So each claim is limited to an exact quote, which I checked.

**Other changes:** I added an "ADR 0010" citation to `docs/design/storage.md` and to the opening comment of `src/larder/sync.py`. The log has no index file; the README just links to the folder.

**Gaps I found while checking the facts the ADR cites:**
- No code in this repo calls `refuse_if_conflicted`. `storage.md` says larder stops on start when it finds conflict copies, but I couldn't confirm that here.
- `tests/test_sync.py` only tests Dropbox's naming. Nothing tests the iCloud (`" 2.db"`) or Syncthing (`"sync-conflict"`) patterns.
- The ADR states both gaps in its Confirmation section. Fixing them is code work I didn't do.

**Decisions you might want to change:**
- **`date`:** I used today, following the skill's template rule that it's the day the record was last updated. The older records look like they use the decision date; if you want that convention, it would be 2026-03-14.
- **No condition for revisiting:** none was recorded, so I didn't make one up.
- **Mid-sync risk left out:** a SQLite file in a syncing folder could get synced partway through a write. Nothing in the record or the issues mentions it, so I didn't include it.