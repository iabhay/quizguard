from fastapi import APIRouter, HTTPException, Body
from starlette import status
from auth.register.register import Register
router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
def register_user(user_data=Body()):
    """Register a new user"""
    reg = Register()
    res = reg.register_module(user_data["username"], user_data["password"])
    if res is None:
        raise HTTPException(409, detail="User already registered")
    elif res is False:
        raise HTTPException(400, detail="Invalid password")
    else:
        return {
                "username": user_data["username"],
                "message": "User registered successfully"
                }
        
        