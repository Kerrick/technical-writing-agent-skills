---
status: accepted
date: 2026-11-22
deciders: Mira Okafor (maintainer)
---

# Devices share a pantry by keeping its one database file in a folder the user's file-syncing service syncs, not through a larder server

## Context and Problem Statement

A household's data is one SQLite file on the user's computer (ADR 0002), and larder runs as a command with no service behind it. In March 2026 three people asked how to use larder on both a laptop and a desktop. How does one pantry reach more than one device?

## Decision Drivers

* A household must see the same pantry on each of its devices.
* Installing larder must not mean installing or running anything else (ADR 0002).

## Considered Options

1. Keep the database file in a folder a file-syncing service such as Dropbox or iCloud Drive syncs, and point `LARDER_DB` at it

No other option was weighed. The meeting that decided it, on 14 March 2026, records that nothing else was discussed.

## Decision Outcome

Chosen: option 1. The only reason recorded is Mira's: "The file is the whole pantry." It shipped in 0.4. How larder finds the file and checks for conflict copies is in [docs/design/storage.md](../design/storage.md).

Confidence: the deciders didn't record any. Today's evidence shows that the approach works when only one device writes between syncs, and that it loses writes when two devices write before syncing. In Issue 41 a user ran `larder add` on two computers within a minute, and Dropbox kept both files. The second computer's purchases were missing until the user noticed. Nothing compares this option with any other.

### Consequences

* Good, because larder needs no server, accounts, or network code, and the project runs nothing.
* Bad, because two devices that write before syncing leave two files. larder does not merge them, so the user keeps one and loses what was written to the other.
* Bad, because each syncing service names its conflict copies its own way, outside the project's control. The maintainers keep the list of names in `src/larder/sync.py`, and a copy whose name matches none of them goes unnoticed.
* Neutral, because larder works with any service that syncs a folder, and not only the two the decision named.

### Confirmation

`tests/test_sync.py` fails if `find_conflict_copies` stops finding a Dropbox conflict copy beside the database, or starts flagging an unrelated `.db` file. No test covers the other conflict-copy names or checks that larder runs the check on start. Nothing checks that larder stays without a server.

## More Information

The meeting note and the Issue 41 follow-up are in `notes/2026-03-sync.md`.

### Later research (2026-11-22)

These alternatives were found after the decision. They were never its reason, and nobody has compared them with option 1.

* A sync server run by the project, which larder would push events to and pull them from. This runs against ADR 0002's driver that nothing else is installed or run.
* A CRDT extension for SQLite, such as cr-sqlite, which records changes so that two copies of a database can be merged.
* A hosted SQLite service with local replicas, such as libSQL embedded replicas on Turso, which keeps a copy on each device in step with a primary database.
* larder merging the conflict copies itself. Stock is the sum of an item's `events` rows (docs/design/storage.md), so two copies differ mainly in the rows that each one added.
