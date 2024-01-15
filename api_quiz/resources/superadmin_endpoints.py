from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from api_quiz.utils_api import role_required
from controllers.super_admin_controller import SuperAdminController
from schemas import UserSchema, UsernameSchema
blp = Blueprint("Superadmin", __name__, description="Superadmin")


@blp.route("/admin")
class SuperAdminModule(MethodView):
    def __init__(self):
        self.super_admin_obj = SuperAdminController()
    
    @role_required(["hanuman"])
    @jwt_required()
    @blp.arguments(UserSchema)
    def post(self, admin_data):
        res = self.super_admin_obj.create_new_admin(admin_data["username"], admin_data["password"])
        if res is None:
            abort(400, message="Not working.")
        if res is False:
            abort(400, message="Validation failed.")
        return {
            "message": "Admin added successfully."
        }
    
    @role_required(["hanuman"])
    @jwt_required()
    @blp.arguments(UsernameSchema)
    def delete(self, admin_data):
        res = self.super_admin_obj.delete_admin(admin_data["username"], admin_data["password"])
        if res is None:
            abort(400, message="Not working.")
        if res is False:
            abort(400, message="Admin not found.")
        return {
            "message": "Admin deleted successfully."
        }




@blp.route("/admin/to_user/<string:username>", methods=["POST"])
@role_required(["hanuman"])
@jwt_required()
def admin_to_user(username):
    super_admin_obj = SuperAdminController()
    res = super_admin_obj.change_admin_to_user(username)
    if res is None:
        abort(400, message="Role Changing not possible.")
    return {
        "message": "Role Changing successful."
    }


@blp.route("/user/to_admin/<string:username>", methods=["POST"])
@role_required(["hanuman"])
@jwt_required()
def user_to_admin(username):
    super_admin_obj = SuperAdminController()
    res = super_admin_obj.change_user_to_admin(username)
    if res is None:
        abort(400, message="Role Changing not possible.")
    return {
        "message": "Role Changing successful."
    }