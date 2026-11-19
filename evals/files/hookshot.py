"""hookshot: verify signed webhook deliveries.

Senders sign each delivery with HMAC-SHA256 over f"{timestamp}.{raw_body}" and send
the header  Hookshot-Signature: t=<unix seconds>,v1=<hex digest>
"""
import hashlib
import hmac
import time

__version__ = "3.4.0"


class SignatureError(Exception):
    pass


def verify(raw_body: bytes, header: str, secret: str, tolerance: int = 300) -> None:
    """Raise SignatureError unless `header` is a valid signature of `raw_body`.

    `raw_body` must be the exact bytes received; re-serialized JSON will not match.
    Deliveries older than `tolerance` seconds are rejected to block replays;
    tolerance=0 disables the age check (not recommended).
    """
    try:
        parts = dict(p.split("=", 1) for p in header.split(","))
        timestamp, sig = int(parts["t"]), parts["v1"]
    except (ValueError, KeyError):
        raise SignatureError("malformed Hookshot-Signature header")
    if tolerance and abs(time.time() - timestamp) > tolerance:
        raise SignatureError("timestamp outside tolerance")
    expected = hmac.new(secret.encode(), f"{timestamp}.".encode() + raw_body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig):
        raise SignatureError("signature mismatch")


def sign(raw_body: bytes, secret: str, timestamp: int | None = None) -> str:
    """Return a Hookshot-Signature header value. Use in tests."""
    t = int(time.time()) if timestamp is None else timestamp
    digest = hmac.new(secret.encode(), f"{t}.".encode() + raw_body, hashlib.sha256).hexdigest()
    return f"t={t},v1={digest}"
