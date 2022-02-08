from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth

from gateau_api.firebase import firebase_init_app

firebase_init_app()


async def get_user_uid(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
):
    token = credentials.credentials

    try:
        user = auth.verify_id_token(id_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e)) from e

    return user["uid"]
