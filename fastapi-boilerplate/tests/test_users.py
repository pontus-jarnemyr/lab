import pytest

from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient


def test_get_all(client: TestClient):
    resp = client.get("/api/v1/users")
    assert resp.status_code == 200


def test_create_user(client: TestClient):
    data = {
        "max_capacity": 123,
        "username": "muh_user",
        "description": "haha"
    }
    resp = client.post("/api/v1/users", json=data)
    assert resp.status_code == 201


# @pytest.mark.asyncio
def test_delete_user(client: TestClient, async_client: AsyncClient):
    resp = client.post("/api/v1/users", json={"max_capacity": 1, "username": "hehe"})
    assert resp.status_code == 201
    new_user = resp.json()
    # resp = async_client.delete(f"/api/v1/users/{new_user['user_id']}")
    resp = client.delete(f"/api/v1/users/{new_user['user_id']}")
    assert resp.status_code == 200
