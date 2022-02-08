"""
Route intended to interface with the Web App
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi_camelcase import CamelModel

from gateau_api.dependencies import get_service, get_user_uid
from gateau_api.service import GateauFirebaseService
from gateau_api.types import Player

logger = logging.getLogger(__name__)


router = APIRouter(dependencies=[Depends(get_user_uid)])


@router.post("/game/{gameId}/players")
async def join_game(
    gameId: str,
    player: Player,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Depends(get_user_uid),
):
    if player.uid != player_id:
        raise HTTPException(
            status_code=401,
            detail="Cannot add someone else to the game",
        )
    service.set_player(game_id=gameId, player=player)


@router.delete("/game/{gameId}/players")
async def leave_game(
    gameId: str,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Depends(get_user_uid),
):
    service.remove_player(game_id=gameId, player_id=player_id)


class NewSubscriptions(CamelModel):
    subscriptions: List[str]


@router.post("/game/{gameId}/subscriptions")
async def post_subsctiptions(
    gameId: str,
    subscriptions: NewSubscriptions,
    service: GateauFirebaseService = Depends(get_service),
):
    service.add_subscriptions(game_id=gameId, meanings=set(subscriptions.subscriptions))
