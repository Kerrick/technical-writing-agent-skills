I wrote the reference page at `outputs/textkit-api-reference.md`. It covers textkit 0.9.2, the version in the source file.

It documents all six public functions with the same sections in the same order: signature, one-line description, parameters, return value, errors, and an example. To keep it short, there's no intro or summary. The top of the page has an index of the functions and one sentence on when to use `truncate` and when to use `shorten`. I ran every example against `textkit.py`, and each output on the page is pasted from the real run.

Some behaviour isn't obvious from the docstrings, so I wrote it out on the page:
- **`make_slug` vs `slugify`:** `make_slug` separates words with `_`, not `-`. Replacing it with plain `slugify(text)` changes the output, so the migration note says to use `slugify(text, sep="_")`.
- **`shorten` can exceed `width`:** if `width` is smaller than the placeholder, it still returns `"[…]"`. For example, `shorten("abc def", 2)` returns `'[…]'`, which is 3 characters.
- **`slugify` drops some letters:** characters with no ASCII equivalent are removed, so `"Straße"` becomes `"strae"`.
- **`dedupe_lines` returns a generator:** for lines read from a file, the trailing `\n` counts in the comparison.
- **`natural_sort` needs strings:** it raises `TypeError` for anything else, and items that compare equal stay in their original order.

Three things to check or add before it goes up:
1. **Removal version for `make_slug`:** I couldn't find it, so the page has a `TODO(verify)` marker there.
2. **"Since" versions:** I left these out because I had no changelog to confirm when each function was added. Add them if you have that history.
3. **Links:** I didn't link to the 0.9 user guide because I don't know its URL. The links within the page point to anchors in GitHub's heading style (like `#slugifytext-sep-`). If your docs site builds anchors differently, check those links.