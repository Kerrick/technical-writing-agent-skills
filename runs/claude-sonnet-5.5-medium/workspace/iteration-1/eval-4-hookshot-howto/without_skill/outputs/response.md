I wrote the guide, but I haven't run any of its code. The sandbox blocked every Python run, so the Flask route and the tests are checked only by reading `hookshot.py`. Run the test block once before publishing.

The guide is at `outputs/verify-webhook-signatures-flask.md`. It covers:

- **Background:** a short section on what a webhook signature is, which readers who already hand-roll HMAC checks can skip.
- **Steps:**
  - Store the secret in an environment variable.
  - Install with `pip install hookshot==3.4.0`.
  - Add a Flask route that verifies `request.get_data()` and returns 400 on `SignatureError`.
  - Write pytest tests using `hookshot.sign()`.
- **Pitfalls:** it explains that `verify()` raises on failure and never returns `False`, and that you must verify the raw bytes rather than re-serialized JSON.
- **Replay window:** how to change `tolerance` (default 300 seconds) and why you shouldn't set it to 0.
- **Switching from hand-rolled HMAC:** a side-by-side table of what `verify()` does against a typical custom check, plus migration steps.
- **Troubleshooting:** a table of the three error messages.

- **Pinned version:** since your docs are built per release, the guide is pinned to 3.4.0. It doesn't say "latest" or point to other versions.
- **Tool-specific details:**
  - I added Python 3.10 or later as a requirement, because `sign()` uses `int | None` in its signature.
  - I added Flask 2.0 or later, because the example uses `@app.post`.
  - The claim that a header missing from the request leads to a `SignatureError` comes from reading the code.
- **Scratch files:** I left a scratch folder, `scratch/`, in the working directory with a draft app and test. It isn't part of the deliverable, so delete it.