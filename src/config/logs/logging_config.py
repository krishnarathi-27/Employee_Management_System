import yaml

FPATH_LOGGING_STATEMENTS = 'src\\config\\logs\\logging_statements.yml'

class LoggingConfig:
    
    WELCOME_LOGGING_INFO = None
    WRONG_FILE_RUNNED = None
    REGISTERED_SUCCESSFULLY = None
    DELETED_SUCCESSFULLY = None
    UPDATED_SUCCESSFULLY = None
    LOGGED_IN = None
    ERROR_MESSAGE = None
       
    # authentication logs
    PROVIDE_ROLE_BASED_ACCESS = None
    LOG_INVALID_LOGIN = None
    LOG_DEFAULT_PASSWORD = None

    #admin
    LOG_CREATE_NEW_USER = None
    LOG_ADMIN_LOGGED_IN = None

    @classmethod
    def load(cls):
        with open(FPATH_LOGGING_STATEMENTS,'r') as f:
            data = yaml.safe_load(f)

            cls.WELCOME_LOGGING_INFO = data['WELCOME_LOGGING_INFO']
            cls.WRONG_FILE_RUNNED = data['WRONG_FILE_RUNNED']
            cls.REGISTERED_SUCCESSFULLY = data['REGISTERED_SUCCESSFULLY']
            cls.DELETED_SUCCESSFULLY = data['DELETED_SUCCESSFULLY']
            cls.UPDATED_SUCCESSFULLY = data['UPDATED_SUCCESSFULLY']
            cls.LOGGED_IN = data['LOGGED_IN']
            cls.ERROR_MESSAGE = data['ERROR_MESSAGE']

            # authentication logs
            cls.PROVIDE_ROLE_BASED_ACCESS = data["PROVIDE_ROLE_BASED_ACCESS"]
            cls.LOG_INVALID_LOGIN = data["LOG_INVALID_LOGIN"]
            cls.LOG_DEFAULT_PASSWORD = data["LOG_DEFAULT_PASSWORD"]

            #admin
            cls.LOG_CREATE_NEW_USER = data["LOG_CREATE_NEW_USER"]
            cls.LOG_ADMIN_LOGGED_IN = data["LOG_ADMIN_LOGGED_IN"]
