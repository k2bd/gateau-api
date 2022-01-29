import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gateau_api.game_ram.carts import Cartridge
from gateau_api.types import Subscription

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/game/{roomCode}/subscription/{cartType}", response_model=Subscription)
async def get_subscription(roomCode: str, cartType: Cartridge):
    logger.info(f"GET /game/{roomCode}/subscription/{cartType}")
    pass


@app.post("/game/{roomCode}/ramChange/")
async def post_ram_change(roomCode: str):
    logger.info(f"POST /game/{roomCode}/ram/")
    pass
