from fastapi.testclient import TestClient
from fastapi import status
import pytest
from main import app
from api_quiz.resources.admin_endpoints import oauth2_bearer
from tests.test_api_quiz.test_resources.test_login_endpoint import token_generator

client = TestClient(app)

def test_token_generator():
    return token_generator("hanuman", "superadmin", "@Superdmin1234")

app.dependency_overrides[oauth2_bearer] = test_token_generator

def test_super_admin_module():
    res = client.post("/admin", json=data_generator("admin2", "@Admin21234"))
    assert res.json() == {"message": "Admin added successfully."}

def test_super_admin_module_fail():
    res = client.post("/admin", json=data_generator("admin3", "Ad34"))
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json()["detail"] == "Validation failed."

def test_delete_admin():
    res = client.request("DELETE","/admin", json=data_generator("admin2", "@Admin21234"))
    assert res.json() == {"message": "Admin deleted successfully."}

def test_delete_admin_fail():
    res = client.request("DELETE","/admin", json=data_generator("admin3", "Ad34"))
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json()["detail"] == "Admin not found."

def test_admin_to_user():
    res = client.put("/admin/to_user/admin")
    assert res.json() == {"message": "Role Changing successful."}

def test_user_to_admin():
    res = client.post("/user/to_admin/admin")
    assert res.json() == {"message": "Role Changing successful."}


def data_generator(username, password):
    return {
        "username": username,
        "password": password
    }
