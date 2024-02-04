from fastapi.testclient import TestClient
from fastapi import status
import pytest
from datetime import datetime, timedelta
from main import app
from api_quiz.resources.login_user import router, login_user, create_access_token

client = TestClient(app)

def test_login_user_spiderman(mocker):
    response = client.post("/login", json=data_generator("apitester", "@Apitester1234"))
    expected_token = return_token("spiderman", "apitester", "@Apitester1234")
    assert response.json()["token"] == expected_token["token"]
    assert response.json() == expected_token

def test_login_user_batman(mocker):
    response = client.post("/login", json=data_generator("admin", "@Admin1234"))
    expected_token = return_token("batman", "admin", "@Admin1234")
    assert response.json() == expected_token

def test_login_user_hanuman(mocker):
    response = client.post("/login", json=data_generator("superadmin", "@Superadmin1234"))
    expected_token = return_token("hanuman", "superadmin", "@Superadmin1234")
    assert response.json() == expected_token

def test_login_user_false(mocker):
    response = client.post("/login", json=data_generator("abhaydfds", "@Abhay1234fsdf"))
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "User not registered"

def data_generator(username, password):
    return {
        "username": username,
        "password": password
    }

def token_generator(role, username, password):
    user_data = data_generator(username, password)
    token = create_access_token(role, user_data["username"], timedelta(minutes=15))
    return token

def return_token(role, username, password):
    token = token_generator(role, username, password)
    return {"token": token,
            "message": f"{username} logged in successfully as {role}"}
