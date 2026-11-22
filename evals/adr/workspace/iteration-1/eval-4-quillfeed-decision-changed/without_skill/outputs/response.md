I fixed the decision log by writing a new ADR 004 that supersedes ADR 002, rather than rewriting 002. That way the log still shows the March decision and why it changed.

**What changed:**
- **`doc/adr/004.md` (new):** "Each host has its own fetch queue, with requests to it spaced 10 seconds apart." I wrote it from your October notes: the 6 October 429s and blocks, the three options and why two of them lost (one walk taking 70 minutes, only 9% of feeds advertising a WebSub hub), the 0.8.0 release, and the costs (340 threads at peak, `quillfeed fetch-status`). Its confirmation is `tests/test_fetch_spacing.py`. I listed Dana as the decider and Tomás as consulted, because the notes say Dana made the call.
- **`doc/adr/002.md`:** the status is now "superseded by ADR 004", with a one-line pointer at the top. The rest is as written.
- **`doc/README.md`:** in the index, 002 is struck through and marked superseded, and 004 is added.
- **ADR references:** `doc/design/fetching.md` and both comments in `src/quillfeed/fetch.py` pointed to ADR 002. They now point to ADR 004. This is the only change to the code.

**Worth a look:**
1. **The 15-minute target doesn't hold for big hosts.** The notes say option 1 keeps the "new article within 15 minutes" promise. But at one request every 10 seconds, a host can get at most 90 fetches per 15 minutes, and each of the three hosts that blocked you serves more than 150 feeds. Fetching 150 feeds takes 25 minutes. I didn't repeat the claim in ADR 004; I listed this as a "Bad" consequence instead. Correct it if I've misread how due times work.
2. **I didn't say whether the fix worked.** Nothing in the notes says whether those hosts have stayed unblocked since 0.8.0, so ADR 004 calls it "not yet known." Update that if you know.
3. **The design doc and the code disagree.** `fetching.md` says hosts with nothing due have no worker running and that feeds are due 15 minutes after their last fetch. In `fetch.py`, `start()` keeps one thread per host running forever, and `DUE_AFTER_SECONDS` is never used. I left both alone.
4. **Two smaller loose ends:**
   - ADR 002 still cites `tests/test_poller.py`, which no longer exists. I left it because that record is kept as written.
   - ADR 003's own title is "Storage", which doesn't match its line in the index.