# textkit API reference

Reference for `textkit` 0.9. Python 3, standard library only. For task-oriented walkthroughs, see the [0.9 user guide](./user-guide.md).

```python
from textkit import slugify, truncate, shorten, dedupe_lines, natural_sort
```

| Function | Purpose |
| - | - |
| [`dedupe_lines`](#dedupe_lines) | Yield each distinct line once, in first-seen order. |
| [`natural_sort`](#natural_sort) | Sort strings so `file9` comes before `file10`. |
| [`shorten`](#shorten) | Cut text at a word boundary to fit a width. |
| [`slugify`](#slugify) | Convert text to a lowercase ASCII slug. |
| [`truncate`](#truncate) | Cut text to a width, possibly mid-word. |
| [`make_slug`](#make_slug) (deprecated) | Replaced by `slugify`. |

All functions are pure except `dedupe_lines`, which consumes its input iterable. Lengths and widths count Python characters (code points), not bytes or display columns.

---

## dedupe_lines

Yields lines in order, skipping any line already seen.

```python
dedupe_lines(lines)
```

| Parameter | Type | Description |
| - | - | - |
| `lines` | iterable of `str` | Lines to filter. Any hashable items work; the function does not check for `str`. |

**Returns:** a generator. Each distinct line is yielded the first time it appears.

**Behavior**

- Comparison is exact. Case and whitespace matter: `"a"`, `"A"`, and `"a "` are three distinct lines.
- The generator keeps every distinct line in memory until it is exhausted.
- Evaluation is lazy, so it works on a file object or other stream.

```python
>>> list(dedupe_lines(["a", "b", "a", "A", "a "]))
['a', 'b', 'A', 'a ']
```

---

## natural_sort

Returns a new list sorted in natural order, where digit runs compare as numbers.

```python
natural_sort(items)
```

| Parameter | Type | Description |
| - | - | - |
| `items` | iterable of `str` | Strings to sort. |

**Returns:** a new `list`. `items` is not modified.

**Behavior**

- Comparison is case-insensitive.
- Each string splits into digit runs and other text. Digit runs compare as integers, other text compares lowercased.
- Only unsigned digit runs are numeric. A `-` or `.` is ordinary text.

```python
>>> natural_sort(["file10", "file9", "File2", "a"])
['a', 'File2', 'file9', 'file10']
```

---

## shorten

Cuts text at a word boundary so the result fits in `width`, and appends a placeholder.

```python
shorten(text, width, placeholder=" […]")
```

| Parameter | Type | Default | Description |
| - | - | - | - |
| `text` | `str` | required | Text to shorten. |
| `width` | `int` | required | Maximum length of the result, including the placeholder. |
| `placeholder` | `str` | `" […]"` | Appended when words are removed. Includes its leading space. |

**Returns:** a `str`.

- Whitespace in `text` is collapsed: the text is split on whitespace runs and rejoined with single spaces. This applies even when nothing is cut.
- If the collapsed text fits in `width`, it is returned without a placeholder.
- Otherwise the result is as many whole words as fit, followed by `placeholder`.
- If not even the first word fits, the result is `placeholder.strip()` alone (`"[…]"` by default).

**Edge case:** the placeholder is never dropped to meet `width`. If `width` is smaller than the placeholder, the result can be longer than `width`. For example, `shorten(text, 0)` returns `"[…]"`.

```python
>>> shorten("The quick brown fox jumps over the lazy dog", 20)
'The quick brown […]'
>>> shorten("The quick brown fox jumps over the lazy dog", 50)
'The quick brown fox jumps over the lazy dog'
>>> shorten("Supercalifragilistic word", 10)
'[…]'
```

**Related:** use [`truncate`](#truncate) to cut mid-word to an exact width.

---

## slugify

Converts text to a lowercase ASCII slug.

```python
slugify(text, sep="-")
```

| Parameter | Type | Default | Description |
| - | - | - | - |
| `text` | `str` | required | Text to convert. |
| `sep` | `str` | `"-"` | String placed between words. |

**Returns:** a `str` of the lowercase ASCII words in `text` joined by `sep`. Returns `""` if no ASCII letters or digits remain.

**Behavior**

- Text is Unicode-normalized (NFKD), then non-ASCII characters are removed. Accented Latin letters therefore keep their base letter (`é` → `e`).
- Characters with no NFKD decomposition into ASCII are dropped, not transliterated. `ß` and `Æ` are dropped, and CJK text is removed entirely.
- A word is a run of `a-z` and `0-9`. All other characters, including punctuation and whitespace, separate words. Leading, trailing, and repeated separators never appear.

```python
>>> slugify("Héllo, Wörld! 2024")
'hello-world-2024'
>>> slugify("a b", sep="_")
'a_b'
>>> slugify("Straße Æon")
'strae-on'
>>> slugify("日本")
''
```

---

## truncate

Cuts text to at most `width` characters, ellipsis included. Can cut mid-word.

```python
truncate(text, width, ellipsis="…")
```

| Parameter | Type | Default | Description |
| - | - | - | - |
| `text` | `str` | required | Text to cut. |
| `width` | `int` | required | Maximum length of the result, including `ellipsis`. |
| `ellipsis` | `str` | `"…"` | Appended when the text is cut. Pass `""` for a plain cut. |

**Returns:** `text` unchanged if `len(text) <= width`. Otherwise the first `width - len(ellipsis)` characters of `text` followed by `ellipsis`.

**Raises**

| Exception | Message | Cause |
| - | - | - |
| `ValueError` | `width must be at least len(ellipsis)` | `width < len(ellipsis)`. Raised before the length of `text` is checked, so it applies even to short text. Increase `width` or use a shorter `ellipsis`. |

```python
>>> truncate("The quick brown fox", 10)
'The quick…'
>>> truncate("short", 10)
'short'
>>> truncate("abcdef", 3, "...")
'...'
```

**Related:** use [`shorten`](#shorten) to cut at a word boundary.

---

## make_slug

> **Deprecated since 0.8.** Use [`slugify(text, sep="_")`](#slugify) instead.

```python
make_slug(text)
```

Calls `slugify(text, sep="_")` and returns the result. Emits a `DeprecationWarning` with the message `make_slug is deprecated; use slugify`, attributed to the caller's line.

Python hides `DeprecationWarning` by default outside `__main__` and test runners. To find remaining calls, run with `python -W error::DeprecationWarning` or `python -W always`.

| Before | After |
| - | - |
| `make_slug(text)` | `slugify(text, sep="_")` |

```python
>>> make_slug("Hello World")
'hello_world'
```

No removal version has been announced.
