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

def test_player_module():
    res = client.get("/profile/apitester")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["user"] == "apitester"

def test_player_module_superadmin():
    res = client.get("/profile/superadmin")
    assert res.status_code == status.HTTP_400_BAD_REQUEST

def test_player_module_non_existing():
    res = client.get("/profile/abhay")
    assert res.status_code == status.HTTP_400_BAD_REQUEST


def test_common_module():
    res = client.get("/leaderboard")
    assert len(res.json()) > 0




