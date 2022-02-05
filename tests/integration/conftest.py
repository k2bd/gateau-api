from typing import Generator

import pytest
from fastapi.testclient import TestClient

from gateau_api.api import app
from gateau_api.service import GateauFirebaseService

from firebase_admin import auth, initialize_app

import contextlib
import os


@pytest.fixture
def custom_token():
    auth.create_custom_token("testUser123")


@pytest.fixture
def service(custom_token) -> Generator[GateauFirebaseService, None, None]:
    s = GateauFirebaseService()
    try:
        yield s
    finally:
        s.root.remove()


@pytest.fixture
def api_client(service) -> TestClient:
    """
    API test client that can interact with a temporary database
    """
    return TestClient(app)
