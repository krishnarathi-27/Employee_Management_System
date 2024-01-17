"""Module for validating user input by correct regex pattern"""
import re
import maskpass
import logging
from datetime import datetime
from config.app_config import AppConfig
from config.prompts.prompts_config import PromptsConfig

logger = logging.getLogger("validations")


class InputValidations:
    """Class containing methods to validate user input using regex pattern."""

    @staticmethod
    def input_name() -> str:
        """
        Method to validate user entered name using regex pattern
        Return type : str
        """
        while True:
            name = input(PromptsConfig.ENTER_USERNAME).strip().lower()
            if re.match(AppConfig.REGEX_NAME, name):
                return name
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid name entered")

    @staticmethod
    def input_email() -> str:
        """
        Method to validate user entered email using regex pattern
        Return type : str
        """
        while True:
            email = input(PromptsConfig.ENTER_MAIL).strip()
            if re.match(AppConfig.REGEX_EMAIL, email):
                return email
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid email entered")

    @staticmethod
    def input_password() -> str:
        """
        Method to validate user entered password using regex pattern
        Return type : str
        """
        while True:
            password = maskpass.askpass(PromptsConfig.ENTER_PASSWORD).strip()
            if re.match(AppConfig.REGEX_PASSWORD, password):
                return password
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid password entered")

    @staticmethod
    def input_age() -> str:
        """
        Method to validate user entered age using regex pattern
        Return type : str
        """
        while True:
            age = input(PromptsConfig.ENTER_AGE).strip()
            if re.match(AppConfig.REGEX_AGE, age):
                return age
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid age entered")

    @staticmethod
    def input_phone() -> str:
        """
        Method to validate user entered phone using regex pattern
        Return type : str
        """
        while True:
            mobile_no = input(PromptsConfig.ENTER_PHONE_NO).strip()
            if re.match(AppConfig.REGEX_MOBILE_NO, mobile_no):
                return mobile_no
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid mobile_no entered")

    @staticmethod
    def input_gender() -> str:
        """
            Validation of gender.
            Parameter -> None
            Return type -> str
        """
        while True:
            gender = input(PromptsConfig.ENTER_GENDER).strip().capitalize()
            if gender == "F":
                return "Female"
            elif gender == "M":
                return "Male"
            else:
                logger.debug("Invalid gender entered")
                print(PromptsConfig.INVALID_INPUT)

    @staticmethod
    def input_user_id() -> str:
        """
        Method to validate user entered user id using regex pattern
        Return type : str
        """
        while True:
            user_id = input(PromptsConfig.ENTER_EMP_ID).strip()
            if re.match(AppConfig.REGEX_USER_ID, user_id):
                return user_id
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid user id entered")
    
    @staticmethod
    def input_leave_id() -> str:

        while True:
            leave_id = input(PromptsConfig.ENTER_LEAVE_ID).strip()
            if re.match(AppConfig.REGEX_LEAVE_ID, leave_id):
                return leave_id
            print(PromptsConfig.INVALID_INPUT)
            logger.info("Invalid leave id entered")

    @staticmethod
    def input_date() -> str:
        """
        Method to validate user entered date using datetime.strptime()
        Return type : str
        """
        while True:
            purchased_date = input(PromptsConfig.ENTER_DATE).strip()
            try:
                datetime.strptime(purchased_date, AppConfig.DATE_FORMAT)
                return purchased_date
            except Exception:
                print(PromptsConfig.INVALID_INPUT)
                logger.info("Invalid date entered")