"""
Router for routes intended to interface with the desktop client
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_camelcase import CamelModel
from firebase_admin import auth

from gateau_api.common.get_service import get_service
from gateau_api.firebase import firebase_init_app
from gateau_api.service import GateauFirebaseService
from gateau_api.types import Player, RamChangeInfo, Subscription

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
