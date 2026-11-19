# Verify webhook signatures with hookshot

Reject forged or replayed webhook requests in a Flask app by checking the `Hookshot-Signature` header with `hookshot.verify()`. This guide also shows how to replace a hand-written HMAC check.

A *webhook* is an HTTP POST that another service sends to a URL in your app when something happens. Anyone who learns that URL can send it fake events, so your app must confirm that each request came from the sender. The sender proves this by signing each request with a secret that only you and the sender know. hookshot checks that signature.

## Before you start

- A Flask app with a route that receives webhook POST requests.
- The signing secret for that endpoint, from the sender's dashboard. This guide uses the placeholder `whsec_example`.
- The `hookshot` module installed in your app's environment.

## Verify requests in a Flask route

1. Store the secret outside your code. For example, set an environment variable:

   ```bash
   export HOOKSHOT_SECRET=whsec_example
   ```

2. Add a route that reads the raw request body and verifies it before doing anything else:

   ```python
   import os

   from flask import Flask, request, abort
   from hookshot import verify, SignatureError

   app = Flask(__name__)
   SECRET = os.environ["HOOKSHOT_SECRET"]


   @app.post("/webhooks/orders")
   def orders_webhook():
       raw_body = request.get_data()
       header = request.headers.get("Hookshot-Signature", "")
       try:
           verify(raw_body, header, SECRET)
       except SignatureError:
           abort(400)

       event = request.get_json()
       # Handle the event, for example mark order event["id"] as paid.
       return "", 204
   ```

   The code does three things that matter:

   - **It verifies `request.get_data()`, not parsed JSON.** The signature covers the exact bytes the sender transmitted. If you parse the body and serialize it again, whitespace and key order can change, and the signature no longer matches.
   - **It passes `""` as the header default.** If the header is missing, `request.headers.get()` returns `None`, and `verify()` raises `AttributeError` instead of `SignatureError` (confirmed against hookshot 3.4.0). Your `except SignatureError` would not catch it, and the client would get a 500 response instead of a rejection.
   - **It verifies before parsing.** Nothing in the body is trusted until the check passes.

3. Start the app and send a request without a signature:

   ```bash
   curl -i -X POST http://localhost:5000/webhooks/orders -d '{"id":"evt_1"}'
   ```

   You should see `HTTP/1.1 400 BAD REQUEST`.

## Test with a signed request

`hookshot.sign()` produces a valid header value, so you can test the route without the real sender.

```python
import json

from hookshot import sign

from app import app  # the module that defines your Flask app


def test_accepts_signed_request():
    body = json.dumps({"id": "evt_1"}).encode()
    header = sign(body, "whsec_example")
    response = app.test_client().post(
        "/webhooks/orders",
        data=body,
        content_type="application/json",
        headers={"Hookshot-Signature": header},
    )
    assert response.status_code == 204
```

Set `HOOKSHOT_SECRET=whsec_example` when you run the test, so the route and the test use the same secret. To test a rejected request, change one byte of `body` after signing, or pass a `timestamp` more than 300 seconds in the past: `sign(body, "whsec_example", timestamp=1)`.

Use `sign()` only in tests. Your app never needs to sign requests.

## Replace a hand-written HMAC check

hookshot implements the same scheme that most hand-written checks use: HMAC-SHA256 over `"{timestamp}.{raw_body}"`, with the header `Hookshot-Signature: t=<unix seconds>,v1=<hex digest>`. If your current code matches this, replace it as follows.

1. Find your existing check. A typical one looks like this:

   ```python
   import hashlib
   import hmac

   def is_valid(raw_body, header, secret):
       parts = dict(p.split("=", 1) for p in header.split(","))
       signed = f"{parts['t']}.".encode() + raw_body
       expected = hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()
       return expected == parts["v1"]
   ```

2. Delete it and call `verify()` as shown above. Change the control flow: `verify()` returns `None` on success and raises `SignatureError` on failure. It does not return a boolean, so `if verify(...)` is always false.

3. Check what your old code skipped. `verify()` does these things that hand-written checks often omit:

   | Behavior | What `verify()` does |
   | - | - |
   | Replay protection | Rejects a request whose timestamp differs from the server clock by more than `tolerance` seconds. The default is 300. |
   | Comparison | Uses `hmac.compare_digest()`, which takes constant time. The `==` comparison in the example above does not. |
   | Bad input | Raises `SignatureError("malformed Hookshot-Signature header")` for a header that is empty or lacks `t` or `v1`, or has a non-integer `t`. |

   If your old code allowed older timestamps, a sender with a delayed retry queue may now see rejections. See [Troubleshooting](#troubleshooting).

## Troubleshooting

`verify()` raises `SignatureError` with one of three messages.

| Message | Cause | Fix |
| - | - | - |
| `malformed Hookshot-Signature header` | The header is missing, empty, or not in the form `t=<unix seconds>,v1=<hex digest>`. | Print `request.headers.get("Hookshot-Signature")`. Confirm that the sender signs with hookshot and that a proxy does not strip or rewrite the header. |
| `timestamp outside tolerance` | The delivery is more than `tolerance` seconds (default 300) away from your server's clock, in either direction. | Check that your server clock is synchronized with NTP. If the sender legitimately delivers late, pass a larger value: `verify(raw_body, header, SECRET, tolerance=900)`. |
| `signature mismatch` | The body or secret differs from what the sender signed. | See the list below. |

For `signature mismatch`, check these in order:

1. You verify `request.get_data()`, not re-serialized JSON.
2. No middleware reads and changes the body before your route runs.
3. You use the secret for this endpoint. Senders usually issue a different secret for each endpoint and environment.
4. The secret has no leading or trailing whitespace, for example a trailing newline from a secrets file.

Setting `tolerance=0` turns off the age check, which removes replay protection. Do not use it in production. To log the cause of a rejection, log `str(error)`, not the header or secret.
