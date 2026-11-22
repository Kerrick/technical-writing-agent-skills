"""Fetch feeds. One poller walks every feed in turn (ADR 002)."""

import threading
import time
from collections import defaultdict
from urllib.parse import urlsplit

SPACING_SECONDS = 10  # between two requests to one host
DUE_AFTER_SECONDS = 15 * 60


class HostQueue:
    """The feeds of one host, and the one worker that fetches them."""

    def __init__(self, host, fetch, clock=time.monotonic, sleep=time.sleep):
        self.host, self.fetch, self.clock, self.sleep = host, fetch, clock, sleep
        self.feeds = []
        self.last_request = None

    def add(self, feed):
        self.feeds.append(feed)

    def run_once(self):
        """Fetch the feed that has waited longest, after the spacing ADR 002 requires."""
        if not self.feeds:
            return None
        if self.last_request is not None:
            wait = SPACING_SECONDS - (self.clock() - self.last_request)
            if wait > 0:
                self.sleep(wait)
        feed = self.feeds.pop(0)
        self.last_request = self.clock()
        self.fetch(feed)
        self.feeds.append(feed)
        return feed


def queues_for(feeds, fetch):
    queues = defaultdict(lambda: None)
    for feed in feeds:
        host = urlsplit(feed).hostname
        queues[host] = queues[host] or HostQueue(host, fetch)
        queues[host].add(feed)
    return dict(queues)


def start(feeds, fetch):
    for queue in queues_for(feeds, fetch).values():
        threading.Thread(target=_work, args=(queue,), daemon=True).start()


def _work(queue):
    while True:
        queue.run_once()
