from fastapi.testclient import TestClient
from fastapi import status
import pytest
from main import app
from api_quiz.resources.admin_endpoints import oauth2_bearer
from tests.test_api_quiz.test_resources.test_login_endpoint import token_generator
from database.module_queries.question_db import QuestionsDB

client = TestClient(app)


def test_token_generator():
    return token_generator("batman", "admin", "@Admin1234")


app.dependency_overrides[oauth2_bearer] = test_token_generator


def test_question_module():
    ques_db = QuestionsDB()
    index = ques_db.get_last_id()
    res = client.put(
        "/question/0",
        json=data_generator(
            question="What's your name?",
            option1="I am not telling you",
            option2="Will tell you later",
            option3="Batman",
            option4="No name",
            correct="Batman",
        ),
    )
    assert res.json() == {
        "question_id": index,
        "question": "What's your name?",
        "option1": "I am not telling you",
        "option2": "Will tell you later",
        "option3": "Batman",
        "option4": "No name",
        "correct": "Batman",
        "message": "Question added Successfully.",
    }


def test_question_module_update():
    ques_db = QuestionsDB()
    index = ques_db.get_last_id()
    res = client.put("/question/1", json=data_generator(
        question="What's my name?",
            option1="I am not telling you",
            option2="Will tell you later",
            option3="Batman",
            option4="No name",
            correct="Batman",
    ))
    assert res.json() == {
                "message": "Successfully updated!"
            }


def test_view_question():
    res = client.get("/question/3")
    assert res.json() == {
                "Id": 3,
        "question": "What's your name?",
        "option1": "I am not telling you",
        "option2": "Will tell you later",
        "option3": "Batman",
        "option4": "No name",
        "correct": "Batman"
        }

def test_view_question_fail():
    res = client.get("/question/1")
    assert res.status_code == status.HTTP_400_BAD_REQUEST

def test_view_all_question():
    res = client.get("/questions")
    assert res.status_code == status.HTTP_200_OK
    assert len(res.json()) > 0

def test_delete_question():
    res = client.request("DELETE","/question/1")
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {
                "message": "Successfully deleted."
            }

def data_generator(question, option1, option2, option3, option4, correct):
    return {
        "question": question,
        "option1": option1,
        "option2": option2,
        "option3": option3,
        "option4": option4,
        "correct": correct,
    }
