from pydantic import BaseModel, Field
from config.app_config import AppConfig

class LoginSchema(BaseModel):
    username : str = Field(pattern=AppConfig.REGEX_NAME)
    password : str 


    