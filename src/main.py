from fastapi import FastAPI
from config.config import Config
from api_quiz.resources.admin_endpoints import router as admin_router
from api_quiz.resources.login_user import router as login_router
from api_quiz.resources.player_res import router as player_router
from api_quiz.resources.question_endpoints import router as question_router
from api_quiz.resources.register_user import router as register_router
from api_quiz.resources.superadmin_endpoints import router as superadmin_router

# if __name__ == "__main__":
Config.load()
app = FastAPI()
app.include_router(admin_router)
app.include_router(player_router)
app.include_router(question_router)
app.include_router(superadmin_router)
app.include_router(login_router)
app.include_router(register_router)