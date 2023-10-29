import logging
from config.logging_config import LoggingConfig
from config.print_statements import PrintConfig
from config.prompts_config import PromptsConfig
from config.queries_emp_config import QueriesEmp
from db import database as db
from .apply_leaves import ApplyLeaves

logger = logging.getLogger('employee')

class Employee:

    def __init__(self,userid):
        self.userid = userid
        logging.info(LoggingConfig.LOGGED_IN)

    def menu_employee(self):
        print(self.userid)
        user_input = input(PromptsConfig.EMPLOYEE_PROMPT)
        while user_input != 'q':
            match user_input:
                case '1':
                    db.display_data(QueriesEmp.QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS,QueriesEmp.LIST_TO_DISPLAY_SELFEMPLOYEE_DETAILS,self.userid)
                case '2':
                    self.update_details()
                case '3':
                    objLeave = ApplyLeaves(self.userid)
                    objLeave.fetch_leaves_date()
                case '4':
                    db.display_data(QueriesEmp.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS,QueriesEmp.LIST_TO_DISPLAY_SELFLEAVES_DETAILS,self.userid)
                case '5':
                    db.display_data(QueriesEmp.QUERY_TO_DISPLAY_SALARY_STATUS,QueriesEmp.LIST_TO_DISPLAY_SELFSALARY_DETAILS,self.userid)
                case _:
                    print(PrintConfig.WRONG_INPUT_ENTERED_MESSAGE)
            user_input = input(PromptsConfig.EMPLOYEE_PROMPT)
      

    def update_details(self):
        self.update_input = input(PromptsConfig.UPDATE_DETAILS_PROMPT)
        match self.update_input:
            case '1':
                email_to_update = input("Enter the new mail:- ")
                db.update_data(QueriesEmp.QUERY_TO_UPDATE_EMP_MAIL,(email_to_update,self.userid,))
                logging.debug(LoggingConfig.UPDATED_SUCCESSFULLY)
            case '2':
                age_to_update = input("Enter the new age:- ")
                db.update_data(QueriesEmp.QUERY_TO_UPDATE_EMP_AGE,(age_to_update,self.userid,))
                logging.debug(LoggingConfig.UPDATED_SUCCESSFULLY)
            case '3':
                phone_to_update = input("Enter the new phone number:- ")
                db.update_data(QueriesEmp.QUERY_TO_UPDATE_EMP_PHONE,(phone_to_update,self.userid,))
                logging.debug(LoggingConfig.UPDATED_SUCCESSFULLY)
            case '4':
                gender_to_update = input("Enter the new gender:- ")
                db.update_data(QueriesEmp.QUERY_TO_UPDATE_EMP_GENDER,(gender_to_update,self.userid,))
                logging.debug(LoggingConfig.UPDATED_SUCCESSFULLY)
            case _:
                print(PrintConfig.WRONG_INPUT_ENTERED_MESSAGE)

    