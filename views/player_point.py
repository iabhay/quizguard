from controllers.player_controller import PlayerController
from config.config import Config

class Player:
    def __init__(self):
       self.player_controller = PlayerController()

    def playermodule(self, username):
        print(f"You are logged in successfully.")
        ask = int(input(Config.PLAYER_PROMPT))
        if ask == 4:
            print("Exiting login Menu.!!")
        while ask != 4:
            ask = int(input(Config.PLAYER_PROMPT))
            if ask == 1:
                self.player_controller.playgame(username)
            elif ask == 2:
                self.player_controller.highscoreinfo(username)
            elif ask == 3:
                self.player_controller.leaderboard()
            elif ask == 4:
                print(f"Exiting Player Menu!!")
                break
            else:
                print("Please Select Carefully!")
                ask = int(input(Config.PLAYER_PROMPT))