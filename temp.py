# from datetime import datetime
# from database.databaseconnection import DatabaseConnection
import hashlib
# user_file = "QUIZ.db"
        
# import sqlite3

# connection = sqlite3.connect(user_file)
# cursor = connection.cursor()
# tm = datetime.now()
# dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
password = "@Superadmin1234"
hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
# cursor.execute('INSERT INTO SCORES(date_time, username, highscore, isLoggedIn) VALUES (?,?, ?, ?)', (dt_string, "admin", 0, 0))
# cursor.execute('INSERT INTO USERS (username, password, role, is_changed) VALUES (?, ?, ?, ?)', ("admin", hashed_password, "admin", 0))
# cursor.execute('DELETE FROM SCORES WHERE username = "admin"')
# cursor.execute('DELETE FROM USERS WHERE username=?', ("admin", ))

# # Do some more SQL queries here
# cursor.close()
print(hashed_password)