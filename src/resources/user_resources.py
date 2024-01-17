import shortuuid
import sqlite3
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from src.utils.rbac import role_required
from src.utils.mapped_roles import MappedRole
from src.controllers.admin_controllers import AdminControllers
from src.controllers.employee_controllers import EmployeeControllers

from src.schemas.user_schema import UserDetailSchema

blp = Blueprint("users", __name__, description="Operations on users")

admin_obj = AdminControllers()
emp_obj = EmployeeControllers()

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
domain = os.getenv('MAILGUN_DOMAIN')
api_key = os.getenv('MAILGUN_API_KEY')

def send_simple_message(to, subject, body):
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", f"{api_key}"),
		data={"from": f"Excited User <mailgun@{domain}>",
			"to": [to],
			"subject": subject,
			"text": body})

@blp.route("/user")
class User(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    def get(self):
        data = admin_obj.view_user()
        if data:
            return data
        else:
            abort(404, message="Resource not found")

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    @blp.arguments(UserDetailSchema)
    def post(self,user_data):
        employee_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        try:  
            result = admin_obj.create_new_user(employee_id,user_data['role'],user_data['username'],user_data['password'],user_data['age'],
                                      user_data['mail'],user_data['gender'],user_data['phone'])

            if result: 
                send_simple_message(
                    to=user_data['mail'],
                    subject="Successfully registered",
                    body=f"Hi {user_data['username']}! You have sucessfully registered into employee management system."
                )
                return {"message" :"User created successfully"}
            
            abort(500, message="Server not responding")
        except sqlite3.IntegrityError:
            abort(409, message="Resource already exists")
        except sqlite3.Error:
            abort(500, message="Server not responding")

@blp.route("/user/<string:user_id>")
class UserwithId(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @jwt_required()
    def delete(self,user_id):
        try:
            result = admin_obj.delete_exisiting_user(user_id)
            if result:
                return {"message": "User deleted successfully"}
            
            abort(500, message="Server not responding")

        except sqlite3.IntegrityError:
            abort(409, message="Resource already exists")
        except sqlite3.Error:
            abort(500, message="Server not responding")

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.EMPLOYEE_ROLE])
    @jwt_required()
    def get(self,user_id):
        result = emp_obj.view_details(user_id)
        if result:
            return result
        else:
            abort(404, message="Resource not found")

