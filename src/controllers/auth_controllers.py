""" Module for validating user, changing their default passsword, and providing them role based access """
import hashlib
import logging

# local imports
from config.queries import Queries
from config.app_config import AppConfig
from config.logs.logging_config import LoggingConfig
from views.admin_views import AdminViews
from views.employee_views import EmployeeViews
from utils.common_helper import CommonHelper
from models.database import db

logger = logging.getLogger("auth_controller")


class AuthControllers:
    """
    Class containing methods for validating user, providing role based access and changing their default password.
    """

    # def __init__(self,db_object) -> None:
    #     self.db_object = db
    #     self.obj_common_helper = CommonHelper(self.db_object)

    def valid_first_login(
        self, username: str, hashed_input_password: str, password: str
    ) -> bool:
        """
        Method for changing default password on first valid login
        Parameters : self, username, hashed_input_password, password
        Return type : bool
        """
        if hashed_input_password == password:
            logger.info("User changing default password")
            self.obj_common_helper.change_default_password(username)
            return True
        else:
            logger.info("Wrong default password entered")
            return False

    def role_based_access(self, role: str, user_id: str) -> bool:
        """
        Method for providig role based accessto valid user.
        Parameters : self, role, user_id
        Return type : None
        """
        logger.info(LoggingConfig.PROVIDE_ROLE_BASED_ACCESS)

        if role == AppConfig.ADMININSTRATOR:
            # admin_obj = AdminViews(self.db_object)
            # admin_obj.admin_menu_operations()
            return True
        elif role == AppConfig.EMPLOYEE:
            # employee_obj = EmployeeViews(self.db_object,user_id)
            # employee_obj.employee_menu_operations()
            return True
        else:
            return False

    def validate_user(self, username: str, input_password: str) -> bool:
        """
        Method for validating user by their credentials
        Paramters : self, username, input_password
        Return type : bool
        """
        user_data = db.fetch_data(Queries.FETCH_USER_CREDENTIALS, (username,))
        if user_data:
            password = user_data[0][1]
            role = user_data[0][2]
            is_changed = user_data[0][3]
            user_id = user_data[0][0]
            hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
            if hashed_password == password:
                return (role, user_id)

        return ()