from tallyho import count_words


def test_most_common_first():
    assert count_words("b a b c b a", limit=2) == [("b", 3), ("a", 2)]
