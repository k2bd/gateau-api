import logging
from typing import Optional

from fastapi import Depends, FastAPI, Header

from gateau_api.service import GateauFirebaseService
from gateau_api.types import RamChangeInfo, Subscription

logger = logging.getLogger(__name__)

app = FastAPI()


def get_service() -> GateauFirebaseService:
    return GateauFirebaseService()


@app.get("/game/{gameId}/subscription", response_model=Subscription)
async def get_subscription(
    gameId: str,
    service: GateauFirebaseService = Depends(get_service),
    player_id: Optional[str] = Header(None),
):
    logger.info(f"GET /game/{gameId}/subscription")

    subscriptions = service.get_ram_subscriptions(game_id=gameId, player_id=player_id)

    return Subscription(ram_addresses=list(subscriptions))


@app.post("/game/{gameId}/ramChange")
async def post_ram_change(
    gameId: str,
    change: RamChangeInfo,
    service: GateauFirebaseService = Depends(get_service),
    player_id: Optional[str] = Header(None),
):
    logger.info(f"POST /game/{gameId}/ramChange")

    service.handle_ram(game_id=gameId, player_id=player_id, change_info=change)
