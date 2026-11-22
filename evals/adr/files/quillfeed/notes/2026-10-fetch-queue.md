# Fetch queue, October 2026

## What happened

On 6 October three hosts (two blog platforms and a podcast host) started answering 429 and then blocked the instance's address for a day. Each serves more than 150 of our feeds, and the poller walked them back to back: 150 requests to one host in about 20 seconds, every 15 minutes.

## What we looked at (Dana and Tomás, 12 to 19 October)

1. A queue per host, each with one worker that leaves at least 10 seconds between requests to its host. Hosts are fetched side by side.
2. Keep the one poller, and have it sleep 10 seconds between two feeds on the same host. Tomás ran it against the maintainer's 2,400 feeds: one walk went from 6 minutes to 70, so a new article could take over an hour to show up.
3. Drop polling and subscribe with WebSub, so hosts push new articles. Of the 2,400 feeds, 216 (9%) advertise a hub.

## Decided, 19 October (Dana)

Option 1. It is the only one that keeps both the 15-minute promise and the hosts' limits. Option 2 breaks the first, option 3 leaves out 91% of feeds. Tomás built it; it shipped in 0.8.0 on 2 November.

Costs we know about: one thread per host with something due, which was 340 threads at the peak on Dana's instance, against one before. And when fetching stops, there is no longer one loop to look at; `quillfeed fetch-status` was added to list each host's queue.

`tests/test_fetch_spacing.py` checks the 10 seconds.
