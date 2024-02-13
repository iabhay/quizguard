import random
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB

class PlayerController:
    def __init__(self):
        self.user = UsersDB()
        self.score = ScoresDB()
        self.ques = QuestionsDB()

    def playgame(self, username):
        user_score = 0
        content = self.ques.get_question()
        for curr_content in content:
            user_score += self.question(curr_content)
        self.highscorer(username, user_score)
        return user_score

    def highscorer(self, name, score):
        entry = self.score.fetch_player_score(name)
        if entry < score:
            self.score.update_player_score(name, score)

    def highscoreinfo(self, name):
        return self.score.show_player_score(name)

    def leaderboard(self):
        return self.score.show_leaderboard()

    def question(self, curr_content):
        my_options = [curr_content[2], curr_content[3], curr_content[4], curr_content[5]]
        correct_option_ind = curr_content[6]
        option_dict = {
            "A": 1,
            "B": 2,
            "C":3,
            "D":4
        }
        correct_option = curr_content[option_dict[correct_option_ind]]
        random.shuffle(my_options)
        current_score = self.show_question(curr_content[1], my_options, correct_option)
        return current_score

    def show_question(self, question, options, correct_option):
        ask_option = int(input("Write correct option (1,2,3,4) : "))
        while ask_option <= 0 or ask_option >= 5:
            ask_option = int(input("Write correct option (1,2,3,4) : "))
        if options[ask_option-1] == correct_option:
            return 1
        return 0
