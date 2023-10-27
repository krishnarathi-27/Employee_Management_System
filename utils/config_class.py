import yaml
FPATH = 'prompt.yml'

class Config:
    """
    Maintains all the config variables
    """
    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.ADMIN_PROMPT = data['ADMIN_PROMPT']
            cls.EMPLOYEE_PROMPT = data['EMPLOYEE_PROMPT']
            cls.UPDATE_DETAILS_PROMPT = data['UPDATE_DETAILS_PROMPT']
            cls.ATTEMPT = data['ATTEMPTS']
            cls.DATABASE_NAME = data['DATABASE_NAME']
            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.ROW_NOT_EXISTS_MESSAGE = data['ROW_NOT_EXISTS_MESSAGE']
            cls.WRONG_INPUT_ENTERED_MESSAGE = data['WRONG_INPUT_ENTERED_MESSAGE']
            
            