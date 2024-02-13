import hashlib
from pwinput import pwinput
from auth.register.register import Register
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB
from utils.password_validator import password_validation


class User:
    def __init__(self):
        self.userdb = UsersDB()
        self.quesdb = QuestionsDB()
        self.score = ScoresDB()
        self.reg = Register()

    def add_user(self,username,password, role="player", is_changed=1):
        if self.reg.check_registration(username) is False:
            if password_validation(password):
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                self.userdb.create_user(username=username, password=hashed_password, role=role, is_changed=is_changed)
                return True
            else:
                return False
        else:
            return None
        
    def show_all_user(self):
        return self.score.show_all_user()

    def update_user_details(self, username, password,new_password):
        if self.userdb.check_login(username, password):
            self.userdb.update_user_password(username, password, new_password)
            return True
        else:
            return None

    def show_leaderboard(self):
        self.score.show_leaderboard()

    def show_user(self, username):
        self.score.show_player_score(username)

