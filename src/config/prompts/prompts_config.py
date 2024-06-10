import yaml
FPATH = 'src\\config\\prompts\\prompt.yml'


class PromptsConfig:
    """
    Maintains all the config variables
    """
    ADMIN_PROMPT = None
    EMPLOYEE_PROMPT = None
    UPDATE_DETAILS_PROMPT = None
    LEAVE_STATUS_PROMPT = None

    WELCOME_MESSAGE = None
    ROW_NOT_EXISTS_MESSAGE = None
    WRONG_INPUT_ENTERED_MESSAGE = None
    ENTER_GENDER = None
    ENTER_PHONE_NO = None
    ENTER_MAIL = None
    ENTER_AGE = None
    ENTER_ROLE = None
    WELCOME_ADMIN_MESSAGE = None
    ENTER_EMP_ID = None
    ENTER_LEAVE_ID = None
    ENTER_LEAVE_STATUS = None
    ENTER_SALARY_STATUS = None
    ENTER_SALARY_MONTH = None
    ENTER_DATE = None
    WRONG_DATE_FORMAT = None
    INVALID_INPUT = None
    LEAVE_ERROR = None
    USER_ADDED_SUCCESS = None
    WELCOME_EMPLOYEE_MESSAGE = None

    # authentication file
    EXIT_SYSTEM_PROMPT = None
    INVALID_LOGIN = None
    INPUT_DEFAULT_PASSWORD = None
    INPUT_NEW_PASSWORD = None
    INPUT_CONFIRM_PASSWORD = None
    PASSWORD_NOT_MATCH = None
    DEFAULT_PASSWORD_UPDATED = None
    ENTER_USERNAME = None
    ENTER_PASSWORD = None
    ATTEMPTS_MESSAGE = None
    ATTEMPTS_EXHAUSTED = None
    STRONG_PASSWORD = None
    LOGIN_AGAIN = None
    WAIT_FOR_LOGIN = None
    NO_DATA_EXISTS = None

    # database_message
    DB_ERROR_MESSAGE = None
    DB_INTEGRITY_ERROR = None
    DB_GENERAL_ERROR = None
    INVALID_INPUT_ERROR = None
    GENERAL_EXCEPTION_MSG = None
    
    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.ADMIN_PROMPT = data['ADMIN_PROMPT']
            cls.EMPLOYEE_PROMPT = data['EMPLOYEE_PROMPT']
            cls.UPDATE_DETAILS_PROMPT = data['UPDATE_DETAILS_PROMPT']
            cls.LEAVE_STATUS_PROMPT = data['LEAVE_STATUS_PROMPT']

            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.WELCOME_EMPLOYEE_MESSAGE = data['WELCOME_EMPLOYEE_MESSAGE']
            cls.ROW_NOT_EXISTS_MESSAGE = data['ROW_NOT_EXISTS_MESSAGE']
            cls.WRONG_INPUT_ENTERED_MESSAGE = data['WRONG_INPUT_ENTERED_MESSAGE']
            cls.ENTER_GENDER = data['ENTER_GENDER']
            cls.ENTER_PHONE_NO = data['ENTER_PHONE_NO']
            cls.ENTER_MAIL = data['ENTER_MAIL']
            cls.ENTER_AGE = data['ENTER_AGE']
            cls.INVALID_INPUT = data['INVALID_INPUT']
            cls.ENTER_ROLE = data['ENTER_ROLE']
            cls.WELCOME_ADMIN_MESSAGE = data['WELCOME_ADMIN_MESSAGE']
            cls.ENTER_EMP_ID = data['ENTER_EMP_ID']
            cls.ENTER_LEAVE_ID = data['ENTER_LEAVE_ID']
            cls.ENTER_LEAVE_STATUS = data['ENTER_LEAVE_STATUS']
            cls.ENTER_SALARY_STATUS = data['ENTER_SALARY_STATUS']
            cls.ENTER_SALARY_MONTH = data['ENTER_SALARY_MONTH']
            cls.ENTER_DATE = data['ENTER_DATE']
            cls.WRONG_DATE_FORMAT = data['WRONG_DATE_FORMAT']
            cls.LEAVE_ERROR = data['LEAVE_ERROR']
            cls.USER_ADDED_SUCCESS = data['USER_ADDED_SUCCESS']
            cls.NO_DATA_EXISTS = data['NO_DATA_EXISTS']

            #authentication
            cls.EXIT_SYSTEM_PROMPT = data['EXIT_SYSTEM_PROMPT']
            cls.INVALID_LOGIN = data["INVALID_LOGIN"]
            cls.INPUT_DEFAULT_PASSWORD = data["INPUT_DEFAULT_PASSWORD"]
            cls.INPUT_NEW_PASSWORD = data["INPUT_NEW_PASSWORD"]
            cls.INPUT_CONFIRM_PASSWORD = data["INPUT_CONFIRM_PASSWORD"]
            cls.PASSWORD_NOT_MATCH = data["PASSWORD_NOT_MATCH"]
            cls.DEFAULT_PASSWORD_UPDATED = data["DEFAULT_PASSWORD_UPDATED"]
            cls.ENTER_USERNAME = data["ENTER_USERNAME"]
            cls.ENTER_PASSWORD = data["ENTER_PASSWORD"]
            cls.ATTEMPTS_MESSAGE = data["ATTEMPTS_MESSAGE"]
            cls.ATTEMPTS_EXHAUSTED = data["ATTEMPTS_EXHAUSTED"]
            cls.STRONG_PASSWORD = data["STRONG_PASSWORD"]
            cls.LOGIN_AGAIN = data["LOGIN_AGAIN"]
            cls.WAIT_FOR_LOGIN = data["WAIT_FOR_LOGIN"]

            # database_message
            cls.DB_ERROR_MESSAGE = data["DB_ERROR_MESSAGE"]
            cls.DB_INTEGRITY_ERROR = data["DB_INTEGRITY_ERROR"]
            cls.DB_GENERAL_ERROR = data["DB_GENERAL_ERROR"]
            cls.INVALID_INPUT_ERROR = data["INVALID_INPUT_ERROR"]
            cls.GENERAL_EXCEPTION_MSG = data["GENERAL_EXCEPTION_MSG"]
            