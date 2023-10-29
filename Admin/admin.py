import hashlib
import logging
from pwinput import pwinput
from config.logging_config import LoggingConfig
from config.prompts_config import PromptsConfig
from config.print_statements import PrintConfig
from config.queries_admin_config import QueriesAdmin
from db import database
from utils.input_validation import password_validation
from .salary import Salary

logger = logging.getLogger('admin')

class Admin:
    def __init__(self):   
        print(PrintConfig.WELCOME_ADMIN_MESSAGE)
            
    def menu_admin(self):
        user_input = input(PromptsConfig.ADMIN_PROMPT)
        salaryObj = Salary()
        while user_input != 'q':           
            match user_input:
                case '1':
                    Admin.register()
                case '2':
                    Admin.delete()
                case '3':
                    database.display_data(QueriesAdmin.QUERY_TO_DISPLAY_EMPLOYEE_DETAILS,QueriesAdmin.LIST_TO_DISPLAY_EMPLOYEE_DETAILS)   
                case '4':
                    database.display_data(QueriesAdmin.QUERY_TO_DISPLAY_LEAVES_DETAILS,QueriesAdmin.LIST_TO_DISPLAY_LEAVES_DETAILS)
                case '5':
                    Admin.update_leave_status()
                case '6':
                    salaryObj.add_salary()
                case '7':
                    salaryObj.view_salary_status()
                case _:
                    print(PrintConfig.WRONG_INPUT_ENTERED_MESSAGE)
            
            user_input = input(PromptsConfig.ADMIN_PROMPT)

    @staticmethod
    def register() -> None:
        username = input(PrintConfig.PRINT_USERNAME)
        while True:
            password = pwinput(prompt=PrintConfig.PRINT_PASSWORD)
            if not password_validation(password):
                print(PrintConfig.ENTER_STRONG_PASSWORD)
            else:
                break
        hashed_password = hashlib.sha256(password.encode()).hexdigest()     
        role = input(PrintConfig.ENTER_ROLE)
        emp_mail = input(PrintConfig.ENTER_MAIL)
        emp_age = int(input(PrintConfig.ENTER_AGE))
        emp_phone = int(input(PrintConfig.ENTER_PHONE_NO))
        emp_gender = input(PrintConfig.ENTER_GENDER)
        database.add_data(QueriesAdmin.QUERY_TO_ADD_IN_AUTH_TABLE,(username,hashed_password,role))
        database.add_data(QueriesAdmin.QUERY_TO_ADD_IN_EMP_DETAILS_TABLE,(emp_mail,emp_age,emp_phone,emp_gender))
        logging.info(LoggingConfig.REGISTERED_SUCCESSFULLY)

    @staticmethod
    def delete() -> None:
        employee_id = input(PrintConfig.ENTER_EMP_ID)
        database.delete_data(QueriesAdmin.QUERY_TO_DELETE_FROM_AUTH_TABLE,employee_id)
        logging.warning(LoggingConfig.DELETED_SUCCESSFULLY)
    
    @staticmethod
    def update_leave_status() -> None:
        database.display_data(QueriesAdmin.QUERY_TO_DISPLAY_LEAVES_DETAILS,QueriesAdmin.LIST_TO_DISPLAY_LEAVES_DETAILS)
        leave_id = input(PrintConfig.ENTER_LEAVE_ID)
        status = input(PrintConfig.ENTER_LEAVE_STATUS)
        database.update_data(QueriesAdmin.QUERY_TO_UPDATE_LEAVES_STATUS,(status,leave_id,))
        logging.debug(LoggingConfig.UPDATED_SUCCESSFULLY)

        