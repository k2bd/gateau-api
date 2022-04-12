from typing import Any, Dict, Optional

import click
from firebase_admin import auth

from gateau_api.dependencies.user import ADMIN_CLAIM
from gateau_api.firebase import firebase_init_app

firebase_init_app()


@click.command()
@click.option("--uid", required=True, type=str)
def make_admin(uid: str):
    """
    Make an existing user an admin.

    Requires the FIREBASE_ADMIN_CREDENTIALS environment variable to be set.
    """
    user = auth.get_user(uid=uid)
    existing_claims: Optional[Dict[str, Any]] = user.custom_claims
    claims = existing_claims or {}

    claims[ADMIN_CLAIM] = True

    auth.set_custom_user_claims(uid, claims)


if __name__ == "__main__":
    make_admin()
