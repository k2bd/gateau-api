import logging
from typing import List

from fastapi import Depends, FastAPI, Header
from fastapi_camelcase import CamelModel

from gateau_api.service import GateauFirebaseService
from gateau_api.types import Player, RamChangeInfo, Subscription

logger = logging.getLogger(__name__)

app = FastAPI()


async def get_service() -> GateauFirebaseService:
    return GateauFirebaseService()


@app.post("/game/{gameId}/players")
async def post_player(
    gameId: str,
    player: Player,
    service: GateauFirebaseService = Depends(get_service),
):
    service.set_player(game_id=gameId, player=player)


class NewSubscriptions(CamelModel):
    subscriptions: List[str]


@app.post("/game/{gameId}/subscriptions")
async def post_subsctiptions(
    gameId: str,
    subscriptions: NewSubscriptions,
    service: GateauFirebaseService = Depends(get_service),
):
    service.add_subscriptions(game_id=gameId, meanings=set(subscriptions.subscriptions))


@app.get("/game/{gameId}/ramSubscriptions", response_model=Subscription)
async def get_ram_subscription(
    gameId: str,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Header(""),
):
    subscriptions = service.get_ram_subscriptions(game_id=gameId, player_id=player_id)
    return Subscription(ram_addresses=sorted(subscriptions))


@app.post("/game/{gameId}/ramChange")
async def post_ram_change(
    gameId: str,
    change: RamChangeInfo,
    service: GateauFirebaseService = Depends(get_service),
    player_id: str = Header(""),
):
    service.handle_ram(game_id=gameId, player_id=player_id, change_info=change)
