I wrote the how-to, but I couldn't run the Flask code. Installing Flask needed approval that wasn't granted, so the Flask view and the tests in the guide are unrun.

I did run `hookshot.verify` and `hookshot.sign` directly against the real `hookshot.py`. That covered a valid signature, a wrong secret, a tampered body, an old timestamp, a re-serialized body, a garbage header and an empty header. The prose and the troubleshooting table match those results. Please run the two listings once in a Flask environment before publishing.

The guide is at `outputs/verify-webhook-signatures-flask.md`. It covers:
- **How signing works:** a short explanation of webhooks and HMAC for new readers.
- **The Flask view:** the main listing.
- **Tests:** built on `hookshot.sign`.
- **Switching from hand-rolled HMAC:** the typical hand-rolled check with its gaps marked, then what `verify` does written out, then three migration steps.
- **Limits:** what a passing check doesn't guarantee.
- **Troubleshooting:** a table of errors, causes and fixes.

Running `verify` turned up two ways to get a 500 instead of a 400, and the guide handles both:
- **Missing header:** `request.headers.get("Hookshot-Signature")` returns `None`, and `verify` then raises `AttributeError`. The example passes `""` as the default, so a missing header becomes `SignatureError`.
- **Non-ASCII header:** a non-ASCII value in `v1` makes `verify` raise `TypeError`. The example rejects those with an `isascii()` check.

Calls I made that you may want to change:
- **No version number in the prose:** since the docs are built per release, I left it out. I also didn't invent links to other pages. The guide points readers to `help(hookshot.verify)` for the full detail.
- **One 400 for every failure:** the view returns 400 and no detail to the caller.
- **Replay and clock limits stated:** the guide says a captured delivery is accepted again within the 300-second default window. It tells readers to dedupe by event ID if double handling is harmful, and says `verify` doesn't do that. It also says `tolerance=0` turns the age check off.
- **Event ID:** I referred to "the event identifier from the payload" generically, because I couldn't confirm what field hookshot senders use.
- **`get_json()` after `get_data()`:** the guide says `request.get_json()` still works after `request.get_data()`. I believe that's right for Flask but didn't run it.