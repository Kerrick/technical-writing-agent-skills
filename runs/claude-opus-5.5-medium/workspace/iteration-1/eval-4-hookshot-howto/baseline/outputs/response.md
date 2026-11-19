I wrote the how-to guide you asked for, plus two short companion pages. Your two kinds of reader need different pages: newcomers need the background, and people with their own HMAC code need to know what changes when they switch. The Flask examples have not been run, because installing Flask was blocked here.

**Files in `outputs/`:**
- **`verify-webhook-signatures.md`** is the guide itself: steps for the Flask view, the `tolerance` setting, a check with `curl`, a pytest test file, and a troubleshooting section for each of the three error messages.
- **`replace-hand-rolled-hmac-check.md`** is for readers who already check signatures themselves. It has a table to confirm their code uses the same scheme, a diff from their own check to `hookshot.verify()`, the new replay check, how to switch test setup to `hookshot.sign()`, and how to undo the change.
- **`how-webhook-signatures-work.md`** is a background page for newcomers. It walks one delivery through signing and checking, and explains why the raw body and the timestamp matter. The other two pages link to it instead of explaining it inline.

All three pages describe 3.4.0 without "new in" or "as of" notes, since each version of your site matches its release. The Flask and Python versions they name are only what this code needs.

**What I checked in hookshot 3.4.0:**
- Every error message, the 300-second default, and that the timestamp check rejects timestamps in the future as well as the past.
- That `tolerance=0` turns the age check off.
- That re-serialized JSON fails with `signature mismatch`.
- That a header with a space after the comma is "malformed".
- Every header and digest shown on the pages.

**Two behaviours your users could hit:**
- **Missing header:** if the header isn't sent, `request.headers.get()` returns `None`. `verify()` then raises `AttributeError` instead of `SignatureError`, so Flask returns a 500 error. The guide defaults the header to `""` to avoid this. You may want to fix it in the library.
- **Bytes secret:** a secret passed as `bytes` also raises `AttributeError`. The guide tells readers to pass it as a `str`.

**Left as `TODO(verify)` in the pages:**
- **Install command:** the package name and index for `pip install hookshot==3.4.0`. I only had the module file.
- **Signing secret:** where users get it.
- **Flask parts:** the `curl` responses and the pytest file. Install Flask, run them, and paste the real status lines.