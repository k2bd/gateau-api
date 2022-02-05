from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from gateau_api.api import app
from gateau_api.constants import (
    FIREBASE_API_KEY,
    FIREBASE_AUTH_DOMAIN,
    FIREBASE_DATABASE_URL,
    FIREBASE_STORAGE_BUCKET,
)
from gateau_api.service import GateauFirebaseService

from gateau_api.api import __name__ as API_NAME

from .constants import EXAMPLE_USER_ID



@pytest.fixture
def service() -> Generator[GateauFirebaseService, None, None]:
    s = GateauFirebaseService()
    try:
        yield s
    finally:
        s.root.remove()


@pytest.fixture
def api_client(service: GateauFirebaseService) -> TestClient:
    """
    API test client that can interact with a temporary database
    """
    return TestClient(app)
