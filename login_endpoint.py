from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm
from auth.login.login import Login
from database.module_queries.users_db import UsersDB
from passlib.context import CryptContext
from jose import jwt


app = FastAPI()

# SECRET_KEY = None
# ALGORITHM = 'HS256'

# bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def authenticate_user(username, password):
    login_obj = Login()
    check = login_obj.loginmodule(username, password)
    if check is None:
        return False
    else:
        return True


@app.post('/token')
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    return 'Successful' if user else 'Failed'