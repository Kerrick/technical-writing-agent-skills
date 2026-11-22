# Ways to share one pantry between devices (2026-11-22)

Written for ADR 0010, eight months after the decision it records. On 14 March 2026 only one option was discussed (notes/2026-03-sync.md), so nothing here was a reason for that decision. This note comes from reading larder's code and docs and from what is generally known about these approaches. No spike was run and no option was measured.

## 1. The user's own file-syncing service carries the SQLite file (shipped in 0.4)

The user puts `larder.db` in a folder that Dropbox, iCloud Drive, or Syncthing syncs, and points `LARDER_DB` at it.

* Good, because larder needs no new code to sync, and the maintainers run nothing.
* Good, because it keeps ADR 0002's "nothing else to install" for anyone who already uses such a service.
* Bad, because these services sync whole files and cannot merge two edited copies of a SQLite file. When two devices write before syncing, the service keeps both (issue 41), and one device's changes stay out of the pantry until the user picks a file.
* Bad, because a service may upload the file while SQLite is writing it, or while a journal file sits beside it. SQLite's own documentation advises against keeping a database where other software copies or locks it without SQLite knowing. Whether this has damaged a larder file is not known.
* Bad, because each service names its conflict copies differently, so larder's check has to know every naming scheme.

## 2. A sync server run by larder's maintainers

Each device keeps its own file and sends its changes to a hosted service, which sends them on to the household's other devices.

* Good, because the server sees every change, so it can order and merge them and no copy diverges unnoticed.
* Bad, because the maintainers would host, secure, and pay for a service holding users' data, and would need accounts or keys to tell households apart.
* Bad, because larder would need a network client and a protocol, and it would stop being only a command with a file behind it.

## 3. larder merges divergent copies itself

`events` is append-only: each purchase or use is one row, and stock is the sum of an item's rows (docs/design/storage.md). So two copies that have diverged could be merged by taking the union of their events, if each event had an id that is unique across devices. The file could still travel by option 1's services, or by any other means.

* Good, because a conflict copy could be merged without losing anything, where now the user picks one file and the other's changes are lost.
* Bad, because events would need globally unique ids, which is a schema change and a migration on every user's computer (see ADR 0002's consequences).
* Bad, because `items` is not append-only: two devices that rename an item or change its threshold would still conflict, and some rule would have to pick a winner.
