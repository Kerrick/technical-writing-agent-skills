I wrote `evals/readme-rewrite/files/inkwell/README.md`. I couldn't run the example because the command needed approval. The output it shows is what markdown-it-py should produce, but I haven't checked it.

The README covers:
- A short code example with its output.
- Installation. The PyPI name is `inkwell-md` but you import `inkwell`, so I said that up front. It also says you need Python 3.10 or newer.
- `render`: what it takes and returns, plus an example that converts a file.
- `export_pdf`: marked as not available yet, since it always raises `NotImplementedError`.
- The Apache 2.0 license.

A few things to look at before you publish:

1. **`docs/demo.png` isn't an image.** It's a text file that just says "placeholder for a screenshot." I left it out of the README so the PyPI page doesn't show a broken image. Add a real screenshot first if you want one.
2. **The tagline claims more than the code does.** `pyproject.toml` says "tidy, self-contained HTML," but `render` only wraps markdown-it's output in bare `<html>`/`<body>` tags. There's no CSS and no `<meta charset>`. I described what it actually does. You may want to change the description to match, or add the styling.
3. **Nothing is escaped or sanitized.** `title` goes into the page as-is, and markdown-it-py's default settings let raw HTML through. I put a short "Untrusted input" note in the README. Escaping `title` with `html.escape` inside `render` would fix the first part with one line.
4. **`export_pdf` is in `__all__`.** It's public even though it always raises an error, which is part of the 1.0.0 API. Consider leaving it out until it works.
5. **The repository URL is `github.com/example/inkwell`.** It looks like a placeholder, so I didn't link to it from the README.