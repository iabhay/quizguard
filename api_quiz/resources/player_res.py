import json
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from controllers.player_controller import PlayerController
from api_quiz.utils_api import role_required
from schemas import PlayerSchema
blp = Blueprint("player", __name__, description="player")

@blp.route("/profile/<string:username>")
class PlayerModule(MethodView):
    @role_required(["spiderman", "batman", "hanuman"])
    @jwt_required()
    @blp.response(200, PlayerSchema)
    def get(self, username):
        if username == "admin":
            abort(400, message="Profile Not available.")
        self.pc_obj = PlayerController()
        res = self.pc_obj.highscoreinfo(username)
        if res is None:
            abort(400, message="{Profile data not found.}")
        return {"last_played": res["Last Played"],
                    "user": res["User"],
                    "highscore":res["Highscore"],
                    "login_status": res["Login Status"]
                }
    

@blp.route("/leaderboard")
class CommonModule(MethodView):

    @role_required(["spiderman", "batman", "hanuman"])
    @jwt_required()
    @blp.response(200)
    def get(self):
        self.pc_obj = PlayerController()
        res = self.pc_obj.leaderboard()
        if res is None or len(res) == 0:
            abort(400, message="{Data not found.}")
        response = {}
        id = 1
        for tup in res:
            curr = {
                "last_played_time": tup[0],
                "username": tup[1],
                "highscore": tup[2]
            }
            response[id] = curr
            id += 1
        return response