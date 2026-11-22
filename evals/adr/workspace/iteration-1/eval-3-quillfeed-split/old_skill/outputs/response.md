I split it. `doc/adr/003.md` now records only the decision to store article bodies as compressed files, and the design detail moved to a new `doc/design/storage.md`. That design detail is the table layout, file naming, retention and cleanup schedule. None of those is costly to undo, so they don't need an ADR.

**ADR 003**
- **Title:** it was just "Storage". It now names the problem and the choice, the same wording the ADR index in `doc/README.md` already used.
- **Kept:** the context, drivers, options, outcome, confidence and consequences say the same as before. I only split some long sentences.
- **Added:** a short "More Information" section with the evidence from the old History section, and a link to the design doc.

**Where each old section went**

| Old section in ADR 003 | Now |
| - | - |
| Context through Consequences | Still in ADR 003 |
| Confirmation | Still in ADR 003, corrected (see below) |
| Table layout | `storage.md`, "The articles table" |
| File naming | `storage.md`, "Body files" |
| Retention | `storage.md`, "Retention" |
| Cleanup schedule | `storage.md`, "Nightly cleanup" |
| History: BLOB backup problem, sizes at each compression level | ADR 003, "More Information" |
| History: level 19 was too slow | `storage.md`, "Body files", as the reason for level 9 |
| History: `ls bodies/` hanging, spike run IDs, the 0.3.0 and 0.5.0 migration notes | Dropped. Git history still has them, and the reason for the subfolders is stated in `storage.md`. |

**Citations updated:** the two docstrings in `src/quillfeed/store.py` that pointed at the old ADR sections now point at `doc/design/storage.md`. I also added the new doc to the index in `doc/README.md`.

**Things you should know**
- **ADR 003's Confirmation was wrong.** It said `tests/test_store.py` fails if the database grows by more than 2 KB, but that test only checks where a body's file goes. I changed the section to say no test checks the decision yet, and to describe the test that would.
- **ADR 002 is out of date.** It says one poller walks every feed in turn. The code (`src/quillfeed/fetch.py`) and `notes/2026-10-fetch-queue.md` describe one queue and worker per host, decided on 19 October and shipped in 0.8.0. That needs a new ADR (004) to replace 002. `fetch.py` also cites ADR 002 for the 10-second spacing, which 002 doesn't mention. I left all of this alone because it's outside what you asked; I can write ADR 004 next if you want.
- **Two tests named in other ADRs don't exist.** ADR 001 and 002 name `tests/test_single_process.py` and `tests/test_poller.py` in their Confirmation sections, and neither file is in the repo.