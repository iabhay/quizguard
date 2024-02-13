from database.module_queries.question_db import QuestionsDB


class Question:
    def __init__(self):
        self.quesdb = QuestionsDB()

    def add_question(self):
        try:
            i = self.quesdb.get_last_id()
            question, option_a, option_b, option_c, option_d, correct = self.question_input()
            self.quesdb.add_question(i, question, option_a, option_b, option_c, option_d, correct)
            return True
        except Exception as e:
            return False

    def question_input(self):
        question = input("Enter question: ")
        option_a = input("Enter Option A: ")
        option_b = input("Enter Option B: ")
        option_c = input("Enter Option C: ")
        option_d = input("Enter Option D: ")
        correct = input("Enter correct option -> 'A','B','C','D'\n=>")
        return [question, option_a, option_b, option_c, option_d, correct]

    def show_all_questions(self):
        self.quesdb.show_all_question()

    def update_question_by_id(self, ques_id):
        ques_data = self.quesdb.show_question(ques_id)
        if not ques_data:
            return None
        else:
            return ques_data

    def delete_question_by_id(self, ques_id):
        try:
            self.quesdb.delete_question(ques_id)
        except:
            pass

    def show_question_by_id(self, ques_id):
        try:
            entry = self.quesdb.show_question(ques_id)
            if not entry:
                return None
            else:
                return entry
        except Exception:
            print(Exception.__name__)
