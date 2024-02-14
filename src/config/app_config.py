"""This module contains all the app constants"""
import os

class AppConfig:
    """Class is used to load all the appconfig constants"""

    MAX_LOGIN_ATTEMPTS = 3
    PAID_LEAVES = 1
    BASE_SALARY = 30000
    DATABASE_LOCATION = os.path.abspath(os.curdir) + "/models/employee_management.db"
    TEST_DB_PATH = "tests/test_db.db"
    LOG_FILE_LOCATION = 'logs.txt'

    # roles of user
    ADMININSTRATOR = "admin"
    EMPLOYEE = "employee"

    #regex patterns    
    DATE_FORMAT = r"%Y-%m-%d"
    REGEX_USER_ID = r"^EMP[a-zA-Z0-9]{4}$"
    REGEX_LEAVE_ID = r"^LID[a-zA-Z0-9]{4}$"
    REGEX_NAME = r"^([A-Za-z0-9]{3,20}.\s*)"
    REGEX_EMAIL = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
    REGEX_PASSWORD = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"
    REGEX_AGE = r"(^[1][4-9]$)|(^[2-5][0-9]$)|60"
    REGEX_MOBILE_NO = r"[6-9][0-9]{9}$"
