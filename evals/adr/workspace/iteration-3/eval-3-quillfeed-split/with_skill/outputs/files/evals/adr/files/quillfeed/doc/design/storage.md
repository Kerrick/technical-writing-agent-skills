# Storage

Storage follows ADR 003. An article's fields are a row in SQLite, and its body is a compressed file on disk.

## The articles table

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

There is a unique index on (`feed_id`, `guid`) and an index on `fetched_at`.

Search uses an FTS5 table, `articles_fts`, over `title` and the body's text. It is filled when the article is stored.

## Body files

- **Name:** the SHA-256 of the uncompressed body, in hex, with `.zst` appended.
- **Folder:** `bodies/` in the data folder, in a subfolder named for the first two hex digits, so no folder holds more than a few thousand files: `bodies/3f/3f9a…c1.zst`.
- **Shared bodies:** two articles with the same body share one file.
- **Writing:** a file is written to a temporary name in the same folder, then renamed, so a reader never sees half a file.
- **Compression:** zstd, level 9.

## Retention

Bodies are kept for 90 days from `fetched_at`. The host changes that with `retention_days` in the configuration file, and 0 keeps them forever. Starred articles are always kept.

The row in `articles` is never deleted, so search by title still finds an article whose body is gone. The reader shows such an article as "body no longer kept".

## Nightly cleanup

Every night at 03:00 local time, Quillfeed:

1. deletes the file of each body past retention, and sets its `body_file` to NULL;
2. deletes each file in `bodies/` that no row names and that is more than a day old, which removes what a crash left behind;
3. runs `VACUUM`, on the first night of each month only.
