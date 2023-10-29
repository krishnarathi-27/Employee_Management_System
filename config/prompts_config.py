import yaml
FPATH = 'config_files\\prompt.yml'


class PromptsConfig:
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
            