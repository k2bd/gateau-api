import base64
import json
from typing import Any, Dict

import firebase_admin
from pyrebase import initialize_app

from gateau_api.constants import (
    FIREBASE_ADMIN_CREDENTIALS,
    FIREBASE_API_KEY,
    FIREBASE_AUTH_DOMAIN,
    FIREBASE_DATABASE_URL,
    FIREBASE_STORAGE_BUCKET,
)


def service_account_info() -> Dict[str, Any]:
    return json.loads(base64.b64decode(FIREBASE_ADMIN_CREDENTIALS).decode("utf-8"))


def firebase_init_app():
    creds = firebase_admin.credentials.Certificate(service_account_info())

    if not firebase_admin._apps:
        firebase_admin.initialize_app(creds)


def pyrebase_app():
    config = {
        "databaseURL": FIREBASE_DATABASE_URL,
        "apiKey": FIREBASE_API_KEY,
        "authDomain": FIREBASE_AUTH_DOMAIN,
        "storageBucket": FIREBASE_STORAGE_BUCKET,
    }
    return initialize_app(config)
