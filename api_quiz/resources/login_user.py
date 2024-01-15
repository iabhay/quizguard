from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from flask_jwt_extended import create_access_token
from auth.login.login import Login

blp = Blueprint("login", "login",description="Login module")

@blp.route("/login")
class LoginUser(MethodView):
    def __init__(self) -> None:
        self.log = Login()

    @blp.arguments(UserSchema)
    def post(self, user_data):
        """Login a new user"""
        res = self.log.loginmodule(user_data["username"], user_data["password"])
        if res is None or res.size() == 0:
            abort(400, message="User not registered")
        else:
            if res[2] == "admin":
                res =  "batman"
            elif res[2] == "superadmin":
                res = "hanuman"
            else:
                res = "spiderman"
            access_token = create_access_token(identity=user_data["username"], additional_claims={"role": res, "username": user_data["username"]})
            return {"access_token": access_token,
                    "message": f"{user_data["username"]} logged in successfully as {res}"}