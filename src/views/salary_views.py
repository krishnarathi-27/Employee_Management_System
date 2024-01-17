import logging
from enum import Enum
from config.queries import Headers
from config.prompts.prompts_config import PromptsConfig
from utils.common_helper import CommonHelper
from utils.validations import InputValidations
from config.logs.logging_config import LoggingConfig
from controllers.salary_controllers import SalaryControllers

class SalaryViews:
    
    def __init__(self,db_object) -> None:
        self.obj_common_helper = CommonHelper(db_object)
        self.obj_salary_controller = SalaryControllers(db_object)

    def display_salary(self) -> None:
        """ Method to display fetched salary from table """

        data = self.obj_salary_controller.view_salary()
        if not data:
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Headers.LIST_TO_DISPLAY_SALARY_DETAILS)

    def display_salary_status(self,user_id) -> None:
        data = self.obj_salary_controller.view_self_salary(user_id)
        if not data:
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Headers.LIST_TO_DISPLAY_SELFSALARY_DETAILS)  
            
    def add_salary(self) -> None:
        employee_id = InputValidations.input_user_id()

        if not self.obj_salary_controller.check_employee_id(employee_id):
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            salary_month = input(PromptsConfig.ENTER_SALARY_MONTH)
            if not self.obj_salary_controller.save_salary_status(employee_id,salary_month):
                print(PromptsConfig.NO_DATA_EXISTS)
            else:
                print("Salary added successfully")
                