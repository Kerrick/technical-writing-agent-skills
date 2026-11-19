<!--
Reader: a Flask developer who already verifies Hookshot-Signature headers with their own
hmac/hashlib code and wants to switch to the library. They know HMAC and their existing code;
they need to know what changes in behavior and how to swap safely. Documented against hookshot 3.4.0.
-->

# Replace a hand-rolled HMAC check with hookshot

Swap your own `hmac` code for `hookshot.verify()`, and keep accepting the same deliveries. hookshot also adds a replay check your code may not have.

If you don't have a signature check yet, follow [Verify webhook signatures with hookshot](verify-webhook-signatures.md) instead.

## Before you begin

- Python 3.10 or later.
- hookshot 3.4.0:

  ```bash
  pip install hookshot==3.4.0
  ```

  TODO(verify): the published package name and index.

- Tests that cover your webhook route, or a way to send it a signed delivery. See the Verify section of [Verify webhook signatures with hookshot](verify-webhook-signatures.md#verify).

## Steps

1. Check that your code verifies the same scheme hookshot does. `hookshot.verify()` expects:

   | Part | Value |
   | - | - |
   | Header | `Hookshot-Signature: t=<unix seconds>,v1=<hex digest>` |
   | Signed message | the bytes of `f"{t}."` followed by the raw request body |
   | Algorithm | HMAC-SHA256, hex-encoded lowercase digest |
   | Key | the signing secret, as a `str` encoded with UTF-8 |

   If your code signs a different message (for example, the body without the `t.` prefix) or reads a different header, your sender uses a different scheme and hookshot won't accept its deliveries. Stop here.

2. Replace your check with `hookshot.verify()`, and catch `hookshot.SignatureError`. A typical change looks like this:

   ```diff
    # app.py
   -import hashlib
   -import hmac
    import json
    import os

    from flask import Flask, abort, request

   +import hookshot
   +
    app = Flask(__name__)
    WEBHOOK_SECRET = os.environ["HOOKSHOT_SECRET"]


   -def signature_is_valid(raw_body, header, secret):
   -    parts = dict(p.split("=", 1) for p in header.split(","))
   -    signed = parts["t"].encode() + b"." + raw_body
   -    expected = hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()
   -    return hmac.compare_digest(expected, parts["v1"])
   -
   -
    @app.route("/webhooks", methods=["POST"])
    def receive_webhook():
        raw_body = request.get_data()
        header = request.headers.get("Hookshot-Signature", "")
   -    if not signature_is_valid(raw_body, header, WEBHOOK_SECRET):
   +
   +    try:
   +        hookshot.verify(raw_body, header, WEBHOOK_SECRET)
   +    except hookshot.SignatureError as error:
   +        app.logger.warning("Rejected webhook: %s", error)
            abort(400)

        event = json.loads(raw_body)
   ```

   Keep these from your existing code:

   - **Pass the raw body as `bytes`.** Keep using `request.get_data()`.
   - **Pass the header as a `str`, never `None`.** With a missing header, `None` raises `AttributeError` from `verify()`, and `""` raises `SignatureError`.
   - **Pass the secret as a `str`.** If your code holds it as `bytes`, decode it first; a `bytes` secret raises `AttributeError`.

   `verify()` raises `SignatureError` for header parse errors too. If your old code caught `KeyError` or `ValueError` around the parse, you can remove that handling.

3. Choose a replay window. `verify()` rejects deliveries whose `t=` timestamp is more than `tolerance` seconds before or after your server's clock, and `tolerance` defaults to `300`.

   - If your code already had an age check, pass its limit, in seconds: `hookshot.verify(raw_body, header, WEBHOOK_SECRET, tolerance=600)`.
   - If your code had no age check, keep the default. Check that your server clock is synced with NTP first. Otherwise, valid deliveries start failing with `timestamp outside tolerance` after you deploy.

   > **Warning:** `tolerance=0` turns off the age check and leaves the route open to replayed deliveries. Use it only to match old behavior while you fix a clock problem, and remove it afterward.

4. Replace test fixtures that compute signatures by hand with `hookshot.sign()`. It returns a complete header value:

   ```python
   BODY = b'{"id": "evt_1042", "type": "invoice.paid"}'
   header = hookshot.sign(BODY, "test-secret")
   ```

   The value has the current time in `t=`, for example:

   ```text
   t=1795065434,v1=09ee5b83ad2338c98f9f30ba312dfdaed7ccb73e10887ce0f273220e9ea4676a
   ```

   To test the replay window, pass a fixed `timestamp`:

   ```python
   import time

   stale = hookshot.sign(BODY, "test-secret", timestamp=int(time.time()) - 301)
   ```

5. Delete your old signature helper and any `hmac`/`hashlib` imports that only it used.

## Verify

1. Run your webhook tests. A signed delivery returns your success status, and a tampered body, a wrong secret, a missing header, and a stale timestamp all return `400`.
2. After you deploy, watch your logs for `Rejected webhook:`. These three messages can appear:

   - `signature mismatch`: the body or secret differs from what the sender signed. Your old code would have rejected these too.
   - `malformed Hookshot-Signature header`: the header is missing or isn't in `t=…,v1=…` form.
   - `timestamp outside tolerance`: new if your old code had no age check. Check your server clock before raising `tolerance`.

## Undo

Revert the change to your webhook route and redeploy. hookshot keeps no state, so nothing else needs rolling back.

## Related

- [Verify webhook signatures with hookshot](verify-webhook-signatures.md): the full Flask setup, plus troubleshooting for each `SignatureError` message.
- [How webhook signatures work](how-webhook-signatures-work.md)
