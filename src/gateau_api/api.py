import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
