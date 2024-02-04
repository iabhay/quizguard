import datetime
from database.databaseconnection import DatabaseConnection

user_file = "QUIZ.db"
def func():
    with DatabaseConnection(user_file) as connection:
        cursor = connection.cursor()
        # tm = datetime.now()
        # dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
        # cursor.execute('INSERT INTO SCORES(date_time, username, highscore, isLoggedIn) VALUES (?,?, ?, ?)', (dt_string, "superadmin", 0, 0))
        # cursor.execute('INSERT INTO USERS (username, password, role, is_changed) VALUES (?, ?, ?, ?)', ("superadmin", "superadmin", "superadmin", 0))
        cursor.execute('DELETE FROM USERS WHERE username=?', ("admin", ))
        cursor.execute('DELETE FROM SCORES WHERE username=?', ("admin", ))
        cursor.close()


func()