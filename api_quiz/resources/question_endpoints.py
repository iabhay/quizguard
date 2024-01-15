from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import QuestionSchema
from flask_jwt_extended import jwt_required
from api_quiz.utils_api import role_required
from database.module_queries.question_db import QuestionsDB
blp = Blueprint("question", __name__, description="question")

@blp.route("/question")
@blp.route("/question/<int:id>")
class QuestionModule(MethodView):
    def __init__(self):
        self.ques = QuestionsDB()

    @role_required(["batman", "hanuman"])
    @jwt_required()
    @blp.arguments(QuestionSchema)
    def post(self, ques_data, id=None):
        if id:
            res = self.ques.update_question(ques_data["question"], ques_data["option1"], ques_data["option2"], ques_data["option3"], ques_data["option4"], ques_data["correct"], id)
            if res:
                return {
                    "message": "Successfully updated!"
                }
            abort(400, message="No Such question exist with this id.")
        i = self.ques.get_last_id()
        res = self.ques.add_question(i, ques_data["question"], ques_data["option1"], ques_data["option2"], ques_data["option3"], ques_data["option4"], ques_data["correct"])
        if res is False:
            abort(400, message="Question not added successfully.")
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
    
    
    @role_required(["batman", "hanuman"])
    @jwt_required()
    def get(self, id=None):
        res = None
        if id:
            tup = self.ques.fetch_question(id)
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
            abort(400, message="No Question available for this id.")
        res = self.ques.show_all_question()
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
            abort(400, message="No Questions Available")

    @role_required(["batman", "hanuman"])
    @jwt_required()
    def delete(self, id=None):
        if id:
            res = self.ques.delete_question(id)
            if res:
                return {
                    "message": "Successfully deleted."
                }
            abort(400, message="No such Question with this id is available.")
        abort(400, message="ID NOT PROVIDED!!")




    