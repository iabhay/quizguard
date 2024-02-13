from datetime import datetime
from database.databaseconnection import DatabaseConnection
from database.database_query import UsersTableQuery, ScoresTableQuery, QUESTIONSTableQuery, DatabasePath
from utils.Exception_Handler.sql_exception_handler import exception_handler


class ScoresDB:
    def __init__(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_create_user)
            cursor.execute(ScoresTableQuery.query_create_score)
            cursor.execute(QUESTIONSTableQuery.query_create_question)
            cursor.close()

    def update_player_score(self, username, highscore):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            tm = datetime.now()
            dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute(ScoresTableQuery.query_update_score, (dt_string, highscore, username))
            cursor.close()

    def show_leaderboard(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            table = cursor.execute(ScoresTableQuery.query_leaderboard).fetchall()
            cursor.close()
            return table

    def show_player_score(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            player_score = cursor.execute(ScoresTableQuery.query_select_userscore, (username, )).fetchone()
            cursor.close()
            if not player_score:
                return None
            response = {"Last Played": player_score[0],
                    "User": player_score[1],
                    "Role": player_score[2],
                    "Highscore":player_score[3],
                    "Login Status": 'Active' if player_score[4] == 1 else 'Not-Active'}
            return response

    def fetch_player_score(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            player_score = cursor.execute(ScoresTableQuery.query_fetch_score, (username, )).fetchone()
            cursor.close()
            if player_score is None:
                return 0
            return player_score[0]

    def mark_login(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(ScoresTableQuery.query_update_login_status, (1, username))
            cursor.close()

    def mark_logout(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(ScoresTableQuery.query_update_login_status, (0, username))
            cursor.close()


    def check_login(self, username, password):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            entry = cursor.execute(ScoresTableQuery.query_select_user, (username, password)).fetchone()
            cursor.close()
            return entry


    def show_all_user(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            table = cursor.execute(ScoresTableQuery.query_select_all_user).fetchall()
            cursor.close()
            return table


    def show_all_loggedin(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            table = cursor.execute(ScoresTableQuery.query_select_all_loggedin, (1,)).fetchall()
            cursor.close()
            if len(table)> 0:
                return table
            return None
