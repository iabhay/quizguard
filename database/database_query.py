"""
This module is for managing all the queries
Tables - Users, Score, QUESTIONSINFO
"""


class UsersTableQuery:
    query_insert_user = 'INSERT INTO USERS (username, password, role, is_changed) VALUES (?, ?, ?, ?)'
    query_create_user = 'CREATE TABLE IF NOT EXISTS USERS (username text, password, role text, is_changed INTEGER)'
    query_select_user = 'SELECT * FROM USERS WHERE username=? AND password=?'
    query_delete_user = 'DELETE FROM USERS WHERE username=? AND password=?'
    query_delete_user_by_admin = 'DELETE FROM USERS WHERE username=? AND role="player"'
    query_select_all_user = 'SELECT * FROM USERS'
    query_select_all_admin = ('SELECT USERS.username, SCORES.date_time, SCORES.highscore, SCORES.isLoggedIn FROM USERS INNER JOIN SCORES ON USERS.role="admin" AND USERS.username = SCORES.username')
    query_update_role = 'UPDATE USERS SET role=? where username=?'
    query_check_existence = 'SELECT * from USERS WHERE username=?'
    query_update_pasword = 'UPDATE USERS SET password=? where (username=? AND password=?)'
    query_update_pasword_by_admin = 'UPDATE USERS SET password=? WHERE username=?'
    query_check_password_status = 'SELECT is_changed from USERS WHERE username=?'
    query_delete_admin = 'DELETE FROM USERS WHERE username = ?'
    

class ScoresTableQuery:
    query_create_score = ('CREATE TABLE IF NOT EXISTS SCORES(date_time text, username text, highscore INT, '
                          'isLoggedIn INT)')
    query_insert_score = 'INSERT INTO SCORES(date_time, username, highscore, isLoggedIn) VALUES (?,?, ?, ?)'
    query_delete_score = 'DELETE FROM SCORES WHERE username=?'
    query_select_userscore = 'SELECT SCORES.date_time,SCORES.username,USERS.role,SCORES.highscore, SCORES.isLoggedIn FROM SCORES INNER JOIN USERS ON USERS.username = SCORES.username WHERE USERS.username=?'
    query_leaderboard = 'SELECT * FROM SCORES ORDER BY highscore DESC,date_time DESC LIMIT 10'
    query_update_score = 'UPDATE SCORES SET date_time=?, highscore=? WHERE username = ?'
    query_update_login_status = 'UPDATE SCORES SET isLoggedIn=? WHERE username=?'
    query_select_all_loggedin = 'SELECT * FROM SCORES WHERE isLoggedIn=?'
    query_select_all_user = 'SELECT SCORES.date_time,SCORES.username,USERS.role,SCORES.highscore, SCORES.isLoggedIn FROM SCORES INNER JOIN USERS ON USERS.username = SCORES.username WHERE USERS.role="player"'
    query_fetch_score= 'SELECT highscore FROM SCORES WHERE username=?'

class QUESTIONSTableQuery:
    query_create_question = ('CREATE TABLE IF NOT EXISTS QUESTIONSINFO(ques_id INT PRIMARY KEY, question text, option1 '
                             'text,'
                             'option2 text, option3 text, option4 text, correct text)')
    query_insert_question = ('INSERT INTO QUESTIONSINFO (ques_id, question, option1, '
                             'option2, option3, option4, correct) VALUES (?,?,?,?,?,?,?)')
    query_update_question = ('UPDATE QUESTIONSINFO SET question=? , option1=? , option2=? , option3=? , option4=? , correct=? WHERE ques_id=?')
    query_delete_question = 'DELETE FROM QUESTIONSINFO WHERE ques_id=?'
    query_select_question = ('SELECT ques_id, question, option1, option2, option3, option4, correct '
                             'FROM QUESTIONSINFO WHERE ques_id=?')
    query_select_all_question = 'SELECT * FROM QUESTIONSINFO'
    query_get_question_table_length = 'SELECT * FROM QUESTIONSINFO'
    query_get_last_ques_id = 'SELECT * FROM QUESTIONSINFO ORDER BY ques_id DESC LIMIT 1'
    query_get_one_question = 'SELECT * FROM QUESTIONSINFO LIMIT 1 OFFSET ABS(RANDOM()) % MAX(( SELECT COUNT(*) FROM QUESTIONSINFO), 1)'
