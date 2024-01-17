from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig

class SalarySchema(Schema):
    employee_id = fields.Str(required=True)
    salary_month = fields.Str(required=True)