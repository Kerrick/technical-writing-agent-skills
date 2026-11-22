from quillfeed.fetch import SPACING_SECONDS, HostQueue


def test_two_requests_to_one_host_are_spaced():
    now, slept = [0.0], []

    def sleep(seconds):
        slept.append(seconds)
        now[0] += seconds

    queue = HostQueue("example.org", fetch=lambda feed: None, clock=lambda: now[0], sleep=sleep)
    queue.add("https://example.org/a.xml")
    queue.add("https://example.org/b.xml")
    queue.run_once()
    queue.run_once()
    assert slept == [SPACING_SECONDS]
