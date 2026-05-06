from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient):
    resp = client.get("/api/healthcheck")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Server is running!"}
