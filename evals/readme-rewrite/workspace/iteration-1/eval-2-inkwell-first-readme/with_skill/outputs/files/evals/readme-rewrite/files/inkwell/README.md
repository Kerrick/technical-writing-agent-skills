# inkwell

[![PyPI](https://img.shields.io/pypi/v/inkwell-md)](https://pypi.org/project/inkwell-md/)
[![Python](https://img.shields.io/pypi/pyversions/inkwell-md)](https://pypi.org/project/inkwell-md/)
[![License](https://img.shields.io/pypi/l/inkwell-md)](https://github.com/example/inkwell/blob/main/LICENSE)

Turn a Markdown string into a complete HTML page with one function call.

inkwell is a Python library for scripts and apps that write Markdown and need a page they can save as an `.html` file or serve as is. You pass it Markdown and a title. It returns one string that holds the doctype, the `<head>` with your title, and the rendered body.

[markdown-it-py](https://github.com/executablebooks/markdown-it-py) does the Markdown parsing. Used directly, markdown-it-py returns an HTML fragment, and you write the page around it. inkwell writes that page for you. If you need options that inkwell doesn't expose, such as tables or plugins, use markdown-it-py directly. [Python-Markdown](https://python-markdown.github.io/) also returns fragments. [Pandoc](https://pandoc.org/) builds full pages with styles and converts to many formats, but it is a separate program to install, not a Python package.

## Example

This three-line script renders a heading and a sentence:

```python
import inkwell

html = inkwell.render("# Hello\n\nThis is *Markdown*.", title="Greeting")
print(html)
```

It prints:

```html
<!doctype html><html><head><title>Greeting</title></head><body><h1>Hello</h1>
<p>This is <em>Markdown</em>.</p>
</body></html>
```

## Compatibility

| Requirement | Version |
| - | - |
| Python | 3.10 or later |
| [markdown-it-py](https://github.com/executablebooks/markdown-it-py) | 3 or later (pip installs it for you) |

inkwell renders [CommonMark](https://commonmark.org/). It doesn't render GitHub extensions: tables, strikethrough (`~~text~~`), and bare URLs come out as plain text.

The page has no stylesheet and no `<meta charset>` tag. Images stay links to their files, so copy the images along with the page.

inkwell doesn't escape its input. HTML in your Markdown, and in `title`, goes into the page as written, `<script>` tags included. Don't pass it text from people you don't trust without sanitizing the result first, for example with [nh3](https://pypi.org/project/nh3/).

PDF export isn't available yet. `inkwell.export_pdf()` exists, but it raises `NotImplementedError`.

## Installation

```sh
pip install inkwell-md
```

The package on PyPI is `inkwell-md`. You import it as `inkwell`.

## Usage

Call `inkwell.render(markdown, title="Document")` with your Markdown as a string. It returns the HTML page as a string. `title` is optional. It sets the page's `<title>` and defaults to `Document`.

To turn a Markdown file into an HTML file, read the file, render it, and write the result:

```python
from pathlib import Path

import inkwell

source = Path("notes.md")
page = inkwell.render(source.read_text(encoding="utf-8"), title="My notes")
Path("notes.html").write_text(page, encoding="utf-8")
```

The page doesn't declare its encoding, so a browser that opens the file from disk can show accented letters and emoji wrongly. If your text has them, serve the page with a `charset=utf-8` content type, as below, or add a `<meta charset="utf-8">` tag to the string before you save it.

To serve the page from a web app, return the string from `render` as the response body, with the content type `text/html; charset=utf-8`.

## Reporting problems

Open an issue at [github.com/example/inkwell/issues](https://github.com/example/inkwell/issues). Include your Python version, the Markdown you passed in, the HTML you got, and the HTML you expected.

## License

inkwell is available under the [Apache License 2.0](https://github.com/example/inkwell/blob/main/LICENSE). You can use it in commercial and closed-source projects. If you redistribute inkwell itself, include its license and notices. The license covers inkwell, not the pages you make with it.
