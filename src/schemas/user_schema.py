from pydantic import BaseModel, Field
from config.app_config import AppConfig

class LoginSchema(BaseModel):
    username : str = Field(pattern=AppConfig.REGEX_NAME)
    password : str 

# class UserDetailSchema(Schema):
#     user_id = fields.Str(dump_only=True)
#     username = fields.Str(required=True)
#     password = fields.Str(required=True)
#     role = fields.Str(required=True)
#     age = fields.Int(required=True)
#     mail = fields.Str(required=True)
#     gender = fields.Str(required=True)
#     phone = fields.Int(required=True)
    