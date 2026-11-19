# inkwell

Turn Markdown into a complete, standalone HTML page with a single function call.

```python
from inkwell import render

html = render("# Hello\n\nThis is *inkwell*.", title="Greeting")
```

```html
<!doctype html><html><head><title>Greeting</title></head><body><h1>Hello</h1>
<p>This is <em>inkwell</em>.</p>
</body></html>
```

inkwell parses CommonMark with [markdown-it-py](https://github.com/executablebooks/markdown-it-py) and wraps the result in a full HTML document, so you can write the output straight to a `.html` file and open it in a browser.

## Installation

The package is published on PyPI as `inkwell-md`, and you import it as `inkwell`:

```sh
pip install inkwell-md
```

You need Python 3.10 or newer.

## Usage

### `render(markdown, title="Document")`

`render` returns the full HTML page as a string. Its `title` argument becomes the page's `<title>` and defaults to `"Document"`.

```python
from pathlib import Path
from inkwell import render

source = Path("notes.md").read_text(encoding="utf-8")
Path("notes.html").write_text(render(source, title="My Notes"), encoding="utf-8")
```

#### Untrusted input

inkwell does not sanitize anything:

- Raw HTML in the Markdown is passed through to the output unchanged, which is standard CommonMark behavior.
- `title` goes into the page as-is, with no escaping.

If the Markdown or the title could come from an untrusted source, sanitize the output (for example with [nh3](https://pypi.org/project/nh3/)) and escape the title with `html.escape` before you call `render`.

### `export_pdf(markdown, path)` (not available yet)

`export_pdf` is a placeholder for planned PDF export. At the moment it raises `NotImplementedError` every time you call it.

## License

inkwell is licensed under the [Apache License 2.0](LICENSE).
