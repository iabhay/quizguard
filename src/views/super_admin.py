from config.config import Config
from controllers.super_admin_controller import SuperAdminController


class SuperAdminModule:
    def __init__(self):
        super_admin = SuperAdminController()
        self.super_admin_dict = {
            1: super_admin.create_new_admin,
            2: super_admin.change_admin_to_user,
            3: super_admin.delete_admin,
            4: super_admin.add_user,
            5: super_admin.change_user_to_admin,
            6: super_admin.delete_admin,
            7: super_admin.show_user,
            8: super_admin.show_all_user,
            9: super_admin.show_all_admins,
            10: super_admin.show_all_loggedin,
            11: super_admin.show_leaderboard,
            12: super_admin.add_question,
            13: super_admin.update_question,
            14: super_admin.delete_question,
            15: super_admin.show_question,
            16: super_admin.show_all_questions,
        }

    def super_admin_module(self):
        # try:
        print(Config.SUPER_ADMIN_PROMPT)
        ask_user = int(input("Enter Choice:"))
        if ask_user == 17:
            print("Exiting admin Module: ")
        while ask_user != 17:
            if 1 > ask_user > 17:
                print("Please Select Carefully!!")
                print(Config.SUPER_ADMIN_PROMPT)
                ask_user = int(input("Enter Choice:"))
                if ask_user == 17:
                    print("Exiting admin Module: ")
            else:
                self.super_admin_dict[ask_user]()
                print(Config.SUPER_ADMIN_PROMPT)
                ask_user = int(input("Enter Choice:"))
                if ask_user == 17:
                    print("Exiting admin Module: ")
                    return None
        return None
        # except Exception:
        #     print(Exception.__name__)
        #     print("Super admin Module Controller not working!!")