# Verify webhook signatures with hookshot

This guide shows you how to reject forged or replayed webhook deliveries in a Flask app with `hookshot.verify()`. It takes about ten minutes.

**Before you start**, you need:

- A Flask app with a route that receives webhooks.
- The signing secret for the endpoint, from the sender's dashboard or settings.
- hookshot installed: `pip install hookshot`

If you already check signatures with your own HMAC code, read [Switch from a hand-rolled HMAC check](#switch-from-a-hand-rolled-hmac-check) first. It covers the differences that can break your endpoint when you switch.

## What verification protects against

Anyone who knows your webhook URL can send it a request. A signature proves that the delivery came from someone who holds your secret, and that nobody changed it in transit.

Every delivery has a header like this:

```
Hookshot-Signature: t=1763510400,v1=5f2b9c...e81a
```

- `t` is the time the delivery was signed, in Unix seconds.
- `v1` is an HMAC-SHA256 hex digest of `"{t}.{raw body}"`, keyed with your secret.

`hookshot.verify()` recomputes that digest and compares it to `v1` in constant time. It also rejects any delivery whose `t` is more than 5 minutes from your server's clock, so an attacker can't record a real delivery and send it again later. If the delivery passes, `verify()` returns `None`. If it fails, `verify()` raises `hookshot.SignatureError`.

## 1. Store the secret outside your code

Read the secret from an environment variable or your secrets manager. Don't commit it.

```python
import os

WEBHOOK_SECRET = os.environ["HOOKSHOT_SECRET"]
```

`verify()` expects the secret as a `str`. If your secrets manager returns `bytes`, decode it first (`secret.decode()`). If you don't, `verify()` raises `AttributeError`.

## 2. Verify the delivery before you use it

```python
import os

from flask import Flask, abort, request
import hookshot

app = Flask(__name__)
WEBHOOK_SECRET = os.environ["HOOKSHOT_SECRET"]


@app.post("/webhooks")
def receive_webhook():
    raw_body = request.get_data()
    header = request.headers.get("Hookshot-Signature", "")

    try:
        hookshot.verify(raw_body, header, WEBHOOK_SECRET)
    except hookshot.SignatureError as exc:
        app.logger.warning("Rejected webhook: %s", exc)
        abort(400)

    event = request.get_json()
    # The delivery is authentic. Handle the event.
    return "", 204
```

Three details in this code matter:

- **Pass the raw bytes.** `request.get_data()` returns the body exactly as it was received. Don't pass `json.dumps(request.get_json())` or anything else you've rebuilt from the parsed body. Re-serialized JSON almost never matches byte for byte, so verification fails with `signature mismatch`. If you pass a `str` instead of `bytes`, `verify()` raises `TypeError`.
- **Read the body first.** Call `request.get_data()` before anything else touches the body. Flask caches the bytes, so you can still call `request.get_json()` after verification.
- **Default the header to `""`.** If the header is missing, `request.headers.get()` returns `None`, and `verify(..., None, ...)` raises `AttributeError` instead of `SignatureError`. Your route would return a 500 instead of a 400. With an empty-string default, a missing header raises `SignatureError("malformed Hookshot-Signature header")` like any other bad header.

Do any work with the event only after `verify()` returns. Until then, the body is untrusted input.

## 3. Test the endpoint with `hookshot.sign()`

`hookshot.sign()` builds a valid header value for a body and secret. Use it in tests so you don't have to capture real deliveries.

```python
# test_webhooks.py
import hookshot
from app import app, WEBHOOK_SECRET

BODY = b'{"type": "invoice.paid", "id": "evt_123"}'


def post(body, header):
    client = app.test_client()
    return client.post(
        "/webhooks",
        data=body,
        headers={"Hookshot-Signature": header},
        content_type="application/json",
    )


def test_accepts_valid_signature():
    assert post(BODY, hookshot.sign(BODY, WEBHOOK_SECRET)).status_code == 204


def test_rejects_wrong_secret():
    assert post(BODY, hookshot.sign(BODY, "not-the-secret")).status_code == 400


def test_rejects_tampered_body():
    header = hookshot.sign(BODY, WEBHOOK_SECRET)
    assert post(BODY.replace(b"123", b"999"), header).status_code == 400


def test_rejects_old_delivery():
    import time
    header = hookshot.sign(BODY, WEBHOOK_SECRET, timestamp=int(time.time()) - 600)
    assert post(BODY, header).status_code == 400


def test_rejects_missing_header():
    client = app.test_client()
    response = client.post("/webhooks", data=BODY, content_type="application/json")
    assert response.status_code == 400
```

Set `HOOKSHOT_SECRET` in your test environment, for example `HOOKSHOT_SECRET=test-secret pytest`.

## Optional: change the replay window

By default, `verify()` accepts deliveries signed up to 300 seconds before or after your server's current time. To change the window, pass `tolerance` in seconds:

```python
hookshot.verify(raw_body, header, WEBHOOK_SECRET, tolerance=600)
```

Widen it only if your servers' clocks drift or deliveries are often delayed. A wider window gives an attacker more time to replay a captured delivery.

`tolerance=0` turns off the age check entirely, so a captured delivery stays valid forever. Don't use it in production. If old fixtures fail in your tests, re-sign them with `hookshot.sign()` instead.

## Switch from a hand-rolled HMAC check

If your code already parses `Hookshot-Signature` and compares digests itself, you can replace that code with one `verify()` call:

```python
# Before
parts = dict(p.split("=", 1) for p in header.split(","))
expected = hmac.new(secret, f"{parts['t']}.".encode() + raw_body, hashlib.sha256).hexdigest()
if not hmac.compare_digest(expected, parts["v1"]):
    abort(400)

# After
try:
    hookshot.verify(raw_body, header, secret)
except hookshot.SignatureError:
    abort(400)
```

Before you deploy, check these differences. Each one can make deliveries that your old code accepted fail now.

| If your old code… | With `verify()`… | What to do |
|---|---|---|
| Didn't check `t` against the clock | Deliveries more than 300 s old or in the future fail with `timestamp outside tolerance` | Sync server clocks with NTP. Re-sign old test fixtures with `hookshot.sign()`. |
| Took the secret as `bytes` | The secret must be a `str`. `bytes` raises `AttributeError`. | Pass `secret.decode()`. |
| Tolerated spaces in the header, such as `t=…, v1=…` | The header must match `t=<int>,v1=<hex>` exactly. Anything else fails with `malformed Hookshot-Signature header`. | Pass the header value unchanged. |
| Accepted any of several `v1=` values, for example during secret rotation | Only the last `v1` value in the header is checked, against a single secret | During rotation, call `verify()` with the new secret, and if it raises, try again with the old one. |
| Returned a specific status for a missing header | A `None` header raises `AttributeError` | Default the header to `""` as shown in step 2. |

You also get three checks you may not have had before: a constant-time comparison, a replay window, and a single exception type (`SignatureError`) for every kind of bad signature.

## Troubleshooting

`SignatureError` messages tell you which check failed. Log them, but don't send them back in the response.

### `signature mismatch`

The digest doesn't match. Check for these causes:
- You passed a re-serialized or decoded body instead of `request.get_data()`.
- Middleware or a proxy changed the body before it reached Flask, for example by decompressing it or normalizing line endings.
- You're using the secret for a different endpoint or environment, or the secret has extra whitespace from an environment file.

### `timestamp outside tolerance`

The delivery was signed more than `tolerance` seconds from your server's current time, in either direction. Check your server clock. If the delivery was a retry of an old event, the sender needs to sign it again.

### `malformed Hookshot-Signature header`

The header is missing or empty, `t` isn't an integer, or `t` or `v1` is missing. Check that a proxy isn't stripping or renaming the header.

### A 500 error instead of a 400

`verify()` raised something other than `SignatureError`:
- `AttributeError: 'NoneType' object has no attribute 'split'`: the header was missing. Default it to `""`.
- `AttributeError: 'bytes' object has no attribute 'encode'`: the secret is `bytes`. Decode it.
- `TypeError: can't concat str to bytes`: the body is a `str`. Use `request.get_data()`, not `request.get_data(as_text=True)`.
