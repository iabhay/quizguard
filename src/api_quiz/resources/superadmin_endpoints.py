from fastapi import APIRouter, HTTPException, Body, Path
from starlette import status
from controllers.super_admin_controller import SuperAdminController
from api_quiz.utils_api import role_required
from api_quiz.resources.admin_endpoints import token_dependency, oauth2_bearer

router = APIRouter()


@router.post("/admin", status_code=status.HTTP_201_CREATED)
@role_required(["hanuman"])
def super_admin_module(token: token_dependency, admin_data=Body()):
    super_admin_obj = SuperAdminController()
    res = super_admin_obj.create_new_admin(admin_data["username"], admin_data["password"])
    if res is None:
        raise HTTPException(400, detail="Not working.")
    if res is False:
        raise HTTPException(400, detail="Validation failed.")
    return {
        "message": "Admin added successfully."
    }
  
@router.delete("/admin", status_code=status.HTTP_200_OK)
@role_required(["hanuman"])
def delete_admin(token: token_dependency, admin_data=Body()):
    super_admin_obj = SuperAdminController()
    res = super_admin_obj.delete_admin(admin_data["username"])
    if res is None:
        raise HTTPException(400, detail="Not working.")
    if res is False:
        raise HTTPException(400, detail="Admin not found.")
    return {
        "message": "Admin deleted successfully."
    }



@router.put("/admin/to_user/{username}", status_code=status.HTTP_200_OK)
@role_required(["hanuman"])
def admin_to_user(token: token_dependency, username=Path()):
    super_admin_obj = SuperAdminController()
    res = super_admin_obj.change_admin_to_user(username)
    if res is None:
        raise HTTPException(400, detail="Role Changing not possible.")
    return {
        "message": "Role Changing successful."
    }


@router.post("/user/to_admin/{username}", status_code=status.HTTP_200_OK)
@role_required(["hanuman"])
def user_to_admin(token: token_dependency, username=Path()):
    super_admin_obj = SuperAdminController()
    res = super_admin_obj.change_user_to_admin(username)
    if res is None:
        raise HTTPException(400, detail="Role Changing not possible.")
    return {
        "message": "Role Changing successful."
    }