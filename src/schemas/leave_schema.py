from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig

class LeaveSchema(Schema):
    employee_id = fields.Str(required=True)
    leaves_date = fields.Date(required=True)

class LeaveUpdateSchema(Schema):
    leaves_status = fields.Str(required=True)

