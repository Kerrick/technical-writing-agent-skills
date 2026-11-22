I replaced ADR 002 with a new ADR 004 and updated everything that pointed at 002. Nothing in the repo cites ADR 002 any more.

**What changed**
- **`doc/adr/004.md`** (new): it restates the whole fetch decision as it stands now. Each host gets its own queue and one worker, requests to a host are at least 10 seconds apart, and hosts are fetched side by side. The three options and the reasons for the choice come from `notes/2026-10-fetch-queue.md`.
- **`doc/adr/002.md`** is deleted, not marked "superseded." It stays in history, and a stale record would only mislead readers.
- **`doc/README.md`**: the index drops 002 and adds 004.
- **`doc/design/fetching.md`**: now says "Fetching follows ADR 004."
- **`src/quillfeed/fetch.py`**: both docstrings now cite ADR 004. The module docstring no longer says "one poller walks every feed in turn" and points to the design doc for how fetching works.
- **`notes/2026-10-fetch-queue.md`** is unchanged. It's a dated note and never mentions ADR 002.

**Judgment calls you may want to overturn**
- **New number, not an edit:** 004 is the next number after 003. There's no git repo here, so I couldn't check whether a number above 003 was ever used and deleted.
- **Deciders:** Dana is the only decider, since the note says "Decided, 19 October (Dana)." Tomás is listed as consulted because he helped weigh the options and ran the test of option 2. Building the queue isn't recorded in the ADR.
- **Drivers:** only the two the note gives: the 15-minute promise and the hosts' limits. "Fetching must fit in the one process" was a driver of 002, but the October note doesn't mention it, so I left it out.
- **Options:** only the three weighed in October. The old "timer per feed" option wasn't weighed this time, so it's gone.
- **Consequences:**
  - The three from 002 don't apply to the new design, so none carried over.
  - "A slow host delays only its own feeds" is my inference from fetching hosts side by side; the note doesn't say it.
  - The bad consequences come straight from the note: 340 threads at the peak instead of one, and no single loop to look at when fetching stops, which `quillfeed fetch-status` was added to help with.
- **Confidence:** the deciders didn't state one, so the record says so. It then gives what's known: it shipped in 0.8.0 and the spacing is tested. Nothing measures the 15-minute promise or whether the blocks stopped.

**Problems I found but didn't fix**
1. **The code may not do what the design doc says.** `DUE_AFTER_SECONDS` is defined in `fetch.py` but never used. `_work` calls `run_once()` in an endless loop, so each host's worker cycles through its feeds every 10 seconds rather than waiting until a feed is due 15 minutes after its last fetch. Workers also start for every host, not only hosts with something due. Either the rest of this lives somewhere I didn't see, or the code and `doc/design/fetching.md` disagree.
2. **ADR 001 cites a missing test.** `tests/test_single_process.py` doesn't exist. (ADR 002 cited a missing `tests/test_poller.py` too, but it's gone now.)
3. **ADR 003 has several problems a review would flag:**
   - Its title, "Storage", names a topic, not a decision.
   - It holds detailed design (table layout, file naming, retention, cleanup schedule) that belongs in a design document.
   - It ends with a History section that names spike runs.

   I can split it if you want.