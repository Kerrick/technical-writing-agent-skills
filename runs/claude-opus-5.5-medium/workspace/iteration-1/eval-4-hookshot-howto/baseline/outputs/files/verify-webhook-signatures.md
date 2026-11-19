<!--
Reader: a Flask developer who has a webhook endpoint (or is about to add one) and wants to
reject deliveries that weren't signed by the sender. They know Flask routing and Python
exceptions. They arrive from search or from the sidebar. Webhook newcomers are pointed to
the explanation page; readers replacing their own HMAC code are pointed to the migration guide.
Documented against hookshot 3.4.0.
-->

# Verify webhook signatures with hookshot

Check every webhook delivery's signature in your Flask view, and reject any delivery that wasn't signed with your secret or is too old.

New to webhook signatures? Read [How webhook signatures work](how-webhook-signatures-work.md) first. Already checking HMAC signatures with your own code? Follow [Replace a hand-rolled HMAC check with hookshot](replace-hand-rolled-hmac-check.md) instead.

## Before you begin

- Python 3.10 or later.
- A Flask app with a route that will receive webhooks.
- Your webhook signing secret. TODO(verify): where senders show or issue the signing secret (dashboard path, API, CLI).
- hookshot 3.4.0:

  ```bash
  pip install hookshot==3.4.0
  ```

  TODO(verify): the published package name and index. The source reviewed is the single module `hookshot.py`.

## Steps

1. Put the signing secret in an environment variable. Don't commit it to source control.

   ```bash
   export HOOKSHOT_SECRET="YOUR_SIGNING_SECRET"
   ```

   Replace `YOUR_SIGNING_SECRET` with your signing secret. Export it in the same shell you start Flask from.

2. In your Flask app, read the raw request body and the `Hookshot-Signature` header, and pass both to `hookshot.verify()`:

   ```python
   # app.py
   import json
   import os

   from flask import Flask, abort, request

   import hookshot

   app = Flask(__name__)
   WEBHOOK_SECRET = os.environ["HOOKSHOT_SECRET"]


   @app.route("/webhooks", methods=["POST"])
   def receive_webhook():
       raw_body = request.get_data()
       header = request.headers.get("Hookshot-Signature", "")

       try:
           hookshot.verify(raw_body, header, WEBHOOK_SECRET)
       except hookshot.SignatureError as error:
           app.logger.warning("Rejected webhook: %s", error)
           abort(400)

       event = json.loads(raw_body)
       app.logger.info("Received %s", event["type"])
       return "", 204
   ```

   `verify()` returns `None` when the signature is valid and raises `hookshot.SignatureError` when it isn't. Only work with the event after `verify()` returns.

   Three details in this view matter:

   - **Pass the exact bytes you received.** `request.get_data()` returns the body as bytes. If you pass `json.dumps(request.json).encode()` instead, the bytes usually differ from what the sender signed and every delivery fails with `signature mismatch`. Call `get_data()` before anything reads `request.form`, and parse the JSON from `raw_body` after verifying.
   - **Default the header to `""`.** If the header is missing, `request.headers.get("Hookshot-Signature")` returns `None`, and `verify()` raises `AttributeError` instead of `SignatureError`, so Flask responds with a 500. With the `""` default, a missing header raises `SignatureError("malformed Hookshot-Signature header")`.
   - **Pass the secret as a `str`.** `verify()` calls `secret.encode()`, so a `bytes` secret raises `AttributeError`.

3. If the default 5-minute replay window doesn't suit you, pass `tolerance` in seconds:

   ```python
   hookshot.verify(raw_body, header, WEBHOOK_SECRET, tolerance=600)
   ```

   `verify()` rejects any delivery whose timestamp is more than `tolerance` seconds before *or after* your server's clock. The default is `300`. Keep your server clock synced with NTP; clock drift beyond the tolerance rejects valid deliveries.

   > **Warning:** `tolerance=0` turns off the age check. An attacker who captures one signed delivery can then resend it whenever they like, and it will pass verification.

4. Restart your Flask server so it picks up the new code and the `HOOKSHOT_SECRET` variable.

   ```bash
   flask --app app run
   ```

