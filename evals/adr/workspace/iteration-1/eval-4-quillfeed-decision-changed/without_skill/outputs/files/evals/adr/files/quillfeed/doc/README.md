# Contributor documentation

## Decisions

One architecturally significant decision per record, in [adr/](adr/). Code cites a decision by number for why, and a design document by path for how.

| ADR | Decision |
| - | - |
| [001](adr/001.md) | Quillfeed is one process with an embedded SQLite database |
| [002](adr/002.md) | ~~One poller fetches every feed on a fixed schedule~~ (superseded by 004) |
| [003](adr/003.md) | Article bodies are compressed files on disk, indexed in SQLite |
| [004](adr/004.md) | Each host has its own fetch queue, with requests to it spaced 10 seconds apart |

## Design

- [design/fetching.md](design/fetching.md): how feeds are fetched.
