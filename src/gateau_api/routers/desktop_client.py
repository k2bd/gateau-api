"""
Router for routes intended to interface with the desktop client
"""

import logging

from fastapi import APIRouter, Depends, Header

from gateau_api.common.get_service import get_service
from gateau_api.service import GateauFirebaseService
from gateau_api.types import RamChangeInfo, Subscription

logger = logging.getLogger(__name__)

# TODO: auth

router = APIRouter()


@router.get("/game/{gameId}/ramSubscriptions", response_model=Subscription)
async def get_ram_subscription(
    gameId: str,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Header(""),
):
    subscriptions = service.get_ram_subscriptions(game_id=gameId, player_id=player_id)
    return Subscription(ram_addresses=sorted(subscriptions))


@router.post("/game/{gameId}/ramChange")
async def post_ram_change(
    gameId: str,
    change: RamChangeInfo,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Header(""),
):
    service.handle_ram(game_id=gameId, player_id=player_id, change_info=change)