## Verify

Send yourself a signed delivery, then a tampered one. Run these from the directory that contains `app.py`, in a second shell where `HOOKSHOT_SECRET` is exported with the same value.

1. Save a sample event body:

   ```bash
   printf '{"id": "evt_1042", "type": "invoice.paid"}' > event.json
   ```

2. Sign it with `hookshot.sign()`, which returns a `Hookshot-Signature` header value for the current time:

   ```bash
   HEADER=$(python -c 'import os, hookshot; print(hookshot.sign(open("event.json", "rb").read(), os.environ["HOOKSHOT_SECRET"]))')
   ```

3. Send the signed delivery. Use `--data-binary` so curl sends the file byte-for-byte:

   ```bash
   curl -i http://127.0.0.1:5000/webhooks \
     -H "Content-Type: application/json" \
     -H "Hookshot-Signature: $HEADER" \
     --data-binary @event.json
   ```

   The response status is `204`. TODO(verify): paste the actual status line. This command wasn't run against a live Flask server while writing this page.

4. Send a different body with the same header:

   ```bash
   curl -i http://127.0.0.1:5000/webhooks \
     -H "Content-Type: application/json" \
     -H "Hookshot-Signature: $HEADER" \
     --data-binary '{"id": "evt_1042", "type": "invoice.voided"}'
   ```

   The response status is `400`, and the Flask log shows `Rejected webhook: signature mismatch`.

To keep this check in your test suite, sign the body with `hookshot.sign()` and post it with Flask's test client:

```python
# test_webhooks.py
import os

os.environ.setdefault("HOOKSHOT_SECRET", "test-secret")

import hookshot
from app import app

BODY = b'{"id": "evt_1042", "type": "invoice.paid"}'


def post(body, header):
    client = app.test_client()
    return client.post(
        "/webhooks",
        data=body,
        headers={"Hookshot-Signature": header},
        content_type="application/json",
    )


def test_accepts_signed_delivery():
    header = hookshot.sign(BODY, os.environ["HOOKSHOT_SECRET"])
    assert post(BODY, header).status_code == 204


def test_rejects_tampered_body():
    header = hookshot.sign(BODY, os.environ["HOOKSHOT_SECRET"])
    assert post(BODY.replace(b"paid", b"voided"), header).status_code == 400


def test_rejects_missing_header():
    client = app.test_client()
    assert client.post("/webhooks", data=BODY).status_code == 400
```

TODO(verify): run these tests with pytest. They weren't run while writing this page because Flask wasn't available.

## Troubleshoot rejected deliveries

`str(error)` on a `SignatureError` is one of these three messages.

### `malformed Hookshot-Signature header`

**Cause:** The header is missing, or it isn't in the form `t=<unix seconds>,v1=<hex digest>`.

**Fix:** Log `request.headers.get("Hookshot-Signature")`. If it's `None`, check that the request reached this route from the sender and that no proxy strips the header. The parser splits on `,` with no trimming, so `t=1795065369, v1=…` (with a space) is also malformed.

### `timestamp outside tolerance`

**Cause:** The `t=` timestamp is more than `tolerance` seconds away from your server's clock. Either the delivery is a replay or a slow retry, or your server clock has drifted.

**Fix:** Check your server's clock against NTP. If the clock is right and the deliveries are legitimate, raise `tolerance`.

### `signature mismatch`

**Cause:** The digest doesn't match the body and secret you passed. The most likely causes, in order:

1. **The body was changed before `verify()` saw it.** You passed re-serialized JSON, a decoded string, or a body that middleware or a proxy rewrote. Pass `request.get_data()`.
2. **The secret is wrong.** Check that `HOOKSHOT_SECRET` holds the secret for this endpoint, with no surrounding whitespace or quotes.
3. **The delivery was forged or tampered with.** Rejecting it is correct.

## Related

- [How webhook signatures work](how-webhook-signatures-work.md): why the signature covers a timestamp, and why the raw body matters.
- [Replace a hand-rolled HMAC check with hookshot](replace-hand-rolled-hmac-check.md)
