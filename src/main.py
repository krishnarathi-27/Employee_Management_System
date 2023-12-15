import logging
from config.app_config import AppConfig
from config.logs.logging_config import LoggingConfig
from config.prompts.prompts_config import PromptsConfig
from models.database import db
from views.auth_views import AuthViews

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = AppConfig.LOG_FILE_LOCATION)

logger = logging.getLogger('main')

if __name__ == '__main__':   
    
    #to load all the configuration files
    LoggingConfig.load()
    PromptsConfig.load()

    logger.info(LoggingConfig.WELCOME_LOGGING_INFO)
    print(PromptsConfig.WELCOME_MESSAGE)   
    
    # creates all tables if not exists
    db.create_all_table()

    # logins the user
    auth_obj = AuthViews(db)
    auth_obj.login()

    # closes database connection
    db.connection.close()  

else:
    logger.debug(LoggingConfig.WRONG_FILE_RUNNED)