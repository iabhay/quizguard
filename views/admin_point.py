from controllers.admincontroller import AdminController
from controllers.usercontroller import User
from controllers.questioncontroller import Question
from config.config import Config

class Admin:
    def __init__(self):
        self.admin_dict = {
            1: adm.add_user,
            2: adm.delete_user,
            3: adm.show_user,
            4: adm.show_all_user,
            5: adm.show_all_admins,
            6: adm.show_all_loggedin,
            7: adm.show_leaderboard,
            8: adm.add_question,
            9: adm.update_question,
            10: adm.delete_question,
            11: adm.show_question,
            12: adm.show_all_questions,
        }

    def adminmodule(self):
        try:
            print(Config.ADMIN_PROMPT)
            ask_user = int(input(Config.ENTER_CHOICE_PROMPT))
            if ask_user == 13:
                print("Exiting admin Module: ")
            while ask_user != 13:
                if ask_user >= 1 and ask_user < 13:
                    self.admin_dict[ask_user]()
                    print(Config.ADMIN_PROMPT)
                    ask_user = int(input(Config.ENTER_CHOICE_PROMPT))
                elif ask_user == 13:
                    print("Exiting admin Module: ")
                else:
                    print("Select Carefully!")
                    print(Config.ADMIN_PROMPT)
                    ask_user = int(input(Config.ENTER_CHOICE_PROMPT))

        except Exception:
            print(Exception.__name__)
            print("admin Module Controller not working!!")


adm = AdminController()
user = User()
ques = Question()
