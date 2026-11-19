# textkit API reference

Functions in the `textkit` module, version 0.9.2. All of them take and return `str` values unless noted.

```python
import textkit
```

- Slugs: [`slugify`](#slugifytext-sep-), [`make_slug`](#make_slugtext) (deprecated)
- Shortening: [`truncate`](#truncatetext-width-ellipsis), [`shorten`](#shortentext-width-placeholder-)
- Lists of strings: [`dedupe_lines`](#dedupe_lineslines), [`natural_sort`](#natural_sortitems)

To pick between `truncate` and `shorten`: `truncate` cuts at an exact character count and may split a word; `shorten` cuts between words and collapses whitespace.

## `slugify(text, sep="-")`

Returns a lowercase ASCII slug made of the letters and digits in `text`, joined by `sep`.

**Parameters**
- `text` (str): the text to convert.
- `sep` (str): placed between words. Defaults to `"-"`.

**Returns** a `str`. Accented letters are transliterated to ASCII (`é` becomes `e`). Characters with no ASCII equivalent are dropped, so `"Straße"` becomes `"strae"`. Returns `""` if no letters or digits remain, for example for `"東京"`.

**Raises** nothing.

**Example**

```python
textkit.slugify("Crème Brûlée Recipes!")
textkit.slugify("Crème Brûlée Recipes!", sep="_")
```

```text
'creme-brulee-recipes'
'creme_brulee_recipes'
```

## `make_slug(text)`

**Deprecated since 0.8.** Use [`slugify`](#slugifytext-sep-) instead. TODO(verify): version in which `make_slug` will be removed.

Returns `slugify(text, sep="_")` and emits a `DeprecationWarning`: `make_slug is deprecated; use slugify`.

To migrate, replace `make_slug(text)` with `slugify(text, sep="_")`. Plain `slugify(text)` uses `-` as the separator, so it returns a different string.

## `truncate(text, width, ellipsis="…")`

Returns `text` cut to at most `width` characters, counting the ellipsis. May cut in the middle of a word.

**Parameters**
- `text` (str): the text to cut.
- `width` (int): maximum length of the result, including `ellipsis`. Must be at least `len(ellipsis)`.
- `ellipsis` (str): appended when `text` is cut. Defaults to `"…"` (one character, U+2026).

**Returns** a `str`. If `len(text) <= width`, returns `text` unchanged, with no ellipsis.

**Raises** `ValueError: width must be at least len(ellipsis)` when `width < len(ellipsis)`.

**Example**

```python
textkit.truncate("Quarterly invoice summary", 12)
textkit.truncate("Quarterly invoice summary", 12, ellipsis="...")
textkit.truncate("Invoice", 12)
```

```text
'Quarterly i…'
'Quarterly...'
'Invoice'
```

## `shorten(text, width, placeholder=" […]")`

Returns `text` cut between words so that it fits in `width` characters, with `placeholder` appended. Runs of whitespace, including newlines, are collapsed to single spaces.

**Parameters**
- `text` (str): the text to shorten.
- `width` (int): maximum length of the result, including `placeholder`.
- `placeholder` (str): appended when words are removed. Defaults to `" […]"`, with a leading space.

**Returns** a `str`:
- If the whitespace-collapsed text fits in `width`, returns it with no placeholder.
- If the first word doesn't fit alongside `placeholder`, returns `placeholder` with surrounding whitespace stripped (`"[…]"` by default). This result can be longer than `width` when `width` is smaller than the stripped placeholder.

**Raises** nothing.

**Example**

```python
textkit.shorten("Quarterly   invoice summary for March", 25)
textkit.shorten("Quarterly   invoice\nsummary", 40)
textkit.shorten("Supercalifragilistic expialidocious", 10)
```

```text
'Quarterly invoice […]'
'Quarterly invoice summary'
'[…]'
```

## `dedupe_lines(lines)`

Yields each item of `lines` in its original order, skipping any that appeared earlier.

**Parameters**
- `lines` (iterable of str): the lines to filter. Can be any iterable, including an open file.

**Returns** a generator. Wrap it in `list()` if you need a list.

Comparison is exact: `"paid"`, `"Paid"`, and `"paid "` are three different lines. Lines read from a file keep their trailing `"\n"`, so a final line without one doesn't match an earlier copy that has one. Every distinct line is kept in memory until the generator is exhausted.

**Raises** nothing.

**Example**

```python
list(textkit.dedupe_lines(["paid", "Paid", "paid", "paid "]))
```

```text
['paid', 'Paid', 'paid ']
```

## `natural_sort(items)`

Returns a new list of `items` sorted with runs of digits compared as numbers, so `"invoice10"` comes after `"invoice9"`. Comparison ignores case.

**Parameters**
- `items` (iterable of str): the strings to sort. Not modified.

**Returns** a new `list`. Strings that compare equal, such as `"file7"` and `"File7"`, or `"file007"` and `"file7"`, keep their input order.

**Raises** `TypeError` if any item isn't a string.

**Example**

```python
invoices = ["invoice10.pdf", "Invoice9.pdf", "invoice1.pdf"]
textkit.natural_sort(invoices)
```

```text
['invoice1.pdf', 'Invoice9.pdf', 'invoice10.pdf']
```
