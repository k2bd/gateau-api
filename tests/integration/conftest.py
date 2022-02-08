from typing import Generator

import pytest
from fastapi.testclient import TestClient

from gateau_api.api import app
from gateau_api.dependencies import get_service, get_user_uid
from gateau_api.service import GateauFirebaseService
from tests.integration.constants import EXAMPLE_ID_TOKEN, EXAMPLE_USER_ID


@pytest.fixture
def service() -> Generator[GateauFirebaseService, None, None]:
    s = GateauFirebaseService(id_token=EXAMPLE_ID_TOKEN)
    try:
        yield s
    finally:
        s.root.remove()


@pytest.fixture
def mock_dependencies(service: GateauFirebaseService):
    def fake_get_user_uid():
        return EXAMPLE_USER_ID

    def fake_get_service():
        return service

    old_overrides = app.dependency_overrides.copy()
    app.dependency_overrides[get_user_uid] = fake_get_user_uid
    app.dependency_overrides[get_service] = fake_get_service

    try:
        yield
    finally:
        app.dependency_overrides = old_overrides


@pytest.fixture
def api_client(service: GateauFirebaseService, mock_dependencies) -> TestClient:
    """
    API test client that can interact with a temporary database
    """
    return TestClient(app)
