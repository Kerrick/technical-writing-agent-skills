# Storage

larder keeps one SQLite file per household (ADR 0002). Its default path is `~/.local/share/larder/larder.db`; the `LARDER_DB` environment variable or the `--db` option names another.

## Tables

| Table | Holds |
| - | - |
| `items` | One row per item: `id`, `name`, `kind` (mass, volume, or count), `low_threshold` |
| `events` | One row per purchase or use: `item_id`, `delta` (a signed integer in the item's base unit, ADR 0006), `at` |

Stock is the sum of an item's `delta` values. Nothing stores a running total.

## Sharing a file between devices

larder runs no sync server (ADR 0010). `larder` reads and writes the file where it is, so a household that keeps the file in a folder their cloud storage syncs (Dropbox, iCloud Drive, Syncthing) sees the same pantry on each device. On start, `larder` looks beside the file for the copies those services make when two devices wrote before syncing, and stops with a message naming them (`src/larder/sync.py`).
