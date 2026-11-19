# textkit API reference

Version 0.9.2. Everything below is importable from the top-level `textkit` module.

```python
import textkit
```

| Function | Summary |
| --- | --- |
| [`slugify`](#slugify) | Turn text into a lowercase ASCII slug. |
| [`truncate`](#truncate) | Cut text to a fixed width, possibly mid-word. |
| [`shorten`](#shorten) | Cut text to a width at a word boundary. |
| [`dedupe_lines`](#dedupe_lines) | Drop repeated lines, keeping first occurrences in order. |
| [`natural_sort`](#natural_sort) | Sort strings so embedded numbers compare numerically. |
| [`make_slug`](#make_slug) | *Deprecated.* Use `slugify`. |

---

## slugify

```python
slugify(text, sep="-") -> str
```

Returns a lowercase ASCII slug made of runs of letters and digits joined by `sep`. Accented letters are transliterated (`é` → `e`). Characters with no ASCII equivalent are dropped. Punctuation and whitespace act as separators.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | | Text to convert. |
| `sep` | `str` | `"-"` | String placed between words. |

Returns `""` if nothing survives, for example when `text` is entirely non-Latin script. Check for an empty result if you use slugs as identifiers.

```python
>>> slugify("Crème Brûlée, 2nd ed.!")
'creme-brulee-2nd-ed'
>>> slugify("Hello World", sep="_")
'hello_world'
>>> slugify("日本語")
''
```

## truncate

```python
truncate(text, width, ellipsis="…") -> str
```

Cuts `text` to at most `width` characters, **counting the ellipsis**. The cut can land mid-word. If `text` already fits within `width`, it is returned unchanged with no ellipsis added.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | | Text to cut. |
| `width` | `int` | | Maximum length of the result. |
| `ellipsis` | `str` | `"…"` | Appended when the text is cut. |

**Raises** `ValueError` if `width < len(ellipsis)`. This check runs even when `text` would fit.

```python
>>> truncate("Hello, world", 8)
'Hello, …'
>>> truncate("Hello, world", 8, ellipsis="...")
'Hello...'
>>> truncate("Hi", 8)
'Hi'
```

To avoid cutting mid-word, use [`shorten`](#shorten).

## shorten

```python
shorten(text, width, placeholder=" […]") -> str
```

Fits `text` into `width` characters by dropping whole words from the end and appending `placeholder`. Runs of whitespace (including newlines) are collapsed to single spaces in the output, even when no words are dropped.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | | Text to shorten. |
| `width` | `int` | | Maximum length of the result, including `placeholder`. |
| `placeholder` | `str` | `" […]"` | Appended when words are dropped. |

If the first word doesn't fit, the result is only `placeholder.strip()` (`"[…]"` by default). In that case the result can be **longer than `width`**, for example when `width` is smaller than the placeholder.

```python
>>> shorten("The quick brown fox jumps", 15)
'The quick […]'
>>> shorten("  a   b  ", 10)
'a b'
>>> shorten("Supercalifragilistic word", 10)
'[…]'
```

## dedupe_lines

```python
dedupe_lines(lines) -> Iterator[str]
```

Yields each item of `lines` the first time it appears and skips later repeats, preserving order. `lines` can be any iterable, such as a list or an open file. The result is a generator, so wrap it in `list()` if you need a list.

Matching is exact: case, leading and trailing whitespace, and line endings all count. A file's last line with no trailing `\n` won't match an otherwise identical earlier line. Strip lines first if that matters.

Every distinct line is held in memory, so memory use grows with the number of unique lines.

```python
>>> list(dedupe_lines(["a", "b", "a", "A", "a "]))
['a', 'b', 'A', 'a ']
```

## natural_sort

```python
natural_sort(items) -> list[str]
```

Returns a new sorted list in which digit runs compare as numbers, so `"file9"` sorts before `"file10"`. Comparison is case-insensitive. `items` is not modified.

Items that compare equal keep their original order. That includes items differing only by case, and numbers differing only by leading zeros (`"x01"` and `"x1"`). All items must be strings.

```python
>>> natural_sort(["file10", "File2", "file9", "file1"])
['file1', 'File2', 'file9', 'file10']
```

## make_slug

> **Deprecated since 0.8.** Use [`slugify`](#slugify). Calling `make_slug` emits a `DeprecationWarning`.

```python
make_slug(text) -> str
```

Equivalent to `slugify(text, sep="_")`. Note that this uses an **underscore**, not `slugify`'s default hyphen. To keep existing slugs unchanged when you migrate, pass `sep="_"`:

```python
# before
make_slug("Hello World")          # 'hello_world'
# after
slugify("Hello World", sep="_")   # 'hello_world'
```
