from fastapi import APIRouter, HTTPException, Body, Path
from starlette import status
from controllers.player_controller import PlayerController
from api_quiz.utils_api import role_required
from api_quiz.resources.admin_endpoints import token_dependency, oauth2_bearer

router = APIRouter()

@router.get("/profile/{username}", status_code=status.HTTP_200_OK)
@role_required(["spiderman", "batman", "hanuman"])
def player_module(token: token_dependency, username=Path()):
    if username == "superadmin":
        raise HTTPException(400, detail="Profile Not available.")
    pc_obj = PlayerController()
    res = pc_obj.highscoreinfo(username)
    if res is None:
        raise HTTPException(400, detail="{Profile data not found.}")
    return {"last_played": res["Last Played"],
                "user": res["User"],
                "highscore":res["Highscore"],
                "login_status": res["Login Status"]
            }
    

@router.get("/leaderboard", status_code=status.HTTP_200_OK)
@role_required(["spiderman", "batman", "hanuman"])
def common_module(token: token_dependency):
    pc_obj = PlayerController()
    res = pc_obj.leaderboard()
    if res is None:
        raise HTTPException(400, message="{Data not found.}")
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