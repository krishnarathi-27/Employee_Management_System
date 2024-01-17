import shortuuid
import sqlite3
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from src.utils.rbac import role_required
from src.utils.mapped_roles import MappedRole
from src.controllers.salary_controllers import SalaryControllers
from src.schemas.salary_schema import SalarySchema

blp = Blueprint("salary", __name__, description="Operations on salary")

salary_obj = SalaryControllers()

@blp.route("/salary")
class Salary(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    def get(self):
        data = salary_obj.view_salary()
        print(data)
        if data:
            return data
        else:
            abort(404, message="Resource not found")

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    @blp.arguments(SalarySchema)
    def post(self,salary_data):
        leave_id = "SID" + shortuuid.ShortUUID().random(length=4)
        try:  
            result = salary_obj.save_salary_status(salary_data['employee_id'],salary_data['salary_month'])

            if result: 
   
                return {"message" :"Leaves added successfully"}
            
            abort(500, message="Server not responding")
        except sqlite3.IntegrityError:
            abort(409, message="Resource already exists")
        except sqlite3.Error:
            abort(500, message="Server not responding")

@blp.route("/salary/<string:salary_id>")
class Salary(MethodView):

    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    def get(self):
        data = salary_obj.view_salary()
        print(data)
        if data:
            return data
        else:
            abort(404, message="Resource not found")


