from fastapi import APIRouter, HTTPException, Body, Path
from starlette import status
from database.module_queries.question_db import QuestionsDB
from api_quiz.utils_api import role_required
from api_quiz.resources.admin_endpoints import token_dependency, oauth2_bearer

router = APIRouter()


@router.put("/question/{id}", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def question_module(token: token_dependency, ques_data=Body(), id=Path()):
    ques = QuestionsDB()
    if int(id) > 0:
        res = ques.update_question(ques_data["question"], ques_data["option1"], ques_data["option2"], ques_data["option3"], ques_data["option4"], ques_data["correct"], id)
        if res:
            return {
                "message": "Successfully updated!"
            }
        raise HTTPException(400, detail="No Such question exist with this id.")
    i = ques.get_last_id()
    res = ques.add_question(i, ques_data["question"], ques_data["option1"], ques_data["option2"], ques_data["option3"], ques_data["option4"], ques_data["correct"])
    if res is False:
        raise HTTPException(400, detail="Question not added successfully.")
    return {
        "question_id": i,
        "question": ques_data["question"],
        "option1": ques_data["option1"],
        "option2": ques_data["option2"],
        "option3": ques_data["option3"],
        "option4": ques_data["option4"],
        "correct": ques_data["correct"],
        "message": "Question added Successfully."
    }

@router.get("/question/{id}", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def view_question(token: token_dependency, id=Path()):
    ques = QuestionsDB()
    res = None
    if id:
        tup = ques.fetch_question(id)
        if tup:
            curr = {
                "Id": tup[0],
                "question": tup[1],
                "option1": tup[2],
                "option2": tup[3],
                "option3": tup[4],
                "option4": tup[5],
                "correct": tup[6]
                }
            return curr
        raise HTTPException(400, detail="No Question available for this id.")

@router.get("/questions", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def view_all_question(token: token_dependency):
    ques = QuestionsDB()
    res = ques.show_all_question()
    if res:
        response = {}
        for tup in res:
            curr = {
            "question": tup[1],
            "option1": tup[2],
            "option2": tup[3],
            "option3": tup[4],
            "option4": tup[5],
            "correct": tup[6]
            }
            response[tup[0]] = curr
        return response
    else:
        raise HTTPException(400, detail="No Questions Available")


@router.delete("/question/{id}", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def delete_question(token: token_dependency, id=Path()):
    ques = QuestionsDB()
    if id:
        res = ques.delete_question(id)
        if res:
            return {
                "message": "Successfully deleted."
            }
        raise HTTPException(400, detail="No such Question with this id is available.")
    raise HTTPException(400, detail="ID NOT PROVIDED!!")