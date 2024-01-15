import hashlib
from pwinput import pwinput
from views.admin_point import Admin
from views.player_point import Player
from views.super_admin import SuperAdminModule
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB
from config.config import Config
from utils.password_validator import password_validation
class Login:
    def __init__(self):
        self.user = UsersDB()
        self.score = ScoresDB()
        self.ques = QuestionsDB()
        self.player = Player()
        self.admin = Admin()
        self.super_admin_module = SuperAdminModule()

    def loginmodule(self, username, password):
        # username = input("Enter Your Name: ")
        # password = pwinput(prompt="Enter your password:- ", mask="*")
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        entry = self.user.check_login(username, hashed_password)
        if not entry:
            print("Invalid Credentials!!")
            return None
        else:
            self.mark_login(username)
            return entry
            print("You are logged in!!")
            if entry[2] == "admin":
                is_admin_menu = int(input(Config.ADMIN_MENU_PROMPT))
                if is_admin_menu == 3:
                    print("Exiting login Menu!!")
                while is_admin_menu != 3:
                    if is_admin_menu == 1:
                        print("Welcome to admin Powers: -->")
                        self.admin.adminmodule()
                        break
                    elif is_admin_menu == 2:
                        print("Welcome to player Fun Arena -->")
                        self.player.playermodule(username)
                        break
                    else:
                        print("Enter Carefully.")
                        is_admin_menu = int(input(Config.ADMIN_MENU_PROMPT))
                    if is_admin_menu == 3:
                        self.mark_logout(username)
                        print("Exiting login Menu!!")
            else:
                print("Welcome to player Fun Arena -->")
                self.player.playermodule(username)
                self.mark_logout(username)
        # except Exception:
        #     print(Exception.__name__)
        #     print("login data not fetched successfully from login!!")
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
        # try:
        self.super_admin_module.super_admin_module()
        # except Exception:
        #     print(Exception.__name__)
        #     print("Super Module not accessed!!!!")
