from fastapi import APIRouter, HTTPException, Body, Depends
from starlette import status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from controllers.admincontroller import AdminController
from controllers.usercontroller import User
from database.module_queries.users_db import UsersDB
from api_quiz.utils_api import role_required

router = APIRouter()


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/login')
token_dependency = Annotated[dict, Depends(oauth2_bearer)]

@router.get("/loggedin", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def view_all_logged_in(token: token_dependency):
    adm = AdminController()
    res = adm.show_all_loggedin()
    if res is None:
        raise HTTPException(404, detail="Data Not Found")
    response = {}
    id = 1
    for tup in res:
        curr = {
            "last_played_time": tup[0],
            "username": tup[1],
            "highscore": tup[2]
        }
        response[id] = curr
        id += 1
    return response


@router.post("/user", status_code=status.HTTP_201_CREATED)
@role_required(["batman", "hanuman"])
def add_user(token: token_dependency, user_data=Body()):
    user = User()
    res = user.add_user(username=user_data["username"], password=user_data["password"])
    if res is False:
        raise HTTPException(400, detail="Invalid Details!")
    elif res is None:
        raise HTTPException(409, detail="User already Exists.")
    return {
        "username": user_data["username"],
        "message": "User Added Successfully."
    }




@router.delete("/user", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def delete_user(token: token_dependency, user_data=Body()):
    userdb = UsersDB()
    res = userdb.delete_user_by_admin(user_data["username"])
    if res is False:
        raise HTTPException(500, detail="User Not deleted.")
    return {
        "message": "User deleted Successfully."
    }

@router.get("/users", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def view_all_users(token: token_dependency):
    user = User()
    res = user.show_all_user()
    response = {}
    id = 1
    for tup in res:
        curr = {
            "last_played_time": tup[0],
            "username": tup[1],
            "role": tup[2],
            "highscore": tup[3],
            "Login Status": tup[4],
        }
        response[id] = curr
        id += 1
    return response

@router.get("/show-admins", status_code=status.HTTP_200_OK)
@role_required(["batman", "hanuman"])
def view_all_admins(token: token_dependency):
    adm = AdminController()
    res = adm.show_all_admins()
    response = {}
    id = 1
    for tup in res:
        curr = {
            "last_played_time": tup[1],
            "username": tup[0],
            "highscore": tup[2],
            "Login Status": tup[3],
        }
        response[id] = curr
        id += 1
    return response
