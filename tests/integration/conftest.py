from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from firebasil.auth import AuthClient
from firebasil.auth.types import SignUpUser

from gateau_api.api import app
from gateau_api.service import GateauFirebaseService
from tests.integration.constants import (
    EXAMPLE_USER_DISPLAY_NAME,
    EXAMPLE_USER_EMAIL,
    EXAMPLE_USER_PASSWORD,
    EXAMPLE_USER_PHOTO_URL,
    FIREBASE_AUTH_EMULATOR_HOST,
)


@pytest.fixture
async def auth_client() -> AsyncGenerator[AuthClient, None]:
    if not FIREBASE_AUTH_EMULATOR_HOST:
        raise RuntimeError(
            "Please set the FIREBASE_AUTH_EMULATOR_HOST environment variable"
        )
    async with AuthClient(api_key="any-fake-key") as auth_client:
        yield auth_client


@pytest.fixture
async def example_user(auth_client: AuthClient) -> AsyncGenerator[SignUpUser, None]:
    """
    Create an example user with a set email, display name, and photo URL.
    """
    user = await auth_client.sign_up(
        email=EXAMPLE_USER_EMAIL,
        password=EXAMPLE_USER_PASSWORD,
    )

    await auth_client.update_profile(
        id_token=user.id_token,
        display_name=EXAMPLE_USER_DISPLAY_NAME,
        photo_url=EXAMPLE_USER_PHOTO_URL,
    )

    try:
        yield user
    finally:
        await auth_client.delete_account(user.id_token)


@pytest.fixture
async def service(
    example_user: SignUpUser,
) -> AsyncGenerator[GateauFirebaseService, None]:
    async with GateauFirebaseService(id_token=example_user.id_token) as s:
        try:
            yield s
        finally:
            await s.db_root.delete()


@pytest.fixture
def api_client(service: GateauFirebaseService) -> TestClient:
    """
    API test client that can interact with a temporary database
    """
    return TestClient(app)
