---
status: accepted
date: 2026-11-22
deciders: Mira Okafor (maintainer)
---

# Devices share a pantry by keeping its one file in a folder the user's file-sync service syncs

## Context and Problem Statement

People use larder on more than one computer, such as a laptop and a desktop, and want the same pantry on each. All of a household's data is one SQLite file on the user's computer (ADR 0002), at a path the user can change. larder has no service behind it. How do two devices see the same pantry?

## Decision Drivers

* People asked how to use larder on a laptop and a desktop.

No other driver was recorded.

## Considered Options

1. Keep the file in a folder synced by a service the user already has, such as Dropbox or iCloud Drive, and point `LARDER_DB` at it.

No other option was weighed.

## Decision Outcome

Chosen: option 1, because the file is the whole pantry. No reason was recorded for preferring it over any other way to sync, and none was compared with it. How larder reads the shared file and checks for conflict copies is in [docs/design/storage.md](../design/storage.md).

Confidence: the deciders didn't record any. Today, `tests/test_sync.py` shows that larder finds a Dropbox conflict copy beside the file and ignores other databases. No recorded comparison shows this approach is better than another. Nothing tests the file names iCloud Drive or Syncthing give their conflict copies, or that two devices writing at different times end up with the same pantry.

### Consequences

* Good, because the maintainers run no server and hold no user data.
* Bad, because when two devices write before the service syncs, the service keeps two files. larder does not merge them. It stops and tells the user to keep one, so the changes in the other are lost unless the user copies them across by hand.
* Bad, because the check for conflict copies depends on how each sync service names them, which the maintainers don't control. When a service changes its naming, larder stops noticing conflicts until `src/larder/sync.py` is updated.

### Confirmation

`tests/test_sync.py` fails if larder stops finding a Dropbox conflict copy, or starts treating another database in the folder as one. Nothing automated checks the other services' names, or that larder runs the check when it starts.

## More Information

The decision was made at a meeting on 14 March 2026, recorded in `notes/2026-03-sync.md`, and shipped in 0.4. The conflict-copy check was added in 0.4.1 after issue 41.

### Later research (2026-11-22)

These alternatives were found after the decision. They inform a reader; they were never its reason, and nothing here shows that option 1 is better or worse than them.

* **A sync server that larder runs.** Each device would send its changes to a service the project operates. This would bring back what ADR 0002 avoids: something running besides larder.
* **SQLite's session extension.** It records the changes made to a database as a changeset and applies them to another copy with the same schema. Conflicting changes go to a handler that can skip them or abort. It is off unless SQLite is built with it. ([sqlite.org/sessionintro.html](https://www.sqlite.org/sessionintro.html))
* **cr-sqlite.** A loadable SQLite extension that merges databases written to independently, using conflict-free replicated data types. It must be loaded on every connection. ([github.com/vlcn-io/cr-sqlite](https://github.com/vlcn-io/cr-sqlite))
