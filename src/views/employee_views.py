"""Module for taking input from admin for various functionalities"""
import logging

# local imports
from config.queries import Headers
from config.app_config import AppConfig
from config.prompts.prompts_config import PromptsConfig
from config.logs.logging_config import LoggingConfig
from controllers.employee_controllers import EmployeeControllers
from utils.common_helper import CommonHelper
from utils.validations import InputValidations
from utils.app_decorator import error_handler
from views.leaves_views import LeavesViews
from views.salary_views import SalaryViews

logger = logging.getLogger("employee_views")

class EmployeeViews(LeavesViews,SalaryViews):
    """
    Class that contains menu options for taking input from employee to perform employee operations
    """
    def __init__(self,db_object,user_id) -> None:
        SalaryViews.__init__(self,db_object)
        LeavesViews.__init__(self,db_object)
        self.user_id = user_id
        self.obj_common_helper = CommonHelper(db_object)
        self.obj_employee_controller = EmployeeControllers(db_object)

        logger.info(LoggingConfig.LOG_ADMIN_LOGGED_IN)
        print(PromptsConfig.WELCOME_ADMIN_MESSAGE)

    def display_user_details(self) -> None:
        """ Method to display logged in users detail from table """

        data = self.obj_employee_controller.view_details(self.user_id)
        if not data:
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Headers.LIST_TO_DISPLAY_EMPLOYEE_DETAILS)

    @error_handler
    def update_menu(self) -> None:
        user_input = input(PromptsConfig.UPDATE_DETAILS_PROMPT)
        match user_input:
            case '1':
                email = InputValidations.input_email()
                self.obj_employee_controller.update_email(email,self.user_id)
            case '2':
                age = InputValidations.input_age()
                self.obj_employee_controller.update_age(age,self.user_id)
            case '3':
                phone = InputValidations.input_phone()
                self.obj_employee_controller.update_phone(phone,self.user_id)
            case '4':
                gender = InputValidations.input_gender()
                self.obj_employee_controller.update_gender(gender,self.user_id)
            case '5':
                return True
            case _:
                print(PromptsConfig.INVALID_INPUT)

        return False

    def update_menu_operations(self) -> None:
        """Method to perform admin tasks"""

        while True:
            if self.update_menu():
                break

    def employee_menu_operations(self) -> None:
        """Method to perform admin tasks"""

        while True:
            if self.employee_menu():
                break

    @error_handler
    def employee_menu(self):
        user_input = input(PromptsConfig.EMPLOYEE_PROMPT)
        match user_input:
            case '1':
                self.display_user_details()
            case '2':
                self.update_menu_operations()
            case '3':
                self.apply_leaves(self.user_id)  
            case '4':
                self.display_leaves_status(self.user_id)
            case '5':
                self.display_salary_status(self.user_id)
            case '6':
                return True
            case _:
                print(PromptsConfig.INVALID_INPUT)

        return False