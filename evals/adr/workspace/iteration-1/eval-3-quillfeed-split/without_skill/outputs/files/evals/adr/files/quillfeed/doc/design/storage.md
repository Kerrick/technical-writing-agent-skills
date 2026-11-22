# Storage

Storage follows ADR 003: article fields are rows in SQLite, and bodies are compressed files on disk.

## Table layout

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

Indexes:

- A unique index on (`feed_id`, `guid`).
- An index on `fetched_at`.

Search uses an FTS5 table, `articles_fts`, over `title` and the body's text. It is filled when the article is stored.

## File naming

A body's file name is the SHA-256 of the uncompressed body, in hex, with `.zst` appended. Two articles with the same body share one file.

Files live under `bodies/` in the data folder, in a subfolder named for the first two hex digits:

```
bodies/3f/3f9a…c1.zst
```

The subfolders keep any one folder to a few thousand files. They were added on 15 April, after `ls bodies/` hung a terminal.

A file is written to a temporary name in the same folder and then renamed, so a reader never sees half a file.

## Compression

Bodies are compressed with zstd at level 9. These are the spike runs that chose it, on the maintainer's 2,400 feeds:

| Run | Compression | Bodies folder | Cost |
| - | - | - | - |
| 2026-04-09-a | none | 38 GB | |
| 2026-04-11-b | zstd level 3 | 14 GB | |
| 2026-04-12-c | zstd level 9 | 11 GB | storing an article 4 ms slower |
| 2026-04-12-d | zstd level 19 | | storing took 60 ms an article, and the walk fell behind |

## Retention

Bodies are kept for 90 days from `fetched_at` by default. The host can change that with `retention_days` in the configuration file; 0 keeps them forever.

Starred articles are kept regardless.

The fields in `articles` are never deleted, so search by title still finds an article whose body is gone.

## Cleanup schedule

Every night at 03:00 local time, Quillfeed:

1. Deletes the files of bodies past retention and sets their `body_file` to NULL.
2. Deletes any file in `bodies/` that no row names and that is more than a day old. This removes what a crash left behind.
3. Runs `VACUUM`, on the first night of each month only.

## Migration from BLOBs

Release 0.3.0 moved existing bodies out of the database. Its code was removed in 0.5.0.
