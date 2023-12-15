"""Module for taking input from admin for various functionalities"""
import logging
import shortuuid

# local imports
from config.queries import Headers
from config.app_config import AppConfig
from config.prompts.prompts_config import PromptsConfig
from config.logs.logging_config import LoggingConfig
from controllers.admin_controllers import AdminControllers
from utils.common_helper import CommonHelper
from utils.validations import InputValidations
from utils.app_decorator import error_handler
from views.leaves_views import LeavesViews
from views.salary_views import SalaryViews

logger = logging.getLogger("admin_views")

class AdminViews(LeavesViews,SalaryViews):
    """
    Class that contains menu options for taking input from admin to perform admin operations
    """
    def __init__(self,db_object) -> None:
        SalaryViews.__init__(self,db_object)
        LeavesViews.__init__(self,db_object)
        self.obj_common_helper = CommonHelper(db_object)
        self.obj_admin_controller = AdminControllers(db_object)

        logger.info(LoggingConfig.LOG_ADMIN_LOGGED_IN)
        print(PromptsConfig.WELCOME_ADMIN_MESSAGE)
    
    def create_user(self) -> None:
        """Method to create new user in the system"""

        employee_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        username = InputValidations.input_name()
        password = InputValidations.input_password()
        employee_mail = InputValidations.input_email()
        employee_age = InputValidations.input_age()
        employee_phone = InputValidations.input_phone()
        employee_gender = InputValidations.input_gender()
        user_role = AppConfig.EMPLOYEE

        self.obj_admin_controller.create_new_user(employee_id,user_role, username, password)
        self.obj_admin_controller.create_employee_details(employee_id,employee_age,employee_mail,employee_gender,employee_phone)

        logger.info("New user added to the system")
        print(PromptsConfig.USER_ADDED_SUCCESS)

    def display_user(self) -> None:
        """ Method to display fetched user from table """

        data = self.obj_admin_controller.view_user()
        if not data:
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Headers.LIST_TO_DISPLAY_EMPLOYEE_DETAILS)

    def delete_user(self) -> None:
        """Method to take input to delete existing user"""

        self.display_user()
        employee_id = InputValidations.input_user_id()
        if not self.obj_admin_controller.check_employee_id(employee_id):
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            self.obj_admin_controller.delete_exisiting_user(employee_id)
            print("Employee deleted successfully")

    def admin_menu_operations(self) -> None:
        """Method to perform admin tasks"""

        while True:
            if self.admin_menu():
                break

    @error_handler
    def admin_menu(self):            
        user_input = input(PromptsConfig.ADMIN_PROMPT)
        match user_input:
            case '1':
                self.create_user()
            case '2':
                self.delete_user()
            case '3':
                self.display_user()   
            case '4':
                self.display_leaves()
            case '5':
                self.update_leaves_status()
                pass
            case '6':
                self.display_user()
                self.add_salary()
                pass
            case '7':
                self.display_salary()
            case '8':
                return True
            case _:
                print(PromptsConfig.INVALID_INPUT)

        return False
                