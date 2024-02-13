import pytest
from database.module_queries.scores_db import ScoresDB
from database.module_queries.users_db import UsersDB
from database.module_queries.question_db import QuestionsDB
from database.database_query import DatabasePath 

@pytest.fixture(scope='package',autouse=True)
def create_test_db(package_mocker):
    package_mocker.patch.object(DatabasePath,'MY_SQL_PATH',DatabasePath.TEST_PATH)
    ScoresDB()
    UsersDB()
    QuestionsDB()

