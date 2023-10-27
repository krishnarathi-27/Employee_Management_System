import hashlib
import db.query_base as q
from pwinput import pwinput
from db import database
from utils.config_class import Config
from utils.input_validation import password_validation
from .salary import Salary


class Admin:
    def __init__(self):   
        print("Welcome as Admin")
            
    def menu_admin(self):
        user_input = input(Config.ADMIN_PROMPT)
        while user_input != 'q':           
            match user_input:
                case '1':
                    Admin.register()
                case '2':
                    Admin.delete()
                case '3':
                    database.display_data(q.QUERY_TO_DISPLAY_EMPLOYEE_DETAILS,q.LIST_TO_DISPLAY_EMPLOYEE_DETAILS)   
                case '4':
                    database.display_data(q.QUERY_TO_DISPLAY_LEAVES_DETAILS,q.LIST_TO_DISPLAY_LEAVES_DETAILS)
                case '5':
                    Admin.update_leave_status()
                case '6':
                    salaryObj = Salary()
                    salaryObj.add_salary()
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            
            user_input = input(Config.ADMIN_PROMPT)

    @staticmethod
    def register() -> None:
        print("Register user in the system")
        username = input("Enter username:- ")
        while True:
            password = pwinput(prompt='Enter password: ')
            if not password_validation(password):
                print("Enter strong password")
            else:
                break
        hashed_password = hashlib.sha256(password.encode()).hexdigest()     
        role = input("Enter the role of the user:- ")
        emp_mail = input("Enter employee mail id:- ")
        emp_age = int(input("Enter age of employee:- "))
        emp_phone = int(input("Enter employee phone number:- "))
        emp_gender = input("Enter gender of employee:- ")
        database.add_data(q.QUERY_TO_ADD_IN_AUTH_TABLE,(username,hashed_password,role))
        database.add_data(q.QUERY_TO_ADD_IN_EMP_DETAILS_TABLE,(emp_mail,emp_age,emp_phone,emp_gender))

    @staticmethod
    def delete() -> None:
        employee_id = input("Enter the employee id to delete:- ")
        database.delete_data(q.QUERY_TO_DELETE_FROM_AUTH_TABLE,employee_id)
        print("Employee delete successfully!!")
    
    @staticmethod
    def update_leave_status() -> None:
        database.display_data(q.QUERY_TO_DISPLAY_LEAVES_DETAILS,q.LIST_TO_DISPLAY_LEAVES_DETAILS)
        leave_id = input("Enter leave id to update leave status:- ")
        status = input("Update status to:- cancel/approved/rejected:- ")
        database.update_data(q.QUERY_TO_UPDATE_LEAVES_STATUS,(status,leave_id,))

        