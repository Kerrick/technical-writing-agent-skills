I wrote the guide, but the Flask code in it never ran, because Flask isn't installed here and I wasn't allowed to install it. The guide is at `outputs/verify-webhook-signatures-flask.md`.

**Who it's for.** I assumed the reader is a Flask developer who knows Python and HTTP. Beginners get a short paragraph at the top explaining what a webhook is and why signatures matter. Readers who already write their own HMAC check get a section on replacing it, with a table of what `verify()` adds: replay protection, constant-time comparison and clear errors.

**What I ran.** I ran `hookshot.py` directly: `sign()` followed by `verify()`, a tampered body, an old timestamp, a malformed header, an empty header, a wrong secret and `tolerance=0`. The error messages in the troubleshooting table come from those runs.

**Bug in `hookshot.py` 3.4.0.** `verify()` raises `AttributeError`, not `SignatureError`, when the header is `None`. That happens when Flask's `request.headers.get("Hookshot-Signature")` finds no header. A route that only catches `SignatureError` would return a 500 instead of a rejection. The guide works around it with `headers.get(..., "")`. You may want to fix this in the library so the workaround isn't needed.

**What I did not run:**
- **Flask code:** the route sample, the pytest sample and the `curl` check are unrun. The expected 400 and 204 responses come from reading the code, not from a run.
- **Install command:** I left it out because I couldn't confirm the package name on PyPI. The prerequisites only say the module must be installed. Add the real command.
- **Hand-written HMAC sample:** it is my own example of a typical check, not your users' code.

**Per-release docs.** The guide has no hard-coded version number. The one version claim, that the `AttributeError` was confirmed against 3.4.0, is a place to check when the library changes. Since the docs are built per release, you could inject the version at build time. The guide also has no links to a hookshot API reference, because I don't know where it lives.