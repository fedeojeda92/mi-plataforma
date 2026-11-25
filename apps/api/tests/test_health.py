from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_returns_request_id() -> None:
    response = client.get("/health")

    assert response.headers["X-Request-ID"]


def test_health_reuses_incoming_request_id() -> None:
    request_id = "my-trace-123"

    response = client.get("/health", headers={"X-Request-ID": request_id})

    assert response.headers["X-Request-ID"] == request_id
