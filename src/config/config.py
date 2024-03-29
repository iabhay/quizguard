import yaml

FPATH = 'config/config.yml'
GENERALCONFIGPATH = 'config/general_config.yml'
QUESTIONSQUERYPATH = 'config/questions_table_query.yml'
SCORESQUERYPATH = 'config/scores_table_query.yml'
USERSQUERYPATH = 'config/users_table_query.yml'

class Config:
    """
    Maintains all the config variables of the game
    """
    QUIZ = None
    MAIN_PROMPT = None
    ADMIN_PROMPT = None
    PLAYER_PROMPT = None
    SUPER_ADMIN_PROMPT = None
    SECURE_PASSWORD_PROMPT = None
    ADMIN_MENU_PROMPT = None
    ENTER_CHOICE_PROMPT = None
    ENTRY_STATEMENT: None
    EXITING_GAME: None
    MESSAGE_FOR_WRONG_INPUT: None
    ENTER_USERNAME: None
    # ENTER_USERNAME_PROMPT: None
    ENTER_PASSWORD: None
    PASSWORD_VALIDATOR_PATTERN: None
    INVALID_PASSWORD: None
    REGISTRATION_SUCCESS_MESSAGE: None
    REGISTRATION_NOT_SUCCESSFUL: None
    ALREADY_REGISTERED: None
    INVALID_CREDENTIALS: None
    LOGIN_SUCCESS_MESSAGE: None
    EXIT_LOGIN_MENU: None
    WELCOME_ADMIN: None
    WELCOME_PLAYER: None
    WELCOME_SUPER_ADMIN: None
    GAME_STARTING: None
    HIGHSCORE_UPDATE_MESSAGE: None
    ROLE_CHANGED: None
    ADMIN_CREATED: None
    ENTER_PROMPT_TO_CHANGE_ROLE: None
    CONFIRMATION_PROMPT: None
    DELETED_SUCCESSFULLY: None
    QUESTION_ADDED: None
    QUESTION_DELETED: None
    QUESTION_UPDATED: None
    QUESTION_ID_NOT_FOUND: None
    ENTER_QUESTION_ID: None
    EXITING_ADMIN: None
    EXITING_SUPERADMIN: None
    query_create_question: None
    query_insert_question: None
    query_update_question: None
    query_delete_question: None
    query_select_question: None
    query_select_all_question: None
    query_get_question_table_length: None
    query_get_last_ques_id: None
    query_insert_user: None
    query_create_user: None
    query_select_user: None
    query_delete_user: None
    query_delete_user_by_admin: None
    query_select_all_user:  None
    query_select_all_admin: None
    query_update_role:  None
    query_check_existence:  None
    query_update_pasword:   None
    query_update_pasword_by_admin:  None
    query_create_score: None
    query_insert_score: None
    query_delete_score: None
    query_select_userscore: None
    query_leaderboard: None
    query_update_score: None
    query_update_login_status: None
    query_select_all_loggedin: None
    query_select_all_user: None

    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUIZ = data['QUIZ']
            cls.MAIN_PROMPT = data['MAIN_PROMPT']
            cls.ADMIN_PROMPT = data['ADMIN_PROMPT']
            cls.PLAYER_PROMPT = data['PLAYER_PROMPT']
            cls.SUPER_ADMIN_PROMPT = data['SUPER_ADMIN_PROMPT']
            cls.SECURE_PASSWORD_PROMPT = data['SECURE_PASSWORD_PROMPT']
            cls.ADMIN_MENU_PROMPT = data['ADMIN_MENU_PROMPT']
            cls.ENTER_CHOICE_PROMPT = data['ENTER_CHOICE_PROMPT']

        with open(GENERALCONFIGPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.ENTRY_STATEMENT = data['ENTRY_STATEMENT']
            cls.EXITING_GAME = data['EXITING_GAME']
            cls.MESSAGE_FOR_WRONG_INPUT = data['MESSAGE_FOR_WRONG_INPUT']
            cls.ENTER_USERNAME = data['ENTER_USERNAME']
            # cls.ENTER_USERNAME = data['ENTER_USERNAME_PROMPT']
            cls.ENTER_PASSWORD = data['ENTER_PASSWORD']
            cls.PASSWORD_VALIDATOR_PATTERN = data['PASSWORD_VALIDATOR_PATTERN']
            cls.INVALID_PASSWORD = data['INVALID_PASSWORD']
            cls.REGISTRATION_SUCCESS_MESSAGE = data['REGISTRATION_SUCCESS_MESSAGE']
            cls.REGISTRATION_NOT_SUCCESSFUL = data['REGISTRATION_NOT_SUCCESSFUL']
            cls.ALREADY_REGISTERED = data['ALREADY_REGISTERED']
            cls.INVALID_CREDENTIALS = data['INVALID_CREDENTIALS']
            cls.LOGIN_SUCCESS_MESSAGE = data['LOGIN_SUCCESS_MESSAGE']
            cls.EXIT_LOGIN_MENU = data['EXIT_LOGIN_MENU']
            cls.WELCOME_ADMIN = data['WELCOME_ADMIN']
            cls.WELCOME_PLAYER = data['WELCOME_PLAYER']
            cls.WELCOME_SUPER_ADMIN = data['WELCOME_SUPER_ADMIN']
            cls.GAME_STARTING = data['GAME_STARTING']
            cls.HIGHSCORE_UPDATE_MESSAGE = data['HIGHSCORE_UPDATE_MESSAGE']
            cls.ROLE_CHANGED = data['ROLE_CHANGED']
            cls.ADMIN_CREATED = data['ADMIN_CREATED']
            cls.ENTER_PROMPT_TO_CHANGE_ROLE = data['ENTER_PROMPT_TO_CHANGE_ROLE']
            cls.CONFIRMATION_PROMPT = data['CONFIRMATION_PROMPT']
            cls.DELETED_SUCCESSFULLY = data['DELETED_SUCCESSFULLY']
            cls.QUESTION_ADDED = data['QUESTION_ADDED']
            cls.QUESTION_DELETED = data['QUESTION_DELETED']
            cls.QUESTION_UPDATED = data['QUESTION_UPDATED']
            cls.QUESTION_ID_NOT_FOUND = data['QUESTION_ID_NOT_FOUND']
            cls.ENTER_QUESTION_ID = data['ENTER_QUESTION_ID']
            cls.EXITING_ADMIN = data['EXITING_ADMIN']
            cls.EXITING_SUPERADMIN = data['EXITING_SUPERADMIN']

        with open(QUESTIONSQUERYPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.query_create_question = data['query_create_question']
            cls.query_insert_question = data['query_insert_question']
            cls.query_update_question = data['query_update_question']
            cls.query_delete_question = data['query_delete_question']
            cls.query_select_question = data['query_select_question']
            cls.query_select_all_question = data['query_select_all_question']
            cls.query_get_question_table_length = data['query_get_question_table_length']
            cls.query_get_last_ques_id = data['query_get_last_ques_id']

        with open(USERSQUERYPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.query_insert_user = data['query_insert_user']
            cls.query_create_user = data['query_create_user']
            cls.query_select_user = data['query_select_user']
            cls.query_delete_user = data['query_delete_user']
            cls.query_delete_user_by_admin = data['query_delete_user_by_admin']
            cls.query_select_all_user = data['query_select_all_user']
            cls.query_select_all_admin = data['query_select_all_admin']
            cls.query_update_role = data['query_update_role']
            cls.query_check_existence = data['query_check_existence']
            cls.query_update_pasword = data['query_update_pasword']
            cls.query_update_pasword_by_admin = data['query_update_pasword_by_admin']

        with open(SCORESQUERYPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.query_create_score = data['query_create_score']
            cls.query_insert_score = data['query_insert_score']
            cls.query_delete_score = data['query_delete_score']
            cls.query_select_userscore = data['query_select_userscore']
            cls.query_leaderboard = data['query_leaderboard']
            cls.query_update_score = data['query_update_score']
            cls.query_update_login_status = data['query_update_login_status']
            cls.query_select_all_loggedin = data['query_select_all_loggedin']
            cls.query_select_all_user = data['query_select_all_user']


