from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, UsernameSchema
from flask_jwt_extended import jwt_required
from controllers.admincontroller import AdminController
from api_quiz.utils_api import role_required
from controllers.usercontroller import User
from database.module_queries.users_db import UsersDB
blp = Blueprint("admin", __name__, description="admin")

@blp.route("/user")
class AdminModule(MethodView):
    def __init__(self):
        self.user = User()

    @role_required(["batman", "hanuman"])
    @jwt_required()
    @blp.doc(params={"role": "Role"})
    @blp.arguments(UserSchema)
    def post(self, user_data):
        res = self.user.add_user(username=user_data["username"], password=user_data["password"])
        if res is False:
            abort(400, message="Invalid Details!")
        elif res is None:
            abort(400, message="User already Exists.")
        return {
            "username": user_data["username"],
            "message": "User Added Successfully."
        }
    

    @role_required(["batman", "hanuman"])
    @jwt_required()
    @blp.arguments(UsernameSchema)
    def delete(self, user_data):
        userdb = UsersDB()
        res = userdb.delete_user_by_admin(user_data["username"])
        if res is False:
            abort(400, message="User Not deleted.")
        return {
            "message": "User deleted Successfully."
        }


@blp.route("/users")
class Admin2Module(MethodView):
    def __init__(self):
        self.user = User()

    @role_required(["batman", "hanuman"])
    @jwt_required()
    def get(self):
        res = self.user.show_all_user()
        response = {}
        id = 1
        for tup in res:
            curr = {
                "last_played_time": tup[0],
                "username": tup[1],
                "role": tup[2],
                "highscore": tup[3],
                "Login Status": tup[4],
            }
            response[id] = curr
            id += 1
        return response
    

@blp.route("/show_admins")
class AdminDetails(MethodView):
    def __init__(self):
        self.user = User()
        self.userdb = UsersDB()
        self.adm = AdminController()

    @role_required(["batman", "hanuman"])
    @jwt_required()
    def get(self):
        res = self.adm.show_all_admins()
        response = {}
        id = 1
        for tup in res:
            curr = {
                "last_played_time": tup[1],
                "username": tup[0],
                "highscore": tup[2],
                "Login Status": tup[3],
            }
            response[id] = curr
            id += 1
        return response



@blp.route("/loggedin")
class LoggedIn(MethodView):
    def __init__(self):
        self.adm = AdminController()

    @role_required(["batman", "hanuman"])
    @jwt_required()
    def get(self):
        res = self.adm.show_all_loggedin()
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


    