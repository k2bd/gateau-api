import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from gateau_api.exceptions import PlayerNotFound
from gateau_api.routers import desktop_client, web_app

logger = logging.getLogger(__name__)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(web_app.router)
app.include_router(desktop_client.router)


@app.exception_handler(PlayerNotFound)
async def missing_player_exception_handler(request: Request, exc: PlayerNotFound):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )
