import os
from fastapi import APIRouter, HTTPException, Body
from starlette import status
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from auth.login.login import Login

router = APIRouter()

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(user_data=Body()):
    """Login a new user"""
    login_obj = Login()
    res = login_obj.loginmodule(user_data["username"], user_data["password"])
    if res is None:
        raise HTTPException(400, detail="User not registered")
    else:
        if res[2] == "admin":
            res =  "batman"
        elif res[2] == "superadmin":
            res = "hanuman"
        elif res[2] == "player":
            res = "spiderman"
        token = create_access_token(res, user_data["username"], timedelta(minutes=15))
        return {"token": token,
                "message": f"{user_data["username"]} logged in successfully as {res}"}

def create_access_token(role: str, user_id: str, expires_delta: timedelta):
    encode = {'sub': role, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)   
