import hashlib
from pwinput import pwinput
from views.admin_point import Admin
from views.player_point import Player
from views.super_admin import SuperAdminModule
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB


class Login:
    def __init__(self):
        self.user = UsersDB()
        self.score = ScoresDB()

    def loginmodule(self, username, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        entry = self.user.check_login(username, hashed_password)
        if not entry:
            return None
        else:
            self.mark_login(username)
            return entry

            
    def mark_login(self, username):
        try:
            self.score.mark_login(username)
        except Exception:
            print(Exception.__name__)
            print("Marking login status active not done!!!!")

    def mark_logout(self, username):
        try:
            self.score.mark_logout(username)
        except Exception:
            print(Exception.__name__)
            print("Marking login status non-active not done!!!!")
