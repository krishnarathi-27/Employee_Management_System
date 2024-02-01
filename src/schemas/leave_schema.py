from pydantic import BaseModel, Field
from config.app_config import AppConfig

class LeaveSchema(BaseModel):
    leaves_id : str 
    leaves_date : str 
    leave_status : str
    employee_id : str

class CreateLeaveSchema(BaseModel):
    employee_id : str = Field(pattern=AppConfig.REGEX_USER_ID)
    leaves_date : str 

class UpdateLeaveSchema(BaseModel):
    leaves_status :str
