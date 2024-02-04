from fastapi.testclient import TestClient
from fastapi import status
import pytest
from main import app

client = TestClient(app)

@pytest.mark.skip
def test_register_user(mocker):
    res = client.post("/register",json=return_obj("apitester5", "@Apitester51234"))
    # assert res.status_code == status.HTTP_201_CREATED
    assert res.json() == {
                "username": "apitester5",
                "message": "User registered successfully"
                }

def test_register_user_false(mocker):
    # reg_mock = mocker.Mock()
    res = client.post("/register",json=return_obj("veryveryuser", ""))
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json()["detail"] == "Invalid password"

def test_register_already_user():
    res = client.post("/register", json=return_obj("apitester", ""))
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json()["detail"] == "User already registered"

def return_obj(username, password):
    return {"username": username, "password": password}




