import hashlib
import logging
from pwinput import pwinput
from db import database
from utils.config_class import Config
from db.queries.queries_config import QueriesConfig
from utils.input_validation import password_validation
from .salary import Salary

logger = logging.getLogger('admin')

class Admin:
    def __init__(self):   
        print(Config.WELCOME_ADMIN_MESSAGE)
            
    def menu_admin(self):
        user_input = input(Config.ADMIN_PROMPT)
        while user_input != 'q':           
            match user_input:
                case '1':
                    Admin.register()
                case '2':
                    Admin.delete()
                case '3':
                    database.display_data(QueriesConfig.QUERY_TO_DISPLAY_EMPLOYEE_DETAILS,QueriesConfig.LIST_TO_DISPLAY_EMPLOYEE_DETAILS)   
                case '4':
                    database.display_data(QueriesConfig.QUERY_TO_DISPLAY_LEAVES_DETAILS,QueriesConfig.LIST_TO_DISPLAY_LEAVES_DETAILS)
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
        username = input(Config.PRINT_USERNAME)
        while True:
            password = pwinput(prompt=Config.PRINT_PASSWORD)
            if not password_validation(password):
                print(Config.ENTER_STRONG_PASSWORD)
            else:
                break
        hashed_password = hashlib.sha256(password.encode()).hexdigest()     
        role = input(Config.ENTER_ROLE)
        emp_mail = input(Config.ENTER_MAIL)
        emp_age = int(input(Config.ENTER_AGE))
        emp_phone = int(input(Config.ENTER_PHONE_NO))
        emp_gender = input(Config.ENTER_GENDER)
        database.add_data(QueriesConfig.QUERY_TO_ADD_IN_AUTH_TABLE,(username,hashed_password,role))
        database.add_data(QueriesConfig.QUERY_TO_ADD_IN_EMP_DETAILS_TABLE,(emp_mail,emp_age,emp_phone,emp_gender))
        logging.info(Config.REGISTERED_SUCCESSFULLY)

    @staticmethod
    def delete() -> None:
        employee_id = input(Config.ENTER_EMP_ID)
        database.delete_data(QueriesConfig.QUERY_TO_DELETE_FROM_AUTH_TABLE,employee_id)
        logging.warning(Config.DELETED_SUCCESSFULLY)
    
    @staticmethod
    def update_leave_status() -> None:
        database.display_data(QueriesConfig.QUERY_TO_DISPLAY_LEAVES_DETAILS,QueriesConfig.LIST_TO_DISPLAY_LEAVES_DETAILS)
        leave_id = input(Config.ENTER_LEAVE_ID)
        status = input(Config.ENTER_LEAVE_STATUS)
        database.update_data(QueriesConfig.QUERY_TO_UPDATE_LEAVES_STATUS,(status,leave_id,))
        logging.debug(Config.UPDATED_SUCCESSFULLY)

        