# Fetching

Fetching follows ADR 002.

Each host has a queue of its feeds and one worker. A worker takes the feed that has waited longest, fetches it, and waits at least 10 seconds before its next request to that host. A feed is due again 15 minutes after its last fetch. Hosts with nothing due have no worker running.

A fetch sends `If-None-Match` and `If-Modified-Since` from the last response, and a `304` stores nothing. After five failures in a row, a feed is due once a day until it succeeds.
