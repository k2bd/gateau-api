from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from gateau_api.api import app
from gateau_api.service import GateauFirebaseService


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
