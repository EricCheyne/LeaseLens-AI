from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to LeaseLens AI API" in response.json()["message"]


def test_health_check():
    # Health endpoint is now under /api/v1/healthz
    response = client.get("/api/v1/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
