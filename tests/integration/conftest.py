from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from firebase_admin import auth
from firebasil.auth import AuthClient
from firebasil.auth.types import SignUpUser

from gateau_api.api import app
from gateau_api.constants import FIREBASE_API_KEY
from gateau_api.dependencies.user import ADMIN_CLAIM
from gateau_api.firebase import firebase_init_app
from gateau_api.service import GateauFirebaseService
from tests.integration.constants import (
    EXAMPLE_ADMIN_DISPLAY_NAME,
    EXAMPLE_ADMIN_EMAIL,
    EXAMPLE_ADMIN_PASSWORD,
    EXAMPLE_ADMIN_PHOTO_URL,
    EXAMPLE_USER_DISPLAY_NAME,
    EXAMPLE_USER_EMAIL,
    EXAMPLE_USER_PASSWORD,
    EXAMPLE_USER_PHOTO_URL,
    FIREBASE_AUTH_EMULATOR_HOST,
)
from tests.integration.helpers import temporary_service, temporary_user

firebase_init_app()


@pytest.fixture
async def auth_client() -> AsyncGenerator[AuthClient, None]:
    if not FIREBASE_AUTH_EMULATOR_HOST:
        raise RuntimeError(
            "Please set the FIREBASE_AUTH_EMULATOR_HOST environment variable"
        )
    async with AuthClient(api_key=FIREBASE_API_KEY) as auth_client:
        yield auth_client


@pytest.fixture
async def example_user(auth_client: AuthClient) -> AsyncGenerator[SignUpUser, None]:
    """
    Create an example user with a set email, display name, and photo URL.
    """
    async with temporary_user(
        auth_client=auth_client,
        email=EXAMPLE_USER_EMAIL,
        password=EXAMPLE_USER_PASSWORD,
        display_name=EXAMPLE_USER_DISPLAY_NAME,
        photo_url=EXAMPLE_USER_PHOTO_URL,
    ) as user:
        yield user


@pytest.fixture
async def example_admin(auth_client: AuthClient) -> AsyncGenerator[SignUpUser, None]:
    """
    Create an admin user with a set email, display name, and photo URL.
    """
    async with temporary_user(
        auth_client=auth_client,
        email=EXAMPLE_ADMIN_EMAIL,
        password=EXAMPLE_ADMIN_PASSWORD,
        display_name=EXAMPLE_ADMIN_DISPLAY_NAME,
        photo_url=EXAMPLE_ADMIN_PHOTO_URL,
    ) as user:
        auth.set_custom_user_claims(user.local_id, {ADMIN_CLAIM: True})
        yield user


@pytest.fixture
async def service(
    example_user: SignUpUser,
) -> AsyncGenerator[GateauFirebaseService, None]:
    async with temporary_service(id_token=example_user.id_token) as s:
        yield s


@pytest.fixture
async def admin_service(
    example_admin: SignUpUser,
) -> AsyncGenerator[GateauFirebaseService, None]:
    async with temporary_service(id_token=example_admin.id_token) as s:
        yield s


@pytest.fixture
def api_client(service: GateauFirebaseService) -> TestClient:
    """
    API test client that can interact with a temporary database
    """
    return TestClient(app)
