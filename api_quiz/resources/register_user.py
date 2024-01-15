from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from auth.register.register import Register

blp = Blueprint("register", "register",description="Register module")

@blp.route("/register")
class RegisterUser(MethodView):
    def __init__(self) -> None:
        self.reg = Register()

    @blp.arguments(UserSchema)
    def post(self, user_data):
        """Register a new user"""
        if self.reg.register_module(user_data["username"], user_data["password"]) is None:
            abort(400, message="User already registered")
        elif self.reg.register_module(user_data["username"], user_data["password"]) is False:
            abort(400, message="Invalid password")
        else:
            return {
                    "username": user_data["username"],
                    "message": "User registered successfully"
                    }
        
        