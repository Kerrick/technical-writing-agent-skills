# Verify webhook signatures with hookshot

This guide shows how to make a Flask route accept a webhook delivery only if it was signed with your signing secret and arrived recently. It then shows how to replace a hand-written HMAC check with `hookshot.verify`.

The examples use one running scenario: a billing service sends your app an `invoice.paid` webhook, and your Flask app marks the invoice as paid.

**Terms used on this page**

| Term | Meaning |
| --- | --- |
| delivery | One HTTP `POST` the sender makes to your endpoint. |
| signing secret | The string you and the sender share. The sender uses it to sign each delivery, and you use it to check the signature. Never send it in a delivery. |
| raw body | The exact bytes of the request body as they arrived, before any JSON parsing. |
| `Hookshot-Signature` | The request header that carries the signature, in the form `t=<unix seconds>,v1=<hex digest>`. |

## What hookshot does and doesn't do

`hookshot.verify` checks three things: the header is well formed, the timestamp in it is within a tolerance of your server's clock (300 seconds by default), and the digest matches the raw body and your signing secret.

It doesn't:

- parse or validate the payload, so you still call `json.loads` and check the fields you use;
- remember deliveries, so a replay inside the tolerance window passes (see [Reject replays inside the tolerance window](#reject-replays-inside-the-tolerance-window));
- store or rotate your signing secret;
- sign outgoing webhooks for your own customers. `hookshot.sign` exists for tests only.

## Prerequisites

- A Flask app and a signing secret from the sender's dashboard.
- Python 3.10 or later (`hookshot` uses `int | None` in its signatures).

Install the library:

```console
pip install hookshot flask
```

Put the signing secret in an environment variable, not in source control:

```console
export HOOKSHOT_SECRET="whsec_your_secret_here"
```

<details>
<summary>New to webhooks? Why signatures matter</summary>

A webhook endpoint is a public URL. Anyone who finds it can `POST` a fake "invoice paid" message to it. The sender prevents this by computing a signature from the body and the signing secret, and sending it in a header. Only someone who knows the secret can produce a signature that matches, so a matching signature tells you the delivery came from the sender and wasn't altered on the way.

The signature also covers a timestamp. Without it, someone who captured a real delivery could send it again later. With it, you can reject deliveries that are too old.

</details>

## Verify a delivery in a Flask route

Create `app.py`:

```python
import json
import os

from flask import Flask, abort, request
from hookshot import SignatureError, verify

app = Flask(__name__)
SECRET = os.environ["HOOKSHOT_SECRET"]


@app.post("/webhooks/billing")
def billing_webhook():
    raw_body = request.get_data()
    header = request.headers.get("Hookshot-Signature", "")

    try:
        verify(raw_body, header, SECRET)
    except SignatureError:
        abort(400)

    event = json.loads(raw_body)
    if event["type"] == "invoice.paid":
        mark_invoice_paid(event["invoice_id"])
    return "", 204


def mark_invoice_paid(invoice_id):
    # Replace with your own code that updates the invoice.
    print(f"paid: {invoice_id}")
```

`SignatureError` and `verify` come from the `hookshot` package. Search for those names when you need help or the reference.

What to notice:

- `request.get_data()` returns the raw body as `bytes`. `verify` needs exactly those bytes.
- The route calls `json.loads(raw_body)` only after `verify` succeeds, so it never parses a body it hasn't authenticated.
- A missing header becomes `""`, which `verify` rejects as malformed. Using `request.headers["Hookshot-Signature"]` instead would turn a missing header into a Flask 400 response with a different body, and passing `None` to `verify` would raise `AttributeError` rather than `SignatureError`.
- Every failure raises the same `SignatureError`, with a message that says which check failed: `malformed Hookshot-Signature header`, `timestamp outside tolerance`, or `signature mismatch`. Log the message on your side if you want to debug. Don't return it to the caller, because it tells an attacker which check they got past.

<details>
<summary>Why 400 and not 401 or 403?</summary>

Any 4xx tells the sender the delivery was refused. Senders typically retry non-2xx responses, so a rejected delivery may arrive several more times, and it will keep being rejected. Pick the status your monitoring already groups with bad requests. `verify` can't tell you whether a failure is an attack or a misconfigured secret, so don't use the status code to encode that.

</details>

## Don't verify a re-serialized body

The signature is computed over the bytes the sender transmitted. If you parse the JSON and serialize it again, the bytes change (key order, whitespace, number formatting), and the signature no longer matches even though the data is the same.

```python
@app.post("/webhooks/billing")
def billing_webhook():
    # Wrong: this body is rebuilt from parsed JSON, not the bytes that were signed.
    event = request.get_json()
    raw_body = json.dumps(event).encode()
    try:
        verify(raw_body, request.headers.get("Hookshot-Signature", ""), SECRET)
    except SignatureError:
        abort(400)
    ...  # your handler code
```

This runs without error, and it may even pass for some payloads, which is why it's dangerous. It starts failing, with `signature mismatch`, as soon as a payload contains whitespace or key order that `json.dumps` doesn't reproduce. For example, a sender that pretty-prints its JSON will never verify. The fix is the route in the previous section: pass `request.get_data()` straight to `verify`.

> **Warning:** Read the raw body with `request.get_data()` before anything touches the request body as form data. In Flask, reading `request.form` or `request.files` consumes the stream. Webhook deliveries are normally JSON, so this mostly matters if you share a route with form posts.

## Test your route

`hookshot.sign` builds a valid `Hookshot-Signature` value, so you can test without the sender. Create `test_app.py`:

```python
import json
import time

import pytest
from hookshot import sign

import app as billing_app

SECRET = billing_app.SECRET
BODY = json.dumps({"type": "invoice.paid", "invoice_id": "inv_1042"}).encode()


@pytest.fixture
def client():
    return billing_app.app.test_client()


def post(client, header):
    return client.post(
        "/webhooks/billing",
        data=BODY,
        content_type="application/json",
        headers={"Hookshot-Signature": header},
    )


def test_valid_signature_is_accepted(client):
    assert post(client, sign(BODY, SECRET)).status_code == 204


def test_wrong_secret_is_rejected(client):
    assert post(client, sign(BODY, "some-other-secret")).status_code == 400


def test_old_delivery_is_rejected(client):
    ten_minutes_ago = int(time.time()) - 600
    assert post(client, sign(BODY, SECRET, timestamp=ten_minutes_ago)).status_code == 400


def test_missing_header_is_rejected(client):
    assert client.post("/webhooks/billing", data=BODY).status_code == 400
```

Run it with the secret set:

```console
HOOKSHOT_SECRET=whsec_test pytest
```

Each of the four tests checks one of the ways `verify` can reject a delivery. `sign` takes the same `raw_body` and `secret` as `verify`, plus an optional `timestamp` for simulating old deliveries.

## Replace a hand-written HMAC check

If you already verify signatures yourself, this is the check `verify` replaces. A typical hand-written version:

```python
import hashlib
import hmac
import time


def is_valid(raw_body: bytes, header: str, secret: str) -> bool:
    parts = dict(p.split("=", 1) for p in header.split(","))
    timestamp = parts["t"]
    if abs(time.time() - int(timestamp)) > 300:
        return False
    expected = hmac.new(
        secret.encode(), f"{timestamp}.".encode() + raw_body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, parts["v1"])
```

`verify(raw_body, header, secret)` does the same work: it parses `t` and `v1` from the header, rejects timestamps more than `tolerance` seconds from now in either direction, computes HMAC-SHA256 over `"<t>." + raw_body`, and compares with `hmac.compare_digest`. The two are equivalent for valid deliveries. They differ in the failure cases:

| Situation | Hand-written version above | `hookshot.verify` |
| --- | --- | --- |
| Header missing a `t` or `v1` part, or `t` not an integer | Raises `KeyError` or `ValueError`, which becomes a 500 unless you catch it | Raises `SignatureError("malformed Hookshot-Signature header")` |
| Timestamp too old or too far in the future | Returns `False` | Raises `SignatureError("timestamp outside tolerance")` |
| Digest doesn't match | Returns `False` | Raises `SignatureError("signature mismatch")` |
| Valid | Returns `True` | Returns `None` |

To switch:

1. Replace `if not is_valid(...): abort(400)` with `try: verify(...) except SignatureError: abort(400)`.
2. Delete your parsing, age check, and comparison code.
3. Keep your tests. Rewrite any that assert on `False` to expect a `SignatureError`, or to expect your route's 400.

> **Warning:** `verify` raises on failure and returns `None` on success. Writing `if not verify(...): abort(400)` rejects **every** valid delivery, because `None` is falsy. Writing `if verify(...): ...` never runs the body, and a route that does `verify(...)` without handling the exception returns a 500 for forged requests instead of rejecting them cleanly. Use `try`/`except SignatureError`.

## Adjust the tolerance

`verify` rejects any delivery whose timestamp is more than 300 seconds from your server's clock. Pass `tolerance` to change that:

```python
verify(raw_body, header, SECRET, tolerance=120)
```

Reasoning: a shorter window leaves less time for a captured delivery to be replayed, but it means a server clock that drifts by more than the window rejects every delivery, valid or not. Keep your servers on NTP before you tighten it.

> **Warning:** `tolerance=0` turns the age check off entirely, so a captured delivery stays valid forever. It does not mean "zero seconds allowed". Don't use it outside tests.

## Reject replays inside the tolerance window

A replayed delivery inside the tolerance window has a valid signature and a fresh-enough timestamp, so `verify` accepts it. The sender's retries also arrive as repeat deliveries. If handling the same event twice would do harm (marking an invoice paid twice, sending two emails), make the handler idempotent: store the event ID from the payload and skip IDs you've already processed. Whether the payload carries an ID is up to the sender; check its webhook documentation.

## Rotating the signing secret

`verify` takes one secret and checks one `v1` digest. It has no support for accepting an old and a new secret at the same time. To rotate without downtime, call `verify` with the new secret and, on `SignatureError`, again with the old one, until the sender has switched over:

```python
def verify_with_rotation(raw_body, header):
    for secret in (SECRET, PREVIOUS_SECRET):
        try:
            verify(raw_body, header, secret)
            return
        except SignatureError:
            continue
    raise SignatureError("no configured secret matches")
```

Define `SECRET` and `PREVIOUS_SECRET` from environment variables, and remove `PREVIOUS_SECRET` once rotation is complete.
