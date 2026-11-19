I wrote the API reference page: `outputs/textkit-api-reference.md`.

It opens with a one-line summary table. Each function then gets its signature, a parameter table, the edge cases that matter, and a short example. I ran every example against `textkit.py`, and the outputs shown are what the code actually returns. The deprecated `make_slug` is at the end.

Some of what's documented is behaviour the docstrings don't fully spell out, and you might want to look at it:

- **`shorten` can return something longer than `width`.** If the first word doesn't fit, it returns `"[…]"`, which is 3 characters even when `width` is 2. The page says so; you may decide it's a bug.
- **`shorten` always collapses whitespace,** even when nothing is cut: `"  a   b  "` comes back as `"a b"`.
- **`truncate` raises `ValueError` whenever `width < len(ellipsis)`,** even when the text would have fit.
- **`make_slug` joins words with `_`, but `slugify` defaults to `-`.** So simply swapping one call for the other changes existing slugs. The migration note says to use `sep="_"`.

The source says the version is `0.9.2` (`__version__`), so that's what the page header uses. If the site labels everything "0.9", change that line to match.