from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig

class LoginSchema(Schema):
    username = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    password = fields.Str(required=True)

class UserDetailSchema(Schema):
    user_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=True)
    age = fields.Int(required=True)
    mail = fields.Str(required=True)
    gender = fields.Str(required=True)
    phone = fields.Int(required=True)
    