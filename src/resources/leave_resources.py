import shortuuid
import sqlite3
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from src.utils.rbac import role_required
from src.utils.mapped_roles import MappedRole
from src.controllers.leaves_controllers import LeavesControllers
from src.schemas.leave_schema import LeaveSchema, LeaveUpdateSchema

blp = Blueprint("leaves", __name__, description="Operations on leaves")

leave_obj = LeavesControllers()

@blp.route("/leave")
class Leave(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    def get(self):
        data = leave_obj.view_leaves()
        if data:
            return data
        else:
            abort(404, message="Resource not found")

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.EMPLOYEE_ROLE])
    @jwt_required()
    @blp.arguments(LeaveSchema)
    def post(self,leave_data):
        leave_id = "LID" + shortuuid.ShortUUID().random(length=4)
        try:  
            result = leave_obj.save_leaves(leave_id,leave_data['employee_id'],leave_data['leaves_date'])

            if result: 
   
                return {"message" :"Leaves added successfully"}
            
            abort(500, message="Server not responding")
        except sqlite3.IntegrityError:
            abort(409, message="Resource already exists")
        except sqlite3.Error:
            abort(500, message="Server not responding")

@blp.route("/leave/<string:leave_id>")
class LeaveId(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    @blp.arguments(LeaveUpdateSchema)    
    def patch(self,leave_data,leave_id):
        try:
            result = leave_obj.update_leaves(leave_data['leaves_status'],leave_id)
            return {"message" :"Leaves updated successfully"}
        except sqlite3.Error:
            abort(500, message="Server not responding")

@blp.route("/leave/<string:user_id>")
class LeaveUserId(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.EMPLOYEE_ROLE])
    @jwt_required()  
    def get(self,user_id):
        data = leave_obj.view_leaves_employee(user_id)
        if data:
            return data
        else:
            abort(404, message="Resource not found")