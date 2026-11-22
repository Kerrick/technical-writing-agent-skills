# Storage

Storage follows ADR 003.

## Articles table

Articles are in the `articles` table:

| Column | Type | Holds |
| - | - | - |
| `id` | INTEGER PRIMARY KEY | |
| `feed_id` | INTEGER NOT NULL | The feed it came from |
| `guid` | TEXT NOT NULL | The feed's own ID for the article; unique per feed |
| `title` | TEXT | |
| `link` | TEXT | |
| `author` | TEXT | |
| `published_at` | INTEGER | Unix seconds, from the feed |
| `fetched_at` | INTEGER NOT NULL | Unix seconds, when Quillfeed first saw it |
| `body_file` | TEXT | The body's file name, or NULL once the body is no longer kept |
| `body_bytes` | INTEGER | The body's size before compression |

There is a unique index on (`feed_id`, `guid`) and an index on `fetched_at`. Search uses an FTS5 table, `articles_fts`, over `title` and the body's text, filled when the article is stored.

## Body files

A body's file name is the SHA-256 of the uncompressed body, in hex, with `.zst` appended. Files live under `bodies/` in the data folder, in a subfolder named for the first two hex digits, so no folder holds more than a few thousand files: `bodies/3f/3f9a…c1.zst`. Two articles with the same body share one file.

Files are written to a temporary name in the same folder and renamed, so a reader never sees half a file. Compression is zstd level 9.

## Retention

Bodies are kept for 90 days from `fetched_at` by default. The host can change that with `retention_days` in the configuration file; 0 keeps them forever. Starred articles are kept regardless.

The fields in `articles` are never deleted, so search by title still finds an article whose body is gone. The reader shows such an article as "body no longer kept".

## Nightly cleanup

Every night at 03:00 local time, Quillfeed:

1. Deletes the files of bodies past retention and sets their `body_file` to NULL.
2. Deletes any file in `bodies/` that no row names and that is more than a day old. This removes files left behind by a crash between writing a file and its row.
3. Runs `VACUUM`, on the first night of each month only.
