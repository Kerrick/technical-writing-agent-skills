# textkit API reference

Version 0.9. Every name on this page is imported from the `textkit` module:

```python
from textkit import slugify, truncate, shorten, dedupe_lines, natural_sort
```

| Function | What it does |
| --- | --- |
| [`slugify`](#slugify) | Turns text into a lowercase ASCII slug. |
| [`truncate`](#truncate) | Cuts text to a fixed length, mid-word if needed. |
| [`shorten`](#shorten) | Cuts text at a word boundary. |
| [`dedupe_lines`](#dedupe_lines) | Drops repeated lines, keeping the first. |
| [`natural_sort`](#natural_sort) | Sorts so `file9` comes before `file10`. |
| [`make_slug`](#make_slug-legacy) | Legacy. Use `slugify`. |

Passing `None` or another non-string type to a text function raises `TypeError`. `dedupe_lines` is the exception: it accepts any iterable of hashable items. textkit does not strip, normalize, or validate text beyond what each entry states.

## slugify

```python
slugify(text, sep="-")
```

Returns `text` as a lowercase ASCII slug: runs of letters and digits joined by `sep`. Everything else, including punctuation and whitespace, is a separator and is not kept.

Accented Latin letters are reduced to their base letter (`é` becomes `e`). Compatibility characters are expanded (`ﬁ` becomes `fi`, `①` becomes `1`). Characters with no ASCII decomposition are dropped, not replaced. That includes `ß`, `æ`, `ø`, `ł`, and every non-Latin script. Returns `""` if nothing survives.

| Call | Result |
| --- | --- |
| `slugify("Héllo, Wörld! 2024")` | `'hello-world-2024'` |
| `slugify("Hello World", sep="_")` | `'hello_world'` |
| `slugify("Straße")` | `'strae'` |
| `slugify("日本語")` | `''` |
| `slugify("")` | `''` |

**Check for an empty result.** Dropped characters don't raise an error. A title written entirely in a non-Latin script yields `""`, which is a valid but useless URL segment or filename:

```python
slug = slugify(title)
if not slug:
    # Fall back to a value that can't be empty, such as the record's id.
    slug = f"post-{post_id}"
```

`slugify` doesn't enforce uniqueness or a maximum length. Different titles can give the same slug (`"Café"` and `"Cafe"` both give `'cafe'`), so check for collisions where you store slugs.

## truncate

```python
truncate(text, width, ellipsis="…")
```

Returns `text` cut to at most `width` characters, with the ellipsis counted inside that width. It cuts at exactly that position, so it can split a word. Text that already fits (`len(text) <= width`) is returned unchanged, with no ellipsis. Raises `ValueError` if `width` is less than `len(ellipsis)`.

| Call | Result |
| --- | --- |
| `truncate("The quick brown fox", 10)` | `'The quick…'` |
| `truncate("short", 10)` | `'short'` |
| `truncate("abcdef", 3)` | `'ab…'` |
| `truncate("abcdef", 3, "...")` | `'...'` |
| `truncate("abcdef", 0, "")` | `''` |
| `truncate("abc", 0)` | raises `ValueError` |

Length is counted in Python characters (code points), not display width, so a combining accent or emoji sequence can be split.

## shorten

```python
shorten(text, width, placeholder=" […]")
```

Returns as many whole words as fit, followed by `placeholder`, so the result fits in `width`. Runs of whitespace, including newlines, are collapsed to single spaces. If the whole text fits after collapsing, it is returned without the placeholder. If not even the first word fits, the result is only the placeholder with surrounding spaces stripped.

| Call | Result |
| --- | --- |
| `shorten("The quick brown fox jumps over the lazy dog", 20)` | `'The quick brown […]'` |
| `shorten("short text", 20)` | `'short text'` |
| `shorten("a  b\n c", 20)` | `'a b c'` |
| `shorten("Supercalifragilistic word", 10)` | `'[…]'` |
| `shorten("", 5)` | `''` |
| `shorten("The quick brown fox", 20, "...")` | `'The quick brown fox'` |

**The result can be longer than `width`.** When `width` is smaller than the stripped placeholder, `shorten` still returns the placeholder: `shorten(text, 2)` returns `'[…]'`, which is 3 characters. If the limit is hard, pass a `width` of at least `len(placeholder.strip())`.

Cost: `shorten` splits the whole input before cutting, so time and memory grow with the length of `text`, not `width`. To preview a very large document, slice the text first.

### truncate or shorten?

|  | `truncate` | `shorten` |
| --- | --- | --- |
| Cuts at | Exact character position | Word boundary |
| Can split a word | Yes | No |
| Whitespace | Kept as is | Collapsed |
| Marker | `ellipsis`, appended directly (`…`) | `placeholder`, appended after a space (` […]`) |
| Word longer than `width` | Cut mid-word | Only the placeholder is returned |
| `width` too small | `ValueError` | Returns the placeholder, which may exceed `width` |

Use `truncate` for fixed-size fields such as a database column or table cell. Use `shorten` for prose a person reads, such as a summary or search snippet.

## dedupe_lines

```python
dedupe_lines(lines)
```

A generator. Yields each item of the iterable `lines` the first time it appears, in input order, and skips later repeats. Nothing is read until you iterate. It accepts any iterable, including a file object, and does not modify its input.

Comparison is exact. `"a"` and `"A"` differ, and so do `"b"` and `"b "`. The empty string is a line like any other, so only the first blank line survives. An empty input yields nothing.

**Line endings count.** Iterating over a file yields lines with their trailing `"\n"`. A final line with no newline differs from an earlier identical line that has one, so both are kept:

```python
list(dedupe_lines(["x\n", "x"]))
# ['x\n', 'x']
```

Strip first when that matters: `dedupe_lines(line.rstrip("\n") for line in f)`.

Cost: it keeps every distinct line in memory until the generator is discarded, so memory grows with the number of distinct lines. Output is produced as input arrives, so it works on streams without loading them first. A generator can be iterated once; call `list(...)` if you need the result twice.

```python
lines = ["a", "b", "a", "A", "b ", "b", ""]
list(dedupe_lines(lines))
# ['a', 'b', 'A', 'b ', '']
```

Removing repeated lines from a file, line endings included:

```python
with open("access.log", encoding="utf-8") as src, open("unique.log", "w", encoding="utf-8") as dst:
    dst.writelines(dedupe_lines(src))
```

## natural_sort

```python
natural_sort(items)
```

Returns a new list of `items` sorted so that runs of digits compare as numbers and everything else compares case-insensitively. `items` is not modified. An empty list returns `[]`. Every item must be a `str`; otherwise it raises `TypeError`.

| Call | Result |
| --- | --- |
| `natural_sort(["file10", "file9", "File2", "file1"])` | `['file1', 'File2', 'file9', 'file10']` |
| `natural_sort(["v1.10", "v1.9", "v1.2"])` | `['v1.2', 'v1.9', 'v1.10']` |
| `natural_sort(["b", "a", "A"])` | `['a', 'A', 'b']` |
| `natural_sort(["x01", "x1"])` | `['x01', 'x1']` |
| `natural_sort(["x1", "x01"])` | `['x1', 'x01']` |

- **Ties keep input order.** Items that differ only by case (`"a"`, `"A"`) or leading zeros (`"x01"`, `"x1"`) compare equal, so they stay in the order you passed them.
- **Only digit runs are numeric.** Signs and decimal points are plain text. `"v1.10"` sorts after `"v1.9"` because the parts `1`, `.`, and `10` are compared in turn, not because it is read as the number 1.10.
- **Plain `sorted` gets this wrong.** `sorted(["file10", "file9"])` returns `['file10', 'file9']`.

Cost: it sorts a copy, so memory is one extra list.

## make_slug (legacy)

```python
make_slug(text)
```

Deprecated since 0.8. Use [`slugify`](#slugify). `make_slug(text)` is equivalent to `slugify(text, sep="_")` plus a `DeprecationWarning`. It takes no `sep` argument. Python hides `DeprecationWarning` by default unless the calling code is the `__main__` script, so run with `python -W default` or under a test runner such as pytest to see it.

| Legacy | Current |
| --- | --- |
| `make_slug("Hello World")` returns `'hello_world'` | `slugify("Hello World", sep="_")` returns `'hello_world'` |

To migrate, replace each call with `slugify(text, sep="_")`. That keeps existing slugs unchanged. Switch to the default `-` only for new slugs, because changing the separator changes the slug of every existing record.
