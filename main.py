import os
from pwinput import pwinput
from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from auth.register.register import Register
from auth.login.login import Login
from config.config import Config
from api_quiz.resources.login_user import blp as login_blp
from api_quiz.resources.register_user import blp as register_blp
from api_quiz.resources.player_res import blp as player_blp
from api_quiz.resources.admin_endpoints import blp as admin_blp
from api_quiz.resources.question_endpoints import blp as ques_blp
from api_quiz.resources.superadmin_endpoints import blp as superadmin_blp

class QuizLix:
    def __init__(self):
        self.register = Register()
        self.login = Login()

    def menu(self):
        print("QuizGuard  : Smart Quiz, Simply Played!!")
        ask = int(input(Config.MAIN_PROMPT))
        if 1 > ask or ask > 2:
            print("Bye! Thanks for playing.")
        while 0 < ask < 3:
            if ask == 1:
                # print(Config.ENTER_USERNAME_PROMPT)
                username = input("Enter username: ")
                print(Config.SECURE_PASSWORD_PROMPT)
                password = pwinput("Enter Password: ", mask="*")
                response = self.register.register_module(username=username, password=password)
                if response == False:
                    print("Invalid Password!!")
                elif response is None:
                    print("Already registered!!\nTry login!!")
                elif response == True:
                    print("Registered successfully!!")
            elif ask == 2:
                # print(Config.ENTER_USERNAME_PROMPT)
                username = input("Enter username: ")
                print(Config.SECURE_PASSWORD_PROMPT)
                password = pwinput("Enter Password: ", mask="*")
                response = self.login.loginmodule(username, password)
                if response is None:
                    print("Invalid Credentials!!")
            else:
                print("Please Select Carefully!")
            ask = int(input(Config.MAIN_PROMPT))
            if ask == 3:
                print("Bye! Thanks for playing.")


if __name__ == "__main__":
    app = Flask(__name__)
    app.config["API_TITLE"] = "Quiz Guard"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    api = Api(app)
    
    app.config["JWT_SECRET_KEY"] = "abhay"
    jwt = JWTManager(app)
    api.register_blueprint(register_blp)
    api.register_blueprint(login_blp)
    api.register_blueprint(player_blp)
    api.register_blueprint(admin_blp)
    api.register_blueprint(ques_blp)
    api.register_blueprint(superadmin_blp)
    app.run(debug=True, port=5000)
    Config.load()
    quiz_obj = QuizLix()
    quiz_obj.menu()