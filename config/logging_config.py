import yaml

FPATH_LOGGING_STATEMENTS = 'config_files\\logging_statements.yml'

class LoggingConfig:
        
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