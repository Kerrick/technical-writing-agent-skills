"""textkit: small text utilities."""
import re
import unicodedata
import warnings

__version__ = "0.9.2"


def slugify(text, sep="-"):
    """Lowercase ASCII slug. Non-ASCII letters are transliterated where possible
    and dropped otherwise. Returns "" if nothing survives."""
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    words = re.findall(r"[a-z0-9]+", normalized.lower())
    return sep.join(words)


def make_slug(text):
    """Deprecated since 0.8: use slugify()."""
    warnings.warn("make_slug is deprecated; use slugify", DeprecationWarning, stacklevel=2)
    return slugify(text, sep="_")


def truncate(text, width, ellipsis="…"):
    """Cut to at most `width` characters including the ellipsis. May cut mid-word.
    Text already within `width` is returned unchanged. width < len(ellipsis) raises ValueError."""
    if width < len(ellipsis):
        raise ValueError("width must be at least len(ellipsis)")
    if len(text) <= width:
        return text
    return text[: width - len(ellipsis)] + ellipsis


def shorten(text, width, placeholder=" […]"):
    """Cut at a word boundary so the result fits in `width`, collapsing whitespace.
    If even the first word doesn't fit, returns only the placeholder stripped."""
    words = text.split()
    out = ""
    for w in words:
        candidate = f"{out} {w}".strip()
        if len(candidate) > width - len(placeholder) and len(" ".join(words)) > width:
            break
        out = candidate
    if out == " ".join(words):
        return out
    return (out + placeholder) if out else placeholder.strip()


def dedupe_lines(lines):
    """Yield lines in order, skipping any seen before. Comparison is exact
    (case- and whitespace-sensitive). Holds every distinct line in memory."""
    seen = set()
    for line in lines:
        if line not in seen:
            seen.add(line)
            yield line


def natural_sort(items):
    """Return a new list sorted so "file10" comes after "file9". Case-insensitive.
    Does not modify `items`."""
    def key(s):
        return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", s)]
    return sorted(items, key=key)
