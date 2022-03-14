"""
Routes that you need to be logged in to use
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi_camelcase import CamelModel

from gateau_api.dependencies import get_service, get_user_uid
from gateau_api.service import GateauFirebaseService
from gateau_api.types import Player, RamChangeInfo, Subscription

logger = logging.getLogger(__name__)

router = APIRouter(dependencies=[Depends(get_user_uid)])

# ---- Web app routes ----


@router.post("/game/{gameId}/players")
async def join_game(
    gameId: str,
    player: Player,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Depends(get_user_uid),
):
    """
    From the web app, join a game
    """
    if player.uid != player_id:
        raise HTTPException(
            status_code=401,
            detail="Cannot add someone else to the game",
        )
    await service.join_game(game_id=gameId, player=player)


@router.delete("/game/{gameId}/players")
async def leave_game(
    gameId: str,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Depends(get_user_uid),
):
    """
    From the web app, leave a game
    """
    await service.remove_player(game_id=gameId, player_id=player_id)


class NewSubscriptions(CamelModel):
    subscriptions: List[str]


@router.post("/game/{gameId}/subscriptions")
async def post_subsctiptions(
    gameId: str,
    subscriptions: NewSubscriptions,
    service: GateauFirebaseService = Depends(get_service),
):
    """
    From the web app, post new subscriptions
    """
    await service.add_subscriptions(
        game_id=gameId,
        meanings=set(subscriptions.subscriptions),
    )


# ---- Desktop app routes ----


@router.get("/game/{gameId}/ramSubscriptions", response_model=Subscription)
async def get_ram_subscription(
    gameId: str,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Depends(get_user_uid),
):
    """
    From the desktop client, get RAM addresses to subscribe to
    """
    subscriptions = await service.get_ram_subscriptions(
        game_id=gameId,
        player_id=player_id,
    )
    return Subscription(ram_addresses=sorted(subscriptions))


@router.post("/game/{gameId}/ramChange")
async def post_ram_change(
    gameId: str,
    change: RamChangeInfo,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Depends(get_user_uid),
):
    """
    From the desktop client, post a RAM update
    """
    await service.handle_ram(
        game_id=gameId,
        player_id=player_id,
        change_info=change,
    )
