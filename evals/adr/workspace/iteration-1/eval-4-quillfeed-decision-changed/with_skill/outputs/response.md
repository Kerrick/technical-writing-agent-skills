I replaced ADR 002 with a new ADR 004 and deleted 002. The skill says an accepted ADR's decision text is never edited or marked "superseded". When the code changes it, a new record restates the whole decision and the old one goes (git keeps it).

**What changed**
- **Added `doc/adr/004.md`:** "Each host's feeds are fetched by a worker of its own, with its requests spaced apart". It's dated 2026-10-19 and marked accepted, since it shipped in 0.8.0. Everything in it comes from `notes/2026-10-fetch-queue.md`, the code, and the March record.
- **Deleted `doc/adr/002.md`.**
- **Updated the citations:** the index in `doc/README.md`, `doc/design/fetching.md` ("follows ADR 004"), and both comments in `src/quillfeed/fetch.py`. The module docstring there also wrongly said "One poller walks every feed". Nothing else cites 002. The October note never names 002, so it stays as written.

**Judgment calls you may want to overturn**
- **Number 004:** this folder isn't a git repo, so I couldn't check for deleted records. I took the next number after the files present and found no "former ADR" mentions in the docs.
- **Deciders:** Dana alone, because the note says "Decided, 19 October (Dana)". Tomás appears as someone who weighed the options and measured option 2, not as a decider.
- **Carried over the March option** ("a timer per feed") and its reason for losing, marked as weighed in March 2026. I also kept the context's ADR 001 framing. The March consequences about one slow host and same-host bursts no longer hold, so I didn't carry them over. "One place to look" is now a bad consequence.
- **Confidence:** the deciders never stated one, so the record says that and then gives today's evidence.

**Things the code or notes don't back up**
1. **The 15-minute promise can't hold for big hosts.** At one request per 10 seconds, a host can serve at most 90 feeds in 15 minutes. The three hosts that blocked you each serve over 150, so each of their feeds is fetched about every 25 minutes. The note says option 1 "keeps both the 15-minute promise and the hosts' limits". I recorded that as Dana's reason, and listed the 90-feed limit as a bad consequence and an unproven point. You may want to decide whether that's acceptable.
2. **`fetch.py` doesn't match `doc/design/fetching.md`.** `DUE_AFTER_SECONDS` is defined but never used, so a host with one feed is fetched every 10 seconds. Every host also gets a thread forever, though the design says idle hosts have none. I didn't touch either.
3. **I couldn't find `quillfeed fetch-status` in the repo.** The note says it was added, so I kept the sentence that mentions it.
4. **Some cited tests don't exist:** `tests/test_poller.py` (cited by the old 002) and `tests/test_single_process.py` (cited by ADR 001). That makes ADR 001's Confirmation section wrong.
5. **ADR 003 fails the log's own rules.** Its title is a topic ("Storage"), and it contains a schema table, naming rules, retention, a schedule, and history. Those belong in a design document. Want me to split it?