import hashlib

from pwinput import pwinput
from auth.register.register import Register
from config.config import Config
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB
from utils.password_validator import password_validation
# from password_generator import PasswordGenerator

class User:
    def __init__(self):
        self.userdb = UsersDB()
        self.quesdb = QuestionsDB()
        self.score = ScoresDB()
        self.reg = Register()

    def add_user(self,username,password, role="player", is_changed=1):
        # username = input("Enter Username: ")
        # print(Config.SECURE_PASSWORD_PROMPT)
        # password = pwinput("Enter Password: ", "*")
        if self.reg.check_registration(username) is False:
            if password_validation(password):
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                self.userdb.create_user(username=username, password=hashed_password, role=role, is_changed=is_changed)
                print("User added Successfully.")
                return True
            else:
                print("Enter valid credentials!!")
                return False
        else:
            return None
        
    def show_all_user(self):
        return self.score.show_all_user()

    def update_user_details(self):
        username = input("Enter username: ")
        password = pwinput("Enter Password: ", "*")
        if self.userdb.check_login(username, password):
            new_password = input(f"Enter New Password: => ")
            self.userdb.update_user_password(username, password, new_password)
        else:
            print("Select Carefully!!")

    def show_leaderboard(self):
        self.score.show_leaderboard()

    def show_user(self):
        username = input("Enter Username: ")
        self.score.show_player_score(username)

