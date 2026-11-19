import json
import os
import time

os.environ["HOOKSHOT_SECRET"] = "whsec_test"
import hookshot
from app import app

SECRET = "whsec_test"
BODY = json.dumps({"type": "ping"}).encode()
c = app.test_client()


def post(h):
    hd = {"Content-Type": "application/json"}
    if h is not None:
        hd["Hookshot-Signature"] = h
    return c.post("/webhooks/hookshot", data=BODY, headers=hd).status_code


print("valid", post(hookshot.sign(BODY, SECRET)))
print("tampered", post(hookshot.sign(b'{"type":"x"}', SECRET)))
print("old", post(hookshot.sign(BODY, SECRET, int(time.time()) - 1000)))
print("missing", post(None))
print("garbage", post("nonsense"))
print("wrong secret", post(hookshot.sign(BODY, "other")))
