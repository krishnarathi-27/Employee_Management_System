import yaml
FPATH_PRINT_STATEMENTS = 'config_files\\print_statements.yml'


class PrintConfig:
    """
    Maintains all the config variables
    """
    @classmethod
    def load(cls):
        with open(FPATH_PRINT_STATEMENTS,'r') as f:
            data = yaml.safe_load(f)           
            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.ROW_NOT_EXISTS_MESSAGE = data['ROW_NOT_EXISTS_MESSAGE']
            cls.WRONG_INPUT_ENTERED_MESSAGE = data['WRONG_INPUT_ENTERED_MESSAGE']
            cls.PRINT_USERNAME = data['PRINT_USERNAME']
            cls.PRINT_PASSWORD = data['PRINT_PASSWORD']
            cls.ENTER_STRONG_PASSWORD = data['ENTER_STRONG_PASSWORD']
            cls.ENTER_GENDER = data['ENTER_GENDER']
            cls.ENTER_PHONE_NO = data['ENTER_PHONE_NO']
            cls.ENTER_MAIL = data['ENTER_MAIL']
            cls.ENTER_AGE = data['ENTER_AGE']
            cls.ENTER_ROLE = data['ENTER_ROLE']
            cls.WELCOME_ADMIN_MESSAGE = data['WELCOME_ADMIN_MESSAGE']
            cls.ENTER_EMP_ID = data['ENTER_EMP_ID']
            cls.ENTER_LEAVE_ID = data['ENTER_LEAVE_ID']
            cls.ENTER_LEAVE_STATUS = data['ENTER_LEAVE_STATUS']
            cls.ENTER_SALARY_STATUS = data['ENTER_SALARY_STATUS']
            cls.ENTER_SALARY_MONTH = data['ENTER_SALARY_MONTH']
            cls.ENTER_DEFAULT_PASSWORD = data['ENTER_DEFAULT_PASSWORD']
            cls.ENTER_NEW_PASSWORD = data['ENTER_NEW_PASSWORD']
            cls.CONFIRM_PASSWORD = data['CONFIRM_PASSWORD'] 
            cls.PRINT_LOGIN = data['PRINT_LOGIN']
            cls.LOGIN_FAILED = data['LOGIN_FAILED']
            cls.ENTER_DATE = data['ENTER_DATE']
            cls.WRONG_DATE_FORMAT = data['WRONG_DATE_FORMAT']
            cls.LEAVE_ERROR = data['LEAVE_ERROR']