from tabulate import tabulate
from database.databaseconnection import DatabaseConnection
from database.database_query import UsersTableQuery, ScoresTableQuery, QUESTIONSTableQuery, DatabasePath

class QuestionsDB:
    def __init__(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_create_user)
            cursor.execute(ScoresTableQuery.query_create_score)
            cursor.execute(QUESTIONSTableQuery.query_create_question)
            cursor.close()

    def add_question(self, ques_id, question, option1, option2, option3, option4, correct):
        try:
            with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
                cursor = connection.cursor()
                cursor.execute(QUESTIONSTableQuery.query_insert_question,
                            (ques_id, question, option1, option2, option3, option4, correct))
                cursor.close()
                return True
        except:
            return False

    def show_question(self, ques_id):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            ques = cursor.execute(QUESTIONSTableQuery.query_select_question, (ques_id,)).fetchone()
            cursor.close()
            if not ques:
                return None
            return ques

    def fetch_question(self, ques_id):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            ques = cursor.execute(QUESTIONSTableQuery.query_select_question, (ques_id,)).fetchone()
            cursor.close()
            if not ques:
                return None
            return ques

    def get_question(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            ques = cursor.execute(QUESTIONSTableQuery.query_get_one_question).fetchall()
            cursor.close()
            return ques

    def show_all_question(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            entry = cursor.execute(QUESTIONSTableQuery.query_select_all_question).fetchall()
            cursor.close()
            return entry

    def update_question(self, question, option1, option2, option3, option4, correct, ques_id):
        res = self.fetch_question(ques_id)
        if res:
            try:
                with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
                    cursor = connection.cursor()
                    cursor.execute(QUESTIONSTableQuery.query_update_question, (question, option1, option2, option3, option4, correct, ques_id))
                    cursor.close()
                    return True
            except:
                return False
        else:
            return None
        
    def delete_question(self, ques_id):
        res = self.fetch_question(ques_id)
        if res:
            try:
                with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
                    cursor = connection.cursor()
                    cursor.execute(QUESTIONSTableQuery.query_delete_question, (ques_id,))
                    cursor.close()
                    return True
            except:
                return False
        else:
            return None
                    
    def count_questions(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            res = cursor.execute(QUESTIONSTableQuery.query_get_question_table_length).fetchall()
            cursor.close()
            if not res:
                return 0
            return len(res)

    def get_last_id(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            res = cursor.execute(QUESTIONSTableQuery.query_get_last_ques_id).fetchone()
            cursor.close()
            if res[0]:
                return res[0] + 1
            return 1
