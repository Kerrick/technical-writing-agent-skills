# textkit API reference

Reference for every public function in `textkit`, a small library of text utilities. For a task-oriented introduction, use the user guide.

Examples are self-contained. Paste them into a Python session after `from textkit import *`. To print the installed version:

```python
import textkit
print(textkit.__version__)
```

| Function | Purpose |
| --- | --- |
| [`slugify`](#slugify) | Convert text to a lowercase ASCII slug |
| [`make_slug`](#make_slug) | Deprecated. Use `slugify` |
| [`truncate`](#truncate) | Cut to a fixed number of characters |
| [`shorten`](#shorten) | Cut at a word boundary |
| [`dedupe_lines`](#dedupe_lines) | Remove repeated lines, keeping order |
| [`natural_sort`](#natural_sort) | Sort strings with numbers in numeric order |

To limit text length, use `truncate` when you need an exact maximum and can accept a cut inside a word. Use `shorten` when you need whole words.

## slugify

```python
slugify(text, sep="-") -> str
```

Returns a lowercase ASCII slug made of the letters and digits in `text`, joined by `sep`.

| Parameter | Description |
| --- | --- |
| `text` | The string to convert. |
| `sep` | String placed between words. Default `"-"`. |

- Accented letters that decompose to ASCII are transliterated (`é` becomes `e`). Any other non-ASCII character is dropped, not transliterated. `ß` is dropped, and text with only such characters, such as `日本語`, gives `""`.
- Any run of characters other than `a-z` and `0-9` is one word break.
- Returns `""` when nothing survives. Check for an empty result before you use a slug as an identifier or filename.

```python
>>> slugify("Héllo, Wörld! 2024")
'hello-world-2024'
>>> slugify("Hello World", sep="_")
'hello_world'
>>> slugify("Straße")      # ß is dropped, not expanded to "ss"
'strae'
>>> slugify("日本語")
''
```

## make_slug

```python
make_slug(text) -> str
```

Deprecated: use [`slugify`](#slugify). Emits a `DeprecationWarning` on every call.

`make_slug(text)` returns the same as `slugify(text, sep="_")`. Its separator is `_`, not the `-` that `slugify` uses by default. To migrate and keep your output unchanged, call `slugify(text, sep="_")`.

> **Change note, 0.8:** `make_slug` was deprecated in favour of `slugify`.

## truncate

```python
truncate(text, width, ellipsis="…") -> str
```

Returns `text` cut to at most `width` characters. When the text is cut, `ellipsis` forms the end of the result and counts toward `width`.

| Parameter | Description |
| --- | --- |
| `text` | The string to cut. |
| `width` | Maximum length of the result, in characters. |
| `ellipsis` | Marker added when the text is cut. Default `"…"`. May be `""`. |

- Text of `width` characters or fewer is returned unchanged, with no ellipsis.
- The cut can fall in the middle of a word. Use [`shorten`](#shorten) to cut at a word boundary.
- Raises `ValueError` if `width` is less than `len(ellipsis)`.

```python
>>> truncate("The quick brown fox", 10)
'The quick…'
>>> truncate("short", 10)
'short'
>>> truncate("The quick brown fox", 10, ellipsis="")
'The quick '
```

## shorten

```python
shorten(text, width, placeholder=" […]") -> str
```

Returns `text` cut at a word boundary so that the result fits in `width` characters. Runs of whitespace in `text` become single spaces.

| Parameter | Description |
| --- | --- |
| `text` | The string to cut. |
| `width` | Maximum length of the result, in characters. |
| `placeholder` | Marker added when the text is cut. Default `" […]"`. It counts toward `width`. |

- If the whole text, with whitespace collapsed, fits in `width`, it is returned without the placeholder.
- If not even the first word fits together with the placeholder, the result is the placeholder with surrounding whitespace removed, and none of the text.

```python
>>> shorten("The quick brown fox jumps", 15)
'The quick […]'
>>> shorten("  hello   world ", 50)      # fits: whitespace collapsed, no placeholder
'hello world'
>>> shorten("Supercalifragilistic word", 10)
'[…]'
```

## dedupe_lines

```python
dedupe_lines(lines) -> Iterator[str]
```

A generator that yields each distinct item of `lines` the first time it appears, in input order.

| Parameter | Description |
| --- | --- |
| `lines` | An iterable of strings, such as a list or an open file. |

- Comparison is exact. It is case-sensitive and whitespace-sensitive, so `"a"`, `"A"` and `"a "` are three different lines. Lines read from a file keep their trailing newline, so a final line without a newline differs from the same text with one.
- It is lazy. Nothing runs until you iterate over the result. Wrap it in `list()` to get all lines at once.
- It keeps every distinct line in memory, so memory use grows with the number of distinct lines.

```python
>>> list(dedupe_lines(["a", "b", "a", "A", "a "]))
['a', 'b', 'A', 'a ']
```

## natural_sort

```python
natural_sort(items) -> list[str]
```

Returns a new list of the strings in `items`, sorted so that digit runs compare as numbers (`"file9"` before `"file10"`) and letters compare without regard to case. `items` is not modified.

| Parameter | Description |
| --- | --- |
| `items` | An iterable of strings. |

- Strings that differ only in case compare as equal and keep their input order.
- Returned strings keep their original case.

```python
>>> natural_sort(["file10", "file9", "File1", "b2", "a"])
['a', 'b2', 'File1', 'file9', 'file10']
```
