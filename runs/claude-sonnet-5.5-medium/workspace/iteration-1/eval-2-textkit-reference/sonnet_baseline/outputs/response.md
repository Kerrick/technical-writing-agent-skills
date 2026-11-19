I wrote the API reference page for textkit 0.9.2 and saved it to `outputs/textkit-api-reference.md`.

I assumed the reader is a Python developer who already uses textkit and wants one exact fact fast. So the page is reference only. Each function gets the same short template: signature, parameter table, return value, edge cases and one example. The functions are in alphabetical order, with a summary table at the top. `make_slug` comes last with its deprecation note and the replacement call.

**What I ran:** I called every function in Python with ordinary and edge-case inputs. Every example output on the page is real output, and I checked the edge-case claims the same way.

**Where the docstrings and the code disagree:** I documented what the code does.
- **`slugify`:** the docstring says "transliterated where possible". The code only strips accents (`é` becomes `e`). `ß` and `Æ` are dropped, so `"Straße Æon"` becomes `"strae-on"`. CJK text is removed entirely.
- **`shorten`:** the result can be longer than `width` when `width` is smaller than the placeholder. `shorten(text, 0)` returns `"[…]"`. It also collapses whitespace even when nothing is cut. You may want to treat the overlong result as a bug. If you fix it, update that note.

**What I couldn't verify:**
- **User-guide link:** the link at the top (`./user-guide.md`) is a guess. Point it at the real 0.9 guide URL.
- **`make_slug` removal:** the source gives no removal version, so the page says none has been announced.
- **Drift check:** the parameter tables are hand-written. After any change to `textkit.py`, check them against the signatures again.