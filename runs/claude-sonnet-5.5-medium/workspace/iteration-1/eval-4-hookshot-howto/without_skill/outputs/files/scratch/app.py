import os

from flask import Flask, abort, request

import hookshot

app = Flask(__name__)
WEBHOOK_SECRET = os.environ["HOOKSHOT_SECRET"]


@app.post("/webhooks/hookshot")
def receive():
    try:
        hookshot.verify(
            request.get_data(),
            request.headers.get("Hookshot-Signature", ""),
            WEBHOOK_SECRET,
        )
    except hookshot.SignatureError:
        abort(400)

    event = request.get_json()
    print("verified event:", event)
    return "", 204
