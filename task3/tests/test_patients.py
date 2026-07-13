from fastapi.testclient import TestClient
from app.main import app

import pytest
from fastapi.testclient import TestClient
from jose import jwt
 
from app.main import app
from app.database import create_db_and_tables, get_session
from app.auth import get_current_user, SECRET_KEY, ALGORITHM
from fastapi import HTTPException

def get_token(client):
    client.post("/auth/register", json={"username": "patientuser", "password": "testpass123"})
    response = client.post("/auth/token", data={"username": "patientuser", "password": "testpass123"})
    return response.json()["access_token"]

def test_get_patients(client):
    response = client.get("/patients")
    assert response.status_code == 200


def test_post_patient(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 30,
        "condition": "fever",
        "risk_score": 50,
        "active": True
    }, headers=headers)
    assert response.status_code == 201


def test_post_patient_no_auth(client):
    token = get_token(client)
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 30,
        "condition": "fever",
        "risk_score": 50,
        "active": True
    })
    assert response.status_code == 401


def test_post_patient_invalid_data(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 200,  # invalid
        "condition": "fever",
        "risk_score": 50,
        "active": True
    }, headers=headers)
    assert response.status_code == 422

def test_get_patient_by_id(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    # first create a patient
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 30,
        "condition": "fever",
        "risk_score": 50,
        "active": True
    }, headers=headers)
    patient_id = response.json()["id"]
    # then get it by id
    response = client.get(f"/patients/{patient_id}")
    assert response.status_code == 200


def test_get_patient_not_found(client):
    response = client.get("/patients/99999")
    assert response.status_code == 404

def test_put_patient(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    # create a patient first
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 30,
        "condition": "fever",
        "risk_score": 50,
        "active": True
    }, headers=headers)
    patient_id = response.json()["id"]
    # now update it
    response = client.put(f"/patients/{patient_id}", json={
        "name": "Jane Doe",
        "age": 25,
        "condition": "cold",
        "risk_score": 30,
        "active": True
    }, headers=headers)
    assert response.status_code == 200



def test_patch_patient(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    # create a patient first
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 30,
        "condition": "fever",
        "risk_score": 50,
        "active": True
    }, headers=headers)
    patient_id = response.json()["id"]
    # now update it
    response = client.patch(f"/patients/{patient_id}", json={
        "name": "Updated name"
    }, headers=headers)
    assert response.status_code == 200


def test_delete_patient(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    # create a patient first
    response = client.post("/patients", json={
        "name": "John Doe",
        "age": 30,
        "condition": "fever",
        "risk_score": 50,
        "active": True
    }, headers=headers)
    patient_id = response.json()["id"]
    # now update it
    response = client.delete(f"/patients/{patient_id}", headers=headers)
    assert response.status_code == 204


def test_get_patients_filter(client):
    response = client.get("/patients?active=true")
    assert response.status_code == 200


def test_put_patient_not_found(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/patients/99999", json={
        "name": "Jane", "age": 25, "condition": "cold", "risk_score": 30, "active": True
    }, headers=headers)
    assert response.status_code == 404

def test_patch_patient_not_found(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.patch("/patients/99999", json={"name": "Updated"}, headers=headers)
    assert response.status_code == 404

def test_delete_patient_not_found(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/patients/99999", headers=headers)
    assert response.status_code == 404

def test_get_patients_condition_filter(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/patients", json={
        "name": "John", "age": 30, "condition": "fever", "risk_score": 50, "active": True
    }, headers=headers)
    response = client.get("/patients?condition=fever")
    assert response.status_code == 200


def test_create_db_and_tables_runs():
    """Directly calling this executes line 8 (metadata.create_all)."""
    create_db_and_tables()
 
 
# --- database.py: lines 12-13 -------------------------------------------
def test_get_session_yields_a_session():
    """Pulling one value from the generator executes the
    'with Session(engine) as session' and 'yield session' lines."""
    gen = get_session()
    session = next(gen)
    assert session is not None
    # close out the generator cleanly
    with pytest.raises(StopIteration):
        next(gen)
 
 
# --- main.py: line 36 ----------------------------------------------------
def test_startup_event_creates_tables():
    """Using TestClient as a context manager triggers FastAPI's
    startup event, which calls create_db_and_tables() (line 36).
    A plain TestClient(app) call WITHOUT 'with' will NOT cover this line."""
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
 
 
# --- auth.py: line 37 -----------------------------------------------------
def test_get_current_user_rejects_token_without_sub():
    """A token that's valid JWT but has no 'sub' claim should hit
    the 401 raise on line 37."""
    token = jwt.encode({"foo": "bar"}, SECRET_KEY, algorithm=ALGORITHM)
 
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token)
 
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"



       