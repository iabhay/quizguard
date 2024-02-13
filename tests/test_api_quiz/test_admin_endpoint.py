from fastapi.testclient import TestClient
from fastapi import status
import pytest
from main import app
from api_quiz.resources.admin_endpoints import oauth2_bearer
from tests.test_api_quiz.test_resources.test_login_endpoint import token_generator

client = TestClient(app)

def test_token_generator():
    return token_generator("batman", "admin", "@Admin1234")

app.dependency_overrides[oauth2_bearer] = test_token_generator

def test_view_all_logged_in():
    res = client.get("/loggedin")
    assert len(res.json()) > 0

def test_view_all_logged_in_fail():
    res = client.get("/loggedin")
    assert res.status_code != status.HTTP_404_NOT_FOUND

def data_generator(username, password):
    return {
    "username": username,
    "password": password
    }

def test_add_user():
    res= client.post("/user", json=data_generator("apitester2", "@Apitester21234"))
    assert res.json() != {"username": "apitester2",
        "message": "User Added Successfully."}
    
def test_add_user_already_exist():
    res= client.post("/user", json=data_generator("apitester2", "@Apitester21234"))
    assert res.json() == {"detail": "User already Exists."}

def test_add_user_invalid():
    res= client.post("/user", json=data_generator("apitester3", "@Apites"))
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json() == {"detail": "Invalid Details!"}

def test_delete_user():
    res = client.request("DELETE", "/user", json=data_generator("apitester2", "@Apitester21234"))
    assert res.json() == {"message": "User deleted Successfully."}

def test_view_all_users():
    res = client.get("/users")
    assert len(res.json())> 0

def test_view_all_admins():
    res = client.get("/show-admins")
    assert len(res.json())> 0

