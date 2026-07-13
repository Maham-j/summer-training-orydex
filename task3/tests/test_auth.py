from fastapi.testclient import TestClient
from app.main import app



def test_register_success(client):
    # POST to /auth/register with username and password
    response = client.post("/auth/register", json={"username": "testuser", "password": "testpass123"})
    # assert status code is 201
    assert response .status_code == 201
    # assert "username" is in response
    assert "username" in response.json()


def test_register_duplicate(client):
    client.post("/auth/register", json={"username": "dupuser", "password": "testpass123"})
    response = client.post("/auth/register", json={"username": "dupuser", "password": "testpass123"})
    assert response.status_code == 409


def test_login_success(client):
    # first register a user, then login
    # assert status code 200
    # assert "access_token" is in response
    client.post("/auth/register", json={"username": "loginuser", "password": "testpass123"})
    response = client.post("/auth/token", data={"username": "loginuser", "password": "testpass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_wrong_password(client):
    # try to login with wrong password
    # assert status code 401
    response = client.post("/auth/token", data={"username": "loginuser", "password": "wrongpassword"})
    assert response.status_code == 401

def test_invalid_token(client):
    headers = {"Authorization": "Bearer invalidtoken123"}
    response = client.post("/patients", json={
        "name": "John", "age": 30, "condition": "fever", "risk_score": 50, "active": True
    }, headers=headers)
    assert response.status_code == 401

