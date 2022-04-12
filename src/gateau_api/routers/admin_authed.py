"""
Routes that you need to be logged in to use
"""

import logging
from typing import List

from fastapi import APIRouter, Depends
from firebase_admin import auth

from gateau_api.dependencies import get_user_uid
from gateau_api.dependencies.user import require_admin
from gateau_api.firebase import firebase_init_app
from gateau_api.types import FirebaseUser

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

router = APIRouter(
    dependencies=[
        Depends(get_user_uid),
        Depends(require_admin),
    ]
)

firebase_init_app()


@router.get("/admin/users", response_model=List[FirebaseUser])
async def get_users():
    users = auth.list_users().iterate_all()
    # TODO: paginate
    return [
        FirebaseUser(
            uid=user.uid,
            claims=user.custom_claims,
            display_name=user.display_name,
            photo_url=user.photo_url,
            email=user.email,
        )
        for user in users
    ]
