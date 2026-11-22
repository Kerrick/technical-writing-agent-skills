---
status: accepted
date: 2026-03-14
deciders: Mira Okafor (maintainer)
consulted: Jun Akiyama
---

# Devices share a pantry by keeping the one database file in the user's own file-syncing service

## Context and Problem Statement

A household's whole pantry is one SQLite file on one computer (ADR 0002). In March 2026, three users asked how to use larder on both a laptop and a desktop. How does a household see the same pantry on more than one device?

## Decision Drivers

* A household using larder on several devices must see one pantry.
* The answer had to ship in 0.4.

No other driver was recorded.

## Considered Options

1. The user keeps `larder.db` in a folder that their own file-syncing service syncs (Dropbox, iCloud Drive), and points `LARDER_DB` at it
2. A sync server run by larder's maintainers
3. larder merges copies that have diverged

Only option 1 was considered when the decision was made. Options 2 and 3 come from later research ([docs/research/2026-11-22-device-sync-options.md](../research/2026-11-22-device-sync-options.md)), and were not weighed against it.

## Decision Outcome

Chosen: option 1. The only reason recorded is that the file is the whole pantry, so syncing the file syncs everything. No reason was recorded for preferring it to a sync server or to merging, because neither was discussed. This record does not claim that option 1 is better than either. How larder finds the file and checks it on start is in [docs/design/storage.md](../design/storage.md).

Confidence: high that a pantry kept in a synced folder shows up on every device; users have done this since 0.4. Low that this is the best option, since no comparison was made.

### Consequences

* Good, because larder needs no sync code of its own, and the maintainers run no service and hold no user data.
* Good, because installing larder still means installing nothing else, for anyone who already uses such a service.
* Bad, because these services can't merge two edited copies of the file. When two devices write before syncing, the service keeps both, and one device's changes are missing until the user notices (issue 41). Since 0.4.1, larder stops on start when it finds a conflict copy beside the file and tells the user to keep one. It doesn't merge them, so the changes in the copy the user deletes are lost.
* Bad, because each service names its conflict copies differently. larder recognises three naming patterns, and a service that uses another goes undetected.
* Bad, because a service may upload the file while SQLite is still writing it. Nobody knows whether this has damaged a user's file.
* Bad, for maintenance, because sync problems show up in services the maintainers neither run nor watch.

### Confirmation

`tests/test_sync.py` checks that a Dropbox conflict copy is found and that other `.db` files are ignored. No test covers the iCloud or Syncthing names, or checks that larder runs this check on start.

## More Information

Revisit this decision if conflict copies keep losing users' changes, or if larder ever needs to sync more than one file. The trade-offs of options 2 and 3 are in the research note above. Decided at the sync meeting of 14 March 2026 (notes/2026-03-sync.md). The conflict check followed on 2 April 2026.
