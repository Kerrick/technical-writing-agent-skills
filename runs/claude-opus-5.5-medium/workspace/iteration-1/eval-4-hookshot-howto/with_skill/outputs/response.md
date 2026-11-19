I wrote the how-to guide and saved it as `outputs/verify-webhook-signatures.md`. I couldn't run the Flask code: Flask and pytest aren't installed here, and installing them needed permission I didn't have. So `app.py` and `test_webhooks.py` were written against Flask's documented API but never executed.

**What I did run:** every hookshot call the guide relies on, in plain Python against your `hookshot.py` 3.4.0. That covers each error message, the rotation helper, the crashes in the hand-rolled example, and the JSON round-trip example. All of them behaved exactly as the page says.

**What I found in the library:**
- **Missing header crashes it.** If the header is missing and you pass `None` (which Flask's `request.headers.get()` gives you), `verify` raises `AttributeError`, not `SignatureError`, so Flask returns a 500. The guide passes `""` instead and explains why.
- **Text body crashes it.** `request.get_data(as_text=True)` passes a `str`, and `verify` raises `TypeError`.

**How the page is organized:**
- **For readers new to webhooks:** prerequisites and terms, then a short section on how a delivery gets checked, including what each of the three error messages means. Then four steps: install, store the secret, add the endpoint, and test it using `hookshot.sign`.
- **For everyone:** a table of ways to read the request body in Flask, with the wrong ones labeled. It has a side-by-side example of the most common mistake, re-serializing the JSON before verifying.
- **For readers switching from their own HMAC code:** a labeled "don't copy this" example of a typical hand-rolled check and its three flaws: a comparison that leaks timing, no protection against replayed deliveries, and a crash on bad headers. A table then maps each of their steps to hookshot. There's a warning against setting `tolerance=0` to get their old behavior back.
- **Optional aside:** accepting two secrets while the sender rotates to a new one, since `verify` only checks one secret per call.
- **Closing section:** what hookshot doesn't do, such as catching duplicate deliveries or reading the header from the request for you.

**Choices I made that you may want to check:**
- **Install name:** I wrote `python -m pip install hookshot` with no version pin, because your docs are built per release. I assumed the package name on PyPI matches the module name.
- **Python version:** the page says Python 3.10 or later. hookshot's `int | None` type hint fails to import on 3.9 or earlier.
- **Status codes:** I picked the route `/webhooks/billing`, a `HOOKSHOT_SECRET` environment variable, 400 for rejected deliveries and 204 for accepted ones. hookshot doesn't prescribe any of these.
- **Links:** the only external link is Flask's installation guide. I didn't link to a hookshot reference page because I don't know its URL. The page tells readers to search for `hookshot.verify` instead.

To check the Flask parts, install Flask and pytest, put `app.py`, `test_webhooks.py` and `hookshot.py` in one folder, and run `python -m pytest test_webhooks.py`.