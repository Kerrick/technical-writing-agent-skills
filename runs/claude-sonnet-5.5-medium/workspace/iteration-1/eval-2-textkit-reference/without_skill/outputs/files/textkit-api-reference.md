# textkit API reference

Version 0.9.2. For a walkthrough, see the [0.9 user guide](#).

```python
import textkit
```

| Function | Purpose |
| --- | --- |
| [`slugify`](#slugify) | Turn text into a lowercase ASCII slug |
| [`truncate`](#truncate) | Cut text to a maximum width, mid-word if needed |
| [`shorten`](#shorten) | Cut text to a maximum width at a word boundary |
| [`dedupe_lines`](#dedupe_lines) | Drop repeated lines, keeping first occurrences |
| [`natural_sort`](#natural_sort) | Sort strings so `file9` comes before `file10` |
| [`make_slug`](#make_slug) | Deprecated alias for `slugify` |

---

## slugify

```python
slugify(text, sep="-")
```

Convert `text` to a lowercase ASCII slug. Runs of letters and digits become words joined by `sep`. Everything else, including punctuation and whitespace, is a separator.

Accented letters are transliterated to their ASCII base letter where possible (`é` becomes `e`). Characters with no ASCII equivalent, such as `ß` or CJK characters, are dropped.

**Parameters**

- `text` (`str`): The text to convert.
- `sep` (`str`, default `"-"`): The string placed between words.

**Returns** `str`. An empty string if no ASCII letters or digits survive.

```python
>>> slugify("Héllo, Wörld! 2024")
'hello-world-2024'
>>> slugify("Hello World", sep="_")
'hello_world'
>>> slugify("日本語")
''
```

---

## truncate

```python
truncate(text, width, ellipsis="…")
```

Cut `text` to at most `width` characters, including the ellipsis. The cut can fall in the middle of a word. Text that already fits within `width` is returned unchanged, with no ellipsis added.

**Parameters**

- `text` (`str`): The text to cut.
- `width` (`int`): The maximum length of the result, ellipsis included.
- `ellipsis` (`str`, default `"…"`): The marker appended when text is cut.

**Returns** `str`.

**Raises** `ValueError` if `width` is less than `len(ellipsis)`.

```python
>>> truncate("The quick brown fox", 10)
'The quick…'
>>> truncate("The quick brown fox", 10, ellipsis="...")
'The qui...'
>>> truncate("short", 10)
'short'
```

To avoid cutting mid-word, use [`shorten`](#shorten).

---

## shorten

```python
shorten(text, width, placeholder=" […]")
```

Cut `text` at a word boundary so that the result, placeholder included, fits within `width`. Runs of whitespace in `text` are collapsed to single spaces. If the whole text fits, it is returned with collapsed whitespace and no placeholder.

**Parameters**

- `text` (`str`): The text to cut.
- `width` (`int`): The maximum length of the result.
- `placeholder` (`str`, default `" […]"`): The marker appended when text is cut.

**Returns** `str`. If not even the first word fits, only the placeholder is returned, with surrounding whitespace stripped. In that case the result can be longer than `width` if `width` is smaller than the stripped placeholder.

```python
>>> shorten("The quick brown fox jumps", 16)
'The quick […]'
>>> shorten("  hi   there ", 20)
'hi there'
>>> shorten("extraordinary words", 6)
'[…]'
```

---

## dedupe_lines

```python
dedupe_lines(lines)
```

Yield each line from `lines` in order, skipping any line already seen. This is a generator, so nothing is read until you iterate it.

Comparison is exact: it is case-sensitive and whitespace-sensitive, so `"a"`, `"A"` and `"a "` are all distinct.

**Parameters**

- `lines` (iterable of `str`): The lines to filter, such as an open file.

**Yields** `str`: the first occurrence of each distinct line.

**Memory:** every distinct line is kept in memory until iteration finishes.

```python
>>> list(dedupe_lines(["a", "b", "a", "A"]))
['a', 'b', 'A']
```

---

## natural_sort

```python
natural_sort(items)
```

Return a new list of `items` in natural order, where runs of digits compare by numeric value, so `"file9"` sorts before `"file10"`. Letters compare case-insensitively. The input is not modified.

**Parameters**

- `items` (iterable of `str`): The strings to sort.

**Returns** `list`.

```python
>>> natural_sort(["file10", "file9", "File1"])
['File1', 'file9', 'file10']
```

---

## make_slug

```python
make_slug(text)
```

> **Deprecated since 0.8.** Use [`slugify`](#slugify) instead.

Emits a `DeprecationWarning` and returns `slugify(text, sep="_")`. Note the underscore separator, which differs from `slugify`'s default hyphen.

**Migrating**

```python
# Before
make_slug("Hello World")             # 'hello_world'

# After
slugify("Hello World", sep="_")      # 'hello_world'
```
