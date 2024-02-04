import hashlib
from pwinput import pwinput
from views.admin_point import Admin
from views.player_point import Player
from views.super_admin import SuperAdminModule
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB
from auth.login.role_based_access import RoleBasedAccess
class Login:
    def __init__(self):
        self.user = UsersDB()
        self.score = ScoresDB()
        self.super_admin_module = SuperAdminModule()
        self.role_access = RoleBasedAccess()

    def loginmodule(self, username, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        entry = self.user.check_login(username, hashed_password)
        if not entry:
            return None
        else:
            # print("You are logged in!!")
            self.mark_login(username)
            # resp = self.role_access.role_based_entry_point(entry)
            # if resp is None:
            #     self.mark_logout(username)
                # print("Exiting login Menu!!")
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

    def super_admin_menu(self):
        print("SUPER ADMIN POWERS ------------>\n")
        try:
            self.super_admin_module.super_admin_module()
        except Exception:
            print(Exception.__name__)
            print("Super Module not accessed!!!!")
