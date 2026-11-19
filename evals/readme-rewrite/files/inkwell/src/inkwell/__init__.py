from markdown_it import MarkdownIt

__all__ = ["render", "export_pdf"]

_md = MarkdownIt()


def render(markdown: str, title: str = "Document") -> str:
    """Return a complete HTML page for `markdown`, with `title` in its <title>."""
    body = _md.render(markdown)
    return f"<!doctype html><html><head><title>{title}</title></head><body>{body}</body></html>"


def export_pdf(markdown: str, path: str) -> None:
    """Planned: write `markdown` to a PDF at `path`."""
    raise NotImplementedError("PDF export isn't available yet")
