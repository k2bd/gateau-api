from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from gateau_api.service import GateauFirebaseService


async def get_service(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> GateauFirebaseService:
    return GateauFirebaseService(id_token=credentials.credentials)
