""" Module for validating user, changing their default passsword, and providing them role based access """
import hashlib
import logging

# local imports
from config.queries import Queries
from config.app_config import AppConfig
from config.logs.logging_config import LoggingConfig
from models.database import Database

logger = logging.getLogger("auth_controller")


class AuthControllers:
    """
    Class containing methods for validating user, providing role based access and changing their default password.
    """

    def validate_user(self, username: str, input_password: str) -> bool:
        """
        Method for validating user by their credentials
        Paramters : self, username, input_password
        Return type : bool
        """
        user_data = Database.fetch_data(Queries.FETCH_USER_CREDENTIALS, (username,))
        print(user_data)
        if user_data:
            password = user_data[0][1]
            role = user_data[0][2]
            is_changed = user_data[0][3]
            user_id = user_data[0][0]
            hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
            if hashed_password == password:
                return (role, user_id)

        return ()
    