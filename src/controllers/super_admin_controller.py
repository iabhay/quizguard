from controllers.usercontroller import User
from controllers.admincontroller import AdminController
from fastapi import HTTPException

class SuperAdminController(AdminController):
    def __init__(self):
        super().__init__()
        self.user = User()

    def create_new_admin(self, username, password):
        return self.user.add_user(username, password, "admin", 0)

    def change_admin_to_user(self, username):
        try:
            self.userdb.update_admin_to_player(username)
            return True
        except:
            return None

    def change_user_to_admin(self, username):
        try:
            self.userdb.update_player_to_admin(username)
            return True
        except:
            return None

    def show_all_loggedin(self):
        self.score.show_all_loggedin()

    def delete_admin(self, username):
        entry = self.userdb.check_user(username)
        if not entry:
            raise HTTPException(404, detail="User not exist.")
        else:
            res = self.userdb.delete_admin_by_superadmin(username)
            if res is None:
                raise HTTPException(500, detail="Internal Server Error")
            elif res is False:
                raise HTTPException(409, detail="User not admin")
            return {
                "message": "Admin deleted successfully."
            }