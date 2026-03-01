# app/tests/test_auth.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.password_handler import hash_password

client = TestClient(app)

# Dummy user data
user_data = {
    "email": "testuser@example.com",
    "password": "TestPass123",
    "role": "candidate"
}

@pytest.fixture
def create_user():
    # Normally you'd insert into DB or use a mock
    user_data["password"] = hash_password(user_data["password"])
    return user_data

def test_register_user(create_user):
    response = client.post("/auth/register", json=create_user)
    assert response.status_code in [200, 201]
    assert "email" in response.json()["data"]

def test_login_user(create_user):
    login_data = {"email": create_user["email"], "password": "TestPass123"}
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()["data"]
