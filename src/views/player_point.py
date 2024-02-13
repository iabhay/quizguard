from controllers.player_controller import PlayerController
from config.config import Config
class Player:
    def __init__(self):
       self.player_controller = PlayerController()

    def playermodule(self, username):
        ask = int(input(Config.PLAYER_PROMPT))
        if ask == 4:
            return None
        while ask != 4:
            if ask == 1:
                self.question_intro()
                user_score = self.player_controller.playgame(username)
                self.question_outro(user_score)
            elif ask == 2:
                resp = self.player_controller.highscoreinfo(username)
                self.view_hishscore(resp)
            elif ask == 3:
                resp = self.player_controller.leaderboard()
            else:
                print("Please Select Carefully!")
            ask = int(input(Config.PLAYER_PROMPT))
            if ask == 4:
                return None

    def question_intro(self):
        print("We will give you 10 Questions.")
        print("Here your game starts...")
    
    def question_outro(self, user_score):
        print(f"You scored {user_score} out of 10.")

    def view_hishscore(self, resp):
        print(f"Last Played: {resp['Last Played']}\nUser: {resp['User']}\nRole: {resp['Role']}\nHighscore: {resp['Highscore']}\nLogin Status: {'Active' if resp['Login Status'] == 1 else 'Not-Active'}")