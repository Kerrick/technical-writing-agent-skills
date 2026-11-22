I've rewritten the decision log. The old poller decision is now ADR 004, and ADR 002 is deleted, following the skill's rule that an accepted ADR isn't rewritten in place.

**Changes**
- **New `doc/adr/004.md`:** "Each host has its own fetch queue and worker, spaced 10 seconds apart." It covers the whole decision again: the 6 October 429 blocks, three drivers (the 15-minute promise, staying within host limits, fitting in one process) and the three options from your October note with Tomás's numbers. Dana is listed as decider and Tomás as consulted. It also lists the known costs: 340 threads at peak, no single loop to debug, and `fetch-status` to list each host's queue. Confirmation points to `tests/test_fetch_spacing.py`; the old ADR named `tests/test_poller.py`, which doesn't exist.
- **Deleted `doc/adr/002.md`.** ADR 004 says it replaces "the former ADR 002". The repo isn't under git here, so I couldn't check for deleted numbers above 003. 004 is correct only if none existed.
- **Citations:**
  - `doc/README.md`: the index now lists 004 instead of 002.
  - `doc/design/fetching.md`: now says it follows ADR 004.
  - `src/quillfeed/fetch.py`: both references to ADR 002 now say ADR 004. I also rewrote the module docstring, which still said "one poller walks every feed in turn".

**Confidence in the 15-minute promise is set to low, and you may want to check this.** The note says the per-host queue keeps the 15-minute promise. But one worker per host at 10-second spacing gets through only 90 feeds in 15 minutes. Each of the three hosts that blocked you serves more than 150 feeds, which works out to about 25 minutes or more per cycle. There's also no recorded walk time or 429 rate since 0.8.0. The recorded reason for the choice stands as written.

**Code that doesn't match the design doc (I didn't change any of it):**
- `fetch.py` defines `DUE_AFTER_SECONDS` but never uses it. Each worker cycles through its feeds non-stop instead of waiting until a feed is due again.
- `start()` starts a thread for every host. `fetching.md` says hosts with nothing due have no worker running.
- I didn't see the five-failures backoff or the conditional-request logic in this file.

**Not touched:** ADR 003 is titled just "Storage" and carries detailed design: the table layout, file naming, retention, cleanup and history. The skill says that material belongs in a design document such as `doc/design/storage.md`. I can split it out if you'd like.