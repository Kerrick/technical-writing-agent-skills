---
status: accepted
date: 2026-11-22
deciders: Mira Okafor (maintainer), who decided that devices share the database file through the user's own file-syncing service
informed: Jun Akiyama, who raised the question and wrote the documentation
---

# Devices share one database file through the user's own file-syncing service, and larder runs no sync server

## Context and Problem Statement

larder keeps a household's data in one SQLite file (ADR 0002). In March 2026, three people asked how to use larder on both a laptop and a desktop. larder has no network code and no service behind it. How does the same pantry reach more than one device?

## Decision Drivers

* Users asked to use larder on more than one computer.
* "The file is the whole pantry." (Mira Okafor, 14 March 2026)

No other driver was recorded.

## Considered Options

1. The user puts the database file in a folder that Dropbox or iCloud syncs and points `LARDER_DB` at it

No other option was weighed.

## Decision Outcome

Chosen: option 1, shipped and documented in 0.4. The record gives no reason beyond the drivers above, and it compares the option with nothing else. How the file is found, and how conflict copies are detected, is in [docs/design/storage.md](../design/storage.md).

Confidence: the deciders didn't state any. The evidence today: issue 41 shows the file syncing between two computers, and also shows the failure described below. No recorded comparison says this approach is better than any other.

### Consequences

* Good, because the maintainers run no server, and users need no larder account.
* Bad, because when two devices write before the service syncs, the service keeps both files. Purchases recorded in the copy the user doesn't keep are lost from the pantry. larder doesn't merge the copies. It only tells the user to keep one (issue 41, fixed in 0.4.1).
* Bad, for maintainers, because each syncing service names its conflict copies its own way, outside the project's control. `MARKERS` in `src/larder/sync.py` has to keep up with every service users rely on.
* Neutral, because whether, when, and how safely the file syncs depends on the user's service, not on larder.

### Confirmation

`tests/test_sync.py` fails if `find_conflict_copies` misses a Dropbox conflicted copy beside the database, or flags an unrelated `.db` file. No test covers the iCloud or Syncthing markers, or `refuse_if_conflicted`. No code in this repository calls `refuse_if_conflicted`. Nothing checks that larder stays free of network code.

## More Information

The decision is recorded in `notes/2026-03-sync.md`, along with the 2 April 2026 follow-up on issue 41. ADR 0002 makes the pantry a single file, which is what this decision relies on.

### Later research (2026-11-22)

These were found after the decision and were not weighed. They show what else exists. They are not reasons for the choice, and nothing here says the choice beats them.

* **SQLite session extension.** Per [its documentation](https://www.sqlite.org/sessionintro.html), it records changes to tables in a database, packages them into a "changeset" or "patchset", and applies them to "another database with the same schema and compatible starting data". It is disabled by default and is enabled with `-DSQLITE_ENABLE_SESSION -DSQLITE_ENABLE_PREUPDATE_HOOK` at build time.
* **cr-sqlite.** Per [its README](https://github.com/vlcn-io/cr-sqlite), it is "a run-time loadable extension for SQLite and libSQL" that "allows merging different SQLite databases together that have taken independent writes".
