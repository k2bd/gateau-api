from typing import AsyncGenerator

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from gateau_api.service import GateauFirebaseService


async def get_service(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> AsyncGenerator[GateauFirebaseService, None]:
    async with GateauFirebaseService(id_token=credentials.credentials) as service:
        yield service
