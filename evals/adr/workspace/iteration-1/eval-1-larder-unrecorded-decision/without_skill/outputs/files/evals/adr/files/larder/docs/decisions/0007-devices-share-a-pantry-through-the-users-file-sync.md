---
status: accepted
date: 2026-03-14
deciders: Mira Okafor (maintainer)
---

# Devices share a pantry by keeping the SQLite file in a folder the user's cloud storage syncs

## Context and Problem Statement

In March 2026 three users asked how to use larder on both a laptop and a desktop. All of a household's data is one SQLite file on the user's computer (ADR 0002), so a second device has no way to see the first device's purchases. How should two devices share a pantry?

This record was written in November 2026, after the decision. It draws on the meeting notes in `notes/2026-03-sync.md`, the 2 April follow-up in those notes, and the code that shipped.

## Decision Drivers

The notes do not say why this option was chosen. The drivers below are the ones ADR 0002 already set for storage. They are listed because this option follows from them, not because they were discussed at the time.

* Installing larder must not mean installing or running anything else.
* A user can back up, move, or delete their data with the tools they already have.

## Considered Options

1. The user keeps `larder.db` in a folder that Dropbox, iCloud Drive, or a similar service syncs, and points `LARDER_DB` at it.

No other option was considered. The notes say: "Nothing else was discussed for sync." A sync server run by the maintainers, or a merge built into larder, were not evaluated, so this record gives no reasons against them.

## Decision Outcome

Chosen: option 1. It needs no new code: larder already reads and writes the file at whatever path `LARDER_DB` or `--db` names (see [docs/design/storage.md](../design/storage.md)). It shipped and was documented in 0.4.

Confidence: medium. It works when one device writes at a time. Issue 41 showed that it loses data from the user's view when two devices write before the service syncs: Dropbox kept both files, and one device's purchases were missing until the user noticed the "conflicted copy". No other option was compared, so there is no evidence on whether another would be better.

### Consequences

* Good, because larder runs no server, holds no accounts, and never sees a user's data.
* Good, because the user chooses the service, and a file that syncs is still one file to back up (ADR 0002).
* Bad, because two devices that write before syncing produce two files. larder does not merge them. Since 0.4.1 it stops on start-up and tells the user to keep one and delete the others, so the purchases in the other copy are lost unless the user enters them again.
* Bad, because larder depends on how each service names conflict copies. `src/larder/sync.py` recognises three patterns (`conflicted copy`, `sync-conflict`, ` 2.db`); a service that names them another way, or does not keep a copy at all, is not detected.
* Bad, because the maintainers cannot see or test the sync itself; it happens in software larder does not control.

### Confirmation

On start, `refuse_if_conflicted` in `src/larder/sync.py` stops larder if a conflict copy sits beside the database file. `tests/test_sync.py` checks that a Dropbox conflict copy is found and that other `.db` files in the folder are ignored. No test covers the `sync-conflict` or ` 2.db` patterns, or the start-up refusal itself.

## More Information

* `notes/2026-03-sync.md`: the 14 March 2026 meeting (Mira, Jun) and the 2 April 2026 follow-up on issue 41.
* ADR 0002: all of a household's data is one SQLite file.
* If two-device writes become common, a merge of conflict copies or a sync service would be a new decision, and this record would be superseded rather than edited.
