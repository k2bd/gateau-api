from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth

from gateau_api.firebase import firebase_init_app

firebase_init_app()


def _verify_token(id_token: str):
    try:
        return auth.verify_id_token(id_token=id_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e)) from e


async def get_user_id_token(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
):
    id_token = credentials.credentials
    _verify_token(id_token=id_token)
    return id_token


async def get_user_uid(
    id_token: str = Depends(get_user_id_token),
):
    user = _verify_token(id_token=id_token)
    return user["uid"]
