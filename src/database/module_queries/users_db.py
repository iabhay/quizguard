from datetime import datetime
from database.databaseconnection import DatabaseConnection
from database.database_query import UsersTableQuery, ScoresTableQuery, QUESTIONSTableQuery, DatabasePath
from fastapi import HTTPException

class UsersDB:

    def __init__(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_create_user)
            cursor.execute(ScoresTableQuery.query_create_score)
            cursor.execute(QUESTIONSTableQuery.query_create_question)
            cursor.close()

    def create_user(self, username, password, role, is_changed=1):
        
        try:
            with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
                cursor = connection.cursor()
                cursor.execute(UsersTableQuery.query_insert_user, (username, password, role, is_changed))
                tm = datetime.now()
                dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
                cursor.execute(ScoresTableQuery.query_insert_score, (dt_string, username, 0, 0))
                cursor.close()
                return True
        except:
            return False

    def delete_user(self, username, password):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_delete_user, (username, password))
            cursor.execute(ScoresTableQuery.query_delete_score, (username,))
            cursor.close()


    def delete_user_by_admin(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            is_exist = cursor.execute(UsersTableQuery.query_select_user_by_admin, (username, )).fetchone()
            if not is_exist:
                raise HTTPException(404, detail="User not exist")
            if is_exist[2] == "admin" or is_exist[2] == "superadmin":
                raise HTTPException(403, detail="User can't be deleted")
            cursor.execute(UsersTableQuery.query_delete_user_by_admin, (username,))
            cursor.execute(ScoresTableQuery.query_delete_score, (username,))
            cursor.close()
            return True

    def read_all_admin(self):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            table = cursor.execute(UsersTableQuery.query_select_all_admin).fetchall()
            cursor.close()
            return table


    def update_admin_to_player(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_role, ("player", username))
            cursor.close()


    def update_player_to_admin(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_role, ("admin", username))
            cursor.close()


    def check_user(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            count = cursor.execute(UsersTableQuery.query_check_existence, (username, )).fetchall()
            cursor.close()
            if not count:
                return False
            return True


    def update_user_password(self, username, password, new_password):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_pasword, (new_password, username, password))
            cursor.close()


    def update_user_password_by_admin(self, username, new_password):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_pasword_by_admin, (new_password, username))
            cursor.close()


    def check_login(self, username, password):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            res = cursor.execute(UsersTableQuery.query_select_user, (username, password)).fetchone()
            cursor.close()
            if not res:
                return None
            return res

    def delete_admin_by_superadmin(self, username):
        with DatabaseConnection(DatabasePath.MY_SQL_PATH) as connection:
            cursor = connection.cursor()
            try:
                entry = cursor.execute(UsersTableQuery.query_select_user_by_admin, (username, )).fetchone()
                if entry[2] == "admin" or entry[2] == "superadmin":
                    cursor.execute(UsersTableQuery.query_delete_admin, (username,))
                    cursor.execute(ScoresTableQuery.query_delete_score, (username,))
                    return True
                else:
                    return False
            except:
                return None


