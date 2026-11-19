# textkit API reference

This page documents textkit 0.9.2. Every function is defined in the top-level `textkit` module:

```python
from textkit import slugify, truncate, shorten, dedupe_lines, natural_sort
```

For step-by-step tasks, see the textkit 0.9 user guide. Examples on this page are Python REPL sessions: lines starting with `>>>` are what you type, and the line after each one is the result.

## Summary

| Function | Does | Example | Result |
|---|---|---|---|
| `slugify(text, sep="-")` | Lowercase ASCII slug from any text. | `slugify("Crème Brûlée & Co.")` | `'creme-brulee-co'` |
| `truncate(text, width, ellipsis="…")` | Cut to `width` characters, even mid-word. | `truncate("The quick brown fox", 12)` | `'The quick b…'` |
| `shorten(text, width, placeholder=" […]")` | Cut at a word boundary to fit in `width`. | `shorten("The quick brown fox", 12)` | `'The […]'` |
| `dedupe_lines(lines)` | Yield lines in order, skipping repeats. | `list(dedupe_lines(["a", "b", "a"]))` | `['a', 'b']` |
| `natural_sort(items)` | New list with numbers sorted by value. | `natural_sort(["file10", "file9"])` | `['file9', 'file10']` |
| `make_slug(text)` | Deprecated since 0.8. Use `slugify(text, sep="_")`. | `make_slug("Hello World")` | `'hello_world'` |

### `truncate` or `shorten`?

Both cut text to a width, and people often say "truncate" for either. They differ in where they cut:

| | `truncate` | `shorten` |
|---|---|---|
| Cuts | At exactly `width` characters, even mid-word | Only between words |
| Whitespace | Kept as is | Every run collapsed to one space |
| Marker | `"…"` | `" […]"` |
| Result can be longer than `width` | No | Yes, when `width` is under 3 (see **shorten**) |
| Too-small `width` | Raises `ValueError` | Returns `"[…]"` |
| Cost on large text | Constant: slices only what it keeps | Linear: splits all of `text` |

The same input, the same width:

```python
>>> truncate("The quick brown fox", 12)
'The quick b…'
>>> shorten("The quick brown fox", 12)
'The […]'
```

`shorten` keeps only `The` because `The quick […]` is 13 characters.

## slugify

```python
slugify(text, sep="-")
```

Returns a lowercase ASCII slug of `text`: each run of ASCII letters and digits becomes a word, and the words are joined with `sep`. Everything else, including spaces, punctuation, and leading or trailing separators, is dropped. Accented Latin letters lose their accents (`é` becomes `e`), and compatibility characters are expanded (the ligature `ﬁ` becomes `fi`). Letters with no ASCII decomposition, such as `ß`, `Æ`, `ø`, and all non-Latin scripts, are dropped.

- **`text`** (`str`): the text to slugify.
- **`sep`** (`str`): placed between words. May be `""`.
- **Returns** `str`. Returns `""` when no ASCII letter or digit survives, including for empty input.

Cost is linear in the length of `text`.

> **Warning: some titles produce an empty or colliding slug.**
> A title in a non-Latin script slugifies to `""`, and titles that differ only in dropped characters get the same slug. Don't use a slug as a unique key without checking for empty and duplicate values.
>
> ```python
> >>> slugify("Привет мир")
> ''
> >>> slugify("Ærø Øresund")
> 'r-resund'
> ```

### Examples

Turn an article title into a URL path segment:

```python
>>> slugify("Hello, World!")
'hello-world'
```

Accents are removed and the `&` is dropped:

```python
>>> slugify("Crème Brûlée & Co.")
'creme-brulee-co'
```

Use a different separator, for example for file names. Digits are kept, and the `.` in `0.9` splits them into separate words:

```python
>>> slugify("Release 0.9 notes", sep="_")
'release_0_9_notes'
```

Text that is already a slug comes back unchanged, minus stray separators:

```python
>>> slugify("  --already-a-slug--  ")
'already-a-slug'
```

## truncate

```python
truncate(text, width, ellipsis="…")
```

Returns `text` cut to at most `width` characters, counting the `ellipsis`. It cuts at exactly that position, even in the middle of a word. Text of `width` characters or fewer is returned unchanged, with no ellipsis.

- **`text`** (`str`): the text to cut.
- **`width`** (`int`): the maximum length of the result, in characters (Python `str` code points).
- **`ellipsis`** (`str`): appended when text is cut. May be `""`.
- **Returns** `str`.
- **Raises** `ValueError("width must be at least len(ellipsis)")` when `width < len(ellipsis)`. The check runs before the length check, so `truncate("", 0)` raises even though the empty string fits.

`truncate` copies only the characters it keeps, so its cost doesn't grow with the length of `text`.

> **Warning: `truncate` can strip an accent without an error.**
> `width` counts code points, not visible characters. In decomposed text (Unicode NFD, common from macOS file names and some keyboards), `é` is two code points, `e` plus a combining accent, and a cut between them drops the accent:
>
> ```python
> >>> import unicodedata
> >>> title = unicodedata.normalize("NFD", "Café menu")
> >>> truncate(title, 5)  # Wrong: the accent is cut off
> 'Cafe…'
> >>> truncate(unicodedata.normalize("NFC", title), 5)
> 'Café…'
> ```
>
> Normalize to NFC first. NFC doesn't help for characters with no precomposed form, such as many emoji sequences.

### Examples

Cut a title to fit a 10-character column:

```python
>>> truncate("Quarterly report", 10)
'Quarterly…'
```

Text that already fits is returned as is:

```python
>>> truncate("Quarterly report", 16)
'Quarterly report'
```

Use an ASCII ellipsis. Its three characters count toward `width`, leaving room for seven of the text:

```python
>>> truncate("Quarterly report", 10, ellipsis="...")
'Quarter...'
```

Cut with no marker at all:

```python
>>> truncate("Quarterly report", 9, ellipsis="")
'Quarterly'
```

## shorten

```python
shorten(text, width, placeholder=" […]")
```

Returns `text` cut at a word boundary to fit in `width` characters, counting the `placeholder`. Words are split on any whitespace, and every run of whitespace in the result becomes a single space, even when nothing is cut. If the collapsed text fits in `width`, it is returned without a placeholder. Otherwise `shorten` keeps as many leading words as fit and appends `placeholder`. If not even the first word fits, it returns `placeholder` with surrounding whitespace stripped: `"[…]"` by default.

- **`text`** (`str`): the text to cut.
- **`width`** (`int`): the maximum length of the result, in characters.
- **`placeholder`** (`str`): appended when text is cut.
- **Returns** `str`. Returns `""` for empty or all-whitespace `text`.

`shorten` splits all of `text` before it starts, so its cost and memory grow with the length of `text`, not with `width`. To show the start of a very large document, prefer `truncate`.

> **Warning: the result can be longer than `width`.**
> When not even the first word fits, `shorten` returns the stripped placeholder whatever `width` is. With the default placeholder, a `width` under 3 gives a 3-character result. Unlike `truncate`, `shorten` never raises for a small `width`.
>
> ```python
> >>> shorten("The quick brown fox", 2)
> '[…]'
> ```

> **Coming from `textwrap.shorten`?**
> The standard library's `textwrap.shorten` also collapses whitespace and cuts between words, and with the same placeholder it gives the same result as textkit's `shorten`. It differs at the edges: its default placeholder is `" [...]"` with ASCII dots, and it raises `ValueError` when the placeholder doesn't fit, where textkit returns `"[…]"`.

### Examples

Fit a headline into 15 characters:

```python
>>> shorten("The quick brown fox jumps", 15)
'The quick […]'
```

Whitespace is collapsed even when the text fits:

```python
>>> shorten("  The   quick\nfox ", 40)
'The quick fox'
```

A first word too long to fit leaves only the placeholder:

```python
>>> shorten("Supercalifragilistic", 10)
'[…]'
```

Use a shorter placeholder to keep one more word:

```python
>>> shorten("The quick brown fox jumps", 15, placeholder="...")
'The quick...'
```

## dedupe_lines

```python
dedupe_lines(lines)
```

Yields each item of `lines` in its original order, skipping any item equal to one already yielded. Comparison is exact: case, leading and trailing whitespace, and line endings all count.

- **`lines`** (iterable of `str`): a list, a file object, a generator, or any other iterable.
- **Returns** a generator. Nothing is read from `lines` until you iterate it, and it can be iterated only once. Wrap it in `list()` to get a list. An empty `lines` yields nothing.

`dedupe_lines` keeps every distinct line in memory until the generator is finished, so memory grows with the number of distinct lines, not the total number. It streams otherwise: it is safe on files larger than memory as long as their distinct lines fit.

### Examples

Remove repeated entries from a list of log messages. `"A"` and `"a "` are kept, because they differ from `"a"` in case and whitespace:

```python
>>> list(dedupe_lines(["a", "b", "a", "A", "a "]))
['a', 'b', 'A', 'a ']
```

Lines read from a file end in `"\n"`, except possibly the last one. That makes the last line distinct from an earlier copy of it:

```python
>>> list(dedupe_lines(["error\n", "warn\n", "error"]))  # Wrong: "error" appears twice
['error\n', 'warn\n', 'error']
>>> list(dedupe_lines(line.rstrip("\n") for line in ["error\n", "warn\n", "error"]))
['error', 'warn']
```

With a real file, strip each line the same way:

```python
with open("app.log", encoding="utf-8") as log:
    for line in dedupe_lines(line.rstrip("\n") for line in log):
        print(line)
```

Passing a single string iterates its characters, not its lines. Split it first:

```python
>>> list(dedupe_lines("error\nwarn\nerror"))  # Wrong: dedupes characters
['e', 'r', 'o', '\n', 'w', 'a', 'n']
>>> list(dedupe_lines("error\nwarn\nerror".splitlines()))
['error', 'warn']
```

## natural_sort

```python
natural_sort(items)
```

Returns a new list of `items` sorted so that runs of digits compare by numeric value: `"file9"` comes before `"file10"`. Text between the numbers compares case-insensitively. The sort is stable, so items that compare equal, such as `"File1"`, `"file1"`, and `"file01"`, keep their input order. `items` is not modified.

- **`items`** (iterable of `str`): a list, tuple, set, or any other iterable of strings.
- **Returns** `list`. An empty `items` gives `[]`.
- **Raises** `TypeError` if any item is not a string. Raises `ValueError` when superscript digits such as `²` follow a number or make up a whole item, as in `"10²"`. Superscripts after letters, as in `"m²"`, sort as text.

Like `sorted()`, `natural_sort` builds a full list and computes a key for every item, so memory and time grow with the number and length of items.

### Examples

Sort file names the way a person would:

```python
>>> natural_sort(["file10", "file9", "File1", "file1", "file01"])
['File1', 'file1', 'file01', 'file9', 'file10']
```

Sort version strings. Each dot-separated part compares as a number:

```python
>>> natural_sort(["v1.10", "v1.9", "v1.2"])
['v1.2', 'v1.9', 'v1.10']
```

Decimal numbers sort wrongly, because the part after the dot also compares as a whole number (`25` is greater than `5`). Minus signs are ignored. To sort numbers, convert them and use `sorted()`:

```python
>>> natural_sort(["1.5", "1.25"])  # Wrong: 1.5 sorts before 1.25
['1.5', '1.25']
>>> sorted(["1.5", "1.25"], key=float)
['1.25', '1.5']
```

## make_slug (deprecated)

```python
make_slug(text)
```

Deprecated since 0.8. It is exactly `slugify(text, sep="_")`, except that it also issues a `DeprecationWarning` with the message `make_slug is deprecated; use slugify`. Python shows `DeprecationWarning` by default only for calls made directly from `__main__`; test runners such as pytest also show it. Calls from inside your own modules print nothing unless you enable warnings, for example with `python -W default`.

To migrate, keep the underscore separator. A bare `slugify(text)` changes every slug, because its default separator is `-`:

```python
>>> make_slug("Hello World")  # Older form
'hello_world'
>>> slugify("Hello World", sep="_")
'hello_world'
>>> slugify("Hello World")  # Wrong replacement: the separator changes
'hello-world'
```
