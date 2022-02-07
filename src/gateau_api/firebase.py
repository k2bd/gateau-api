import base64
import json

import firebase_admin

from gateau_api.constants import FIREBASE_ADMIN_CREDENTIALS


def firebase_init_app():
    service_account_info = json.loads(
        base64.b64decode(FIREBASE_ADMIN_CREDENTIALS).decode("utf-8")
    )
    creds = firebase_admin.credentials.Certificate(service_account_info)

    if not firebase_admin._apps:
        firebase_admin.initialize_app(creds)
