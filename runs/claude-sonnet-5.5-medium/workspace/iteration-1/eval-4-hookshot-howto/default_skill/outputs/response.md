I wrote the guide, but I couldn't run the Flask parts. Flask wasn't installed, and the sandbox blocked the `pip install`. Please run `app.py` and `test_app.py` from the guide once in a Flask environment before publishing.

I did run the hookshot behavior against `hookshot.py`:
- **Valid and rejected deliveries:** `sign` followed by `verify` works. A re-serialized body, an old timestamp, a wrong secret, and a malformed or empty header each fail with the `SignatureError` message the guide gives.
- **Hand-written equivalent:** the HMAC check the guide shows for readers who roll their own produces the same digest as `verify`.
- **`tolerance=0`:** it turns the age check off, as the guide warns.

The guide has:
- **Scope and terms:** a short list of what hookshot does and doesn't do, plus a terms table and a skippable aside on why signatures matter, for readers new to webhooks.
- **The Flask route and its test:** the route reads the body with `request.get_data()`, then a pytest file built on `sign`.
- **The re-serialized-body trap:** the wrong form (`json.dumps` of parsed JSON) is shown next to the right one, labeled and marked inside the code block.
- **Switching from a hand-rolled check:** a side-by-side of the failure cases, and a warning that `verify` returns `None` on success.
- **Tolerance, replays and rotation:** a tolerance section with reasoning, a note that replays inside the window still pass, and a two-secret rotation pattern.

The docs are built per release, so the install line is unpinned and no version number appears in the prose. The guide is in `outputs/verify-webhook-signatures-with-hookshot.md`.

Calls I made that you may want to change:
- **Package name:** I wrote `pip install hookshot` from the module name, since nothing in the source confirms the PyPI name. Please check it.
- **Status code:** the route returns 400 on failure. The library doesn't dictate a status.
- **Event payload:** the example uses `event["type"]` and `event["invoice_id"]`. Those are my own example fields, not something hookshot defines.
- **Rotation snippet:** it is my own pattern built on `verify`, not a hookshot feature.
- **Python version:** I stated 3.10 or later, because `int | None` in the signatures needs it.

**Library bug:** `verify` raises `TypeError`, not `SignatureError`, when the `v1` value contains non-ASCII characters. I reproduced it with `hmac.compare_digest` on a `str`. In the guide's route that returns a 500 instead of a 400. The request is still rejected, but you may want to fix it in the library. I left it out of the guide so I didn't document a bug as intended behavior.