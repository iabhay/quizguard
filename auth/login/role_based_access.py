from config.config import Config
from utils.password_validator import password_validation
from views.admin_point import Admin
from views.player_point import Player

class RoleBasedAccess:
    def __init__(self) -> None:
        self.admin = Admin()
        self.player = Player()
    
    def role_based_entry_point(self, entry):
        if entry[2] == "admin":
           choice = self.is_admin(entry)
           if choice is None:
               return None
        else:
            self.player_access(entry)
            
    def is_admin(self, entry):
        is_admin_menu = int(input(Config.ADMIN_MENU_PROMPT))
        if is_admin_menu == 3:
            return None
        while is_admin_menu != 3:
            if is_admin_menu == 1:
                self.admin_access()
            elif is_admin_menu == 2:
                self.player_access(entry)
            else:
                print("Enter Carefully.")
            is_admin_menu = int(input(Config.ADMIN_MENU_PROMPT))
            if is_admin_menu == 3:
                return None
            
    def admin_access(self, entry):
        print("Welcome to admin Powers: -->")
        resp = self.admin.adminmodule()
        if resp is None:
            print("Exiting admin Module!!")

    def player_access(self, entry):
        print("Welcome to player Fun Arena -->")
        resp = self.player.playermodule(entry[0])
        if resp is None:
            print("Exiting Player Menu!!")