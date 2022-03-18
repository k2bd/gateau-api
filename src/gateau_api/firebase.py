import base64
import json
from typing import Any, Dict

import firebase_admin

from gateau_api.constants import FIREBASE_ADMIN_CREDENTIALS, TESTING_PROJECT_ID


def service_account_info() -> Dict[str, Any]:
    return json.loads(base64.b64decode(FIREBASE_ADMIN_CREDENTIALS).decode("utf-8"))


def firebase_init_app():
    """
    Initialize the admin app, using a testing project ID if we're emulating.
    """
    if TESTING_PROJECT_ID:
        firebase_admin.initialize_app(options={"projectId": TESTING_PROJECT_ID})
        return

    # Production
    creds = firebase_admin.credentials.Certificate(service_account_info())

    if not firebase_admin._apps:
        firebase_admin.initialize_app(creds)
