from pwinput import pwinput
from controllers.questioncontroller import Question
from database.module_queries.users_db import UsersDB
from database.module_queries.question_db import QuestionsDB
from database.module_queries.scores_db import ScoresDB
from controllers.usercontroller import User
from config.config import Config
from controllers.usercontroller import User


class AdminController(User):
    def __init__(self):
            super().__init__()
            self.ques = Question()

    def add_user(self, role="player", is_Changed=1):
        User.add_user(role="player", is_changed=0)

    def update_user_password(self):
        username = input("Enter Username: ")
        new_password = pwinput(Config.SECURE_PASSWORD_PROMPT,"*")
        self.userdb.update_user_password_by_admin(username, new_password)

    def show_all_admins(self):
        return self.userdb.read_all_admin()

    def show_all_loggedin(self):
        return self.score.show_all_loggedin()

    def delete_user(self, username):
        return self.userdb.delete_user_by_admin(username)

    def add_question(self):
        return self.ques.add_question()

    def show_question(self):
        try:
            total_ques = self.quesdb.count_questions()
            ques_id = int(input(f"Enter Question ID to show details: "))
            self.ques.show_question_by_id(ques_id)
        except Exception:
            return None
        
    def show_all_questions(self):
        self.ques.show_all_questions()

    def update_question(self):
        ques_id = int(input(f"Enter Question ID to update details: "))
        self.ques.update_question_by_id(ques_id)

    def delete_question(self):
        total_ques = self.quesdb.count_questions()
        ques_id = int(input(f"Enter Question ID to delete details: "))
        self.ques.delete_question_by_id(ques_id)