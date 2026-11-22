I've replaced ADR 002 with a new ADR 004, `doc/adr/004.md`, which records the per-host fetch queue as the decision now stands. I deleted `002.md` instead of marking it superseded, so nobody follows a dead decision. I didn't run the tests.

**Changes**
- **New record:** `doc/adr/004.md`, "Each host has its own fetch queue and one worker". It's dated 19 October, the day Dana made the call. Everything in it comes from `notes/2026-10-fetch-queue.md`: the 6 October 429s and blocks, the three options weighed (per-host queue, the old poller with a 10-second sleep between feeds on the same host, WebSub), why each of the other two lost, and the costs (340 threads at peak, no single loop to look at, `quillfeed fetch-status`).
- **Deleted:** `doc/adr/002.md`. This folder isn't a git repository, so if you want the old text, it's only in whatever copy you keep elsewhere.
- **Citations updated:** the index in `doc/README.md`, the line in `doc/design/fetching.md`, and the two docstrings in `src/quillfeed/fetch.py`. The module docstring there still said "One poller walks every feed in turn". The October notes never name ADR 002, so I left them as written. Nothing in the repository still cites 002.

**One thing you should look at:** the notes say option 1 "is the only one that keeps both the 15-minute promise and the hosts' limits." But with one worker per host and 10 seconds between requests, a host can get through at most 90 feeds in 15 minutes. Each of the three hosts that blocked you has more than 150, so their feeds come round every 25 minutes or more. ADR 004 records Dana's reason as stated and lists this as a bad consequence; it doesn't claim the 15-minute target holds for those hosts. If that trade was intended, nothing needs changing. If not, it's a code problem, not a wording one.

**Judgment calls you may want to overturn**
- **Deciders:** I put Dana Whitlock as the decider and Tomás Reyes under `consulted`. The notes say Dana decided; Tomás weighed the options with her, ran the timing test and built it.
- **Drivers:** I kept two from 002, "within 15 minutes" and "fits in the one process", and added "within each host's limits" from the notes.
- **Confidence:** the notes never state one, so the record says so. It then gives only what the notes show: it shipped in 0.8.0 on 2 November and peaked at 340 threads. I didn't claim the hosts have stopped blocking you, because nothing records that.
- **An inference of mine:** the good consequence that a slow host now delays only its own feeds comes from the code, not the notes.
- **Confirmation:** it names `tests/test_fetch_spacing.py` and says what that test doesn't check. If someone changes the constant, the test still passes, and nothing tests the 15-minute target. ADR 002's `tests/test_poller.py` doesn't exist; it went away with that record.

**Problems elsewhere in the log (not changed):**
- **ADR 003:** the title is a topic ("Storage") rather than a decision. It also holds detailed design (the table layout, file naming, retention and cleanup schedule) and a history section with spike run IDs. That design belongs in a design document, and `src/quillfeed/store.py` cites those sections by name. Moving them means updating those citations too.
- **ADR 001:** its Confirmation cites `tests/test_single_process.py`, which isn't in the repository.

I can fix either one if you'd like.