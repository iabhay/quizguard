from database.module_queries.question_db import QuestionsDB


class Question:
    def __init__(self):
        self.quesdb = QuestionsDB()

    def add_question(self):
        try:
            i = self.quesdb.get_last_id()
            question, option_a, option_b, option_c, option_d, correct = self.question_input()
            self.quesdb.add_question(i, question, option_a, option_b, option_c, option_d, correct)
            print("Question Added Successfully!!")
            return True
        except Exception as e:
            print(e)
            print("Adding Question failed by admin!!")
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
        # try:
        ques_data = self.quesdb.show_question(ques_id)
        if not ques_data:
            print("No Such Question ID Found!!")
        else:
            print(f"Question: {ques_data[1]}\nOptions:\nA. {ques_data[2]}\n"
                  f"B. {ques_data[3]}\nC. {ques_data[4]}\nD. {ques_data[5]}\nCorrect: {ques_data[6]}")
            new_data = self.question_input()
            question = new_data[0]
            option_a = new_data[1]
            option_b = new_data[2]
            option_c = new_data[3]
            option_d = new_data[4]
            correct = new_data[5]
            self.quesdb.update_question(question, option_a, option_b, option_c, option_d, correct, ques_id)
            print("Question Updated Successfully!!")
        # except Exception:
        #     print(Exception.__name__)
        #     print("Updating Question failed by admin!!")

    def delete_question_by_id(self, ques_id):
        try:
            self.quesdb.delete_question(ques_id)
            print("Question Deleted Successfully!!")
        except:
            print("No Such Id Found!!")

    def show_question_by_id(self, ques_id):
        try:
            entry = self.quesdb.show_question(ques_id)
            if not entry:
                print("No Such ID Found!!")
            else:
                print(f"QuestionID : {entry[0]}\nQuestion : {entry[1]}\nOption-A : {entry[2]}\nOption-B : {entry[3]}\nOption-C : {entry[4]}\nOption-D : {entry[5]}\nCorrect Option : {entry[6]}")
        except Exception:
            print(Exception.__name__)
            print("Showing Question to admin failed!!")
