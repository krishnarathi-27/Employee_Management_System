"""Module having buisness logic of admin functionalities"""
import logging
import hashlib

# local imports
from config.queries import Queries
from config.logs.logging_config import LoggingConfig

logger = logging.getLogger("admin_controller")


class AdminControllers:
    """
    Class containing methods to create new user
    """
    def __init__(self,db_object):
        self.db_object = db_object

    def view_user(self):
        data = self.db_object.fetch_data(Queries.QUERY_TO_DISPLAY_EMPLOYEE_DETAILS)
        return data 
    
    def create_new_user(self, employee_id: str,user_role: str, username: str, password: str) -> None:
        """
        Method for creating new user in the system with unique username
        Parameters : self, user_role, username, password
        Return Type : None
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.db_object.save_data(
            Queries.INSERT_USER_CREDENTIALS,
            (
                employee_id,
                username,
                hashed_password,
                user_role,
            )
        )

        logger.info(LoggingConfig.LOG_CREATE_NEW_USER)

    def create_employee_details(self,employee_id,employee_age,employee_mail,employee_gender,employee_phone) -> None:
        self.db_object.save_data( 
                Queries.QUERY_TO_ADD_IN_EMP_DETAILS_TABLE,
                (     
                    employee_id,employee_age,
                    employee_mail,employee_gender,
                    employee_phone,
                )
            )
        
    def check_employee_id(self, employee_id: str):
        data = self.db_object.fetch_data(
                    Queries.QUERY_TO_FETCH_EMPLOYEE_EXISTS,
                    (employee_id,)
                )
        
        if not data:
            return False
        else:
            return True
        
    def delete_exisiting_user(self, employee_id: str):
        self.db_object.save_data(
                Queries.QUERY_TO_DELETE_FROM_AUTH_TABLE,
                (employee_id,)
            )
        