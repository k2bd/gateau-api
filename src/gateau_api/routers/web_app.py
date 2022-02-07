"""
Route intended to interface with the Web App
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_camelcase import CamelModel
from firebase_admin import auth

from gateau_api.common.get_service import get_service
from gateau_api.firebase import firebase_init_app
from gateau_api.service import GateauFirebaseService
from gateau_api.types import Player

logger = logging.getLogger(__name__)


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


router = APIRouter(dependencies=[Depends(get_user_uid)])


@router.post("/game/{gameId}/players")
async def post_player(
    gameId: str,
    player: Player,
    service: GateauFirebaseService = Depends(get_service),
):
    service.set_player(game_id=gameId, player=player)


class NewSubscriptions(CamelModel):
    subscriptions: List[str]


@router.post("/game/{gameId}/subscriptions")
async def post_subsctiptions(
    gameId: str,
    subscriptions: NewSubscriptions,
    service: GateauFirebaseService = Depends(get_service),
):
    service.add_subscriptions(game_id=gameId, meanings=set(subscriptions.subscriptions))
