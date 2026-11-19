from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_public_properties_endpoint():
    response = client.get("/api/properties")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_website_homepage_is_served():
    response = client.get("/")
    assert response.status_code == 200
    assert "Quỳnh Như BDS" in response.text


def test_lead_requires_consent():
    response = client.post(
        "/api/leads",
        json={"name": "Nguyen Van A", "phone": "0901234567", "need": "Tim dat", "consent": False},
    )
    assert response.status_code == 400


def test_lead_rejects_invalid_phone():
    response = client.post(
        "/api/leads",
        json={"name": "Nguyen Van A", "phone": "abcdefgh", "need": "Tim dat", "consent": True},
    )
    assert response.status_code == 422
