import json

import firebase_admin

from gateau_api.constants import FIREBASE_ADMIN_CREDENTIALS


def firebase_init_app():
    service_account_info = json.loads(FIREBASE_ADMIN_CREDENTIALS)
    creds = firebase_admin.credentials.Certificate(service_account_info)

    if not firebase_admin._apps:
        firebase_admin.initialize_app(creds)
