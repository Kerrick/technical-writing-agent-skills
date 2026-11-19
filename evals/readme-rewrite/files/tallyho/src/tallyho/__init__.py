from collections import Counter
import re

__all__ = ["count_words"]


def count_words(text: str, limit: int = 10) -> list[tuple[str, int]]:
    """Return the `limit` most common lowercase words in `text`, most common first."""
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(limit)
