from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_decode_valid():
    response = client.get("/decode?vin=3TMKB5FN0SM050383")
    assert response.status_code == 200
    body = response.json()
    assert body["make"] == "Toyota"
    assert body["model"] == "Tacoma"

def test_decode_invalid():
    response = client.get("/decode?vin=XYZ123")
    assert response.status_code == 404

def test_short_vin():
    response = client.get("/decode?vin=123")
    assert response.status_code == 400
