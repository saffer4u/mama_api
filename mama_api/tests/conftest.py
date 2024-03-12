from typing import Generator

from fastapi.testclient import TestClient

from mama_api.main import app


def client() -> Generator:
    yield TestClient(app)
