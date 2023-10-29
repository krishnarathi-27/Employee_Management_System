import logging
from authentication import Authentication
from config.constants_config import ConstantsConfig
from config.logging_config import LoggingConfig
from config.print_statements import PrintConfig
from config.prompts_config import PromptsConfig
from config.queries_admin_config import QueriesAdmin
from config.queries_emp_config import QueriesEmp

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'config_files\\logs.txt')

logger = logging.getLogger('main')

def load_config_files():
    #to load all the configuration files
    ConstantsConfig.load()
    LoggingConfig.load()
    PrintConfig.load()
    PromptsConfig.load()
    QueriesAdmin.load()
    QueriesEmp.load()

if __name__ == '__main__':   
    load_config_files()
    logger.info(LoggingConfig.WELCOME_LOGGING_INFO)
    print(PrintConfig.WELCOME_MESSAGE)   
    Authentication()  

else:
    logger.debug(LoggingConfig.WRONG_FILE_RUNNED)