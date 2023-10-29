import yaml
FPATH = 'config_files\\constants.yml'

class ConstantsConfig:
    """
    Maintains all the config variables
    """
    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.ATTEMPT = data['ATTEMPTS']
            cls.DATABASE_NAME = data['DATABASE_NAME']
            cls.BASE_SALARY = data['BASE_SALARY']
            cls.PAID_LEAVES = data['PAID_LEAVES']