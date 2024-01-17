"""Module contains common utility functions which are accessed across different modules"""
import logging
import hashlib
from tabulate import tabulate
from config.queries import Queries
from utils.validations import InputValidations
from config.prompts.prompts_config import PromptsConfig
from config.logs.logging_config import LoggingConfig

logger = logging.getLogger("common_helper")


class CommonHelper:
    """
    Class contains methods which are common and used across various files.
    """
    def __init__(self,db_object):
        self.db_object = db_object

    def change_default_password(self, username: str) -> None:
        """
        Method for changing default password of validated user
        Parameters : self, username
        Return type : None
        """

        while True:
            logger.info("Validated user changing default password")
            print(PromptsConfig.STRONG_PASSWORD)
            new_password = InputValidations.input_password()
            print(PromptsConfig.INPUT_CONFIRM_PASSWORD)
            confirm_password = InputValidations.input_password()

            if new_password != confirm_password:
                print(PromptsConfig.PASSWORD_NOT_MATCH)
                logger.info("New password not matches confirm new password")

            else:
                new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                self.db_object.save_data(
                    Queries.QUERY_TO_CHANGE_DEFAULT_PASWORD,
                    (
                        new_hashed_password,
                        username,
                    ),
                )
                print(PromptsConfig.DEFAULT_PASSWORD_UPDATED)
                logger.info(LoggingConfig.LOG_DEFAULT_PASSWORD)
                return

    @staticmethod
    def display_table(data: list, headers: list) -> None:
        """
        Method to display data in tabular format using tabulate
        Parameters : data, headers
        Return type : None
        """
        row_id = [i for i in range(1, len(data) + 1)]
        print(tabulate(data, headers, showindex=row_id, tablefmt="simple_grid"))
