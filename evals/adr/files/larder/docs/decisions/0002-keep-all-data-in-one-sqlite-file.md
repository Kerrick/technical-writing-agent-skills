---
status: accepted
date: 2025-11-03
deciders: Mira Okafor (maintainer)
---

# All of a household's data is one SQLite file on the user's computer

## Context and Problem Statement

larder records purchases and use for one household, a few thousand rows a year. It runs as a command, with no service behind it. Where does the data live?

## Decision Drivers

* Installing larder must not mean installing or running anything else.
* A user can back up, move, or delete their data with the tools they already have.

## Considered Options

1. One SQLite file per household, at a path the user can change
2. A folder of JSON files, one per item
3. A PostgreSQL database the user runs

## Decision Outcome

Chosen: option 1, because SQLite ships with Python, so nothing else is installed, and one file is the simplest thing to back up or move. Option 2 lost because `larder low` reads every item, and a spike with 4,000 item files took 1.9 seconds to answer it. Option 3 lost because it fails the first driver. The schema and the file's location are in [docs/design/storage.md](../design/storage.md).

Confidence: high that it works; the test suite runs every command against a real file. Medium that it is better than option 2 for small households, where the spike's slowness would not show.

### Consequences

* Good, because a backup is a copy of one file.
* Bad, because two processes writing at once must wait for SQLite's lock, so a long import blocks `larder add`.
* Bad, because a schema change needs a migration that runs on each user's computer, which the maintainers cannot watch.

### Confirmation

`tests/test_storage.py` opens a fresh file for every test and fails if any command leaves a second file beside it.
