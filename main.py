import hashlib
import hmac
import json
import logging

from flask import Flask, request
from waitress import serve

from data import ImmichKioskWebhookPayload

app = Flask(__name__)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)

log = logging.getLogger(__name__)

SECRET = "your_secret_token_here"


def verify_signature(payload_body, secret_token, signature_header) -> bool:
    """
    Verify if the webhook signature is valid

    Args:
        payload_body: The raw request payload body
        secret_token: The shared secret token used to sign the payload
        signature_header: The signature header from the request

    Returns:
        bool: True if signature is valid, False otherwise
    """
    if not signature_header:
        return False
    hash_object = hmac.new(
        secret_token.encode("utf-8"), msg=payload_body, digestmod=hashlib.sha256
    )
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        return False
    return True


@app.route("/webhook", methods=["POST"])
def webhook():
    """
    Webhook endpoint that verifies the request signature, processes then prints the payload

    The signature (if provided) is verified against the shared secret token. If verification fails,
    returns an error response. If successful, the payload is processed and logged.

    Returns:
        tuple: Response message and status code
            - ("Payload received!", 200) for successful requests
            - ("Error", 500) for invalid/missing signatures
            - ("Error", 400) for invalid JSON payload
    """
    secret_header = request.headers.get("X-Kiosk-Signature-256")
    log.debug("secret_header", secret_header)

    if secret_header is not None:
        verify = verify_signature(request.get_data(), SECRET, secret_header)
        if not verify:
            log.error("Invalid signature")
            return "Erro", 500

    data = request.get_json()
    print(json.dumps(data, indent=4))

    # Using dataclass
    # payload = ImmichKioskWebhookPayload(**data)
    # print(payload)

    return "Payload received!", 200


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=6000)
