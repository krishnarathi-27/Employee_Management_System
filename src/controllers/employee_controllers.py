"""Module having buisness logic of employee functionalities"""
import logging
import hashlib

# local imports
from models.database import Database
from config.queries import Queries
from config.logs.logging_config import LoggingConfig

logger = logging.getLogger("employee_controller")


class EmployeeControllers:
    """
    Class containing methods to create new user
    """

    def view_details(self, employee_id: str):
        data = Database.fetch_data(
                    Queries.QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS,
                    (employee_id,)
                    )
        return data 
    
    def update_email(self,email: str, employee_id: str) -> None:
        Database.save_data(
                Queries.QUERY_TO_UPDATE_EMP_MAIL,
                (email,employee_id,)
        )
         
    def update_age(self,age: str, employee_id: str) -> None:
        Database.save_data(
                Queries.QUERY_TO_UPDATE_EMP_AGE,
                (age,employee_id,)
        )
         
    def update_phone(self,phone: str, employee_id: str) -> None:
        Database.save_data(
                Queries.QUERY_TO_UPDATE_EMP_PHONE,
                (phone,employee_id,)
        )
         
    def update_gender(self,gender: str, employee_id: str) -> None:
        Database.save_data(
                Queries.QUERY_TO_UPDATE_EMP_GENDER,
                (gender,employee_id,)
        )
