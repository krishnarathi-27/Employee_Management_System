from pydantic import BaseModel, Field
from config.app_config import AppConfig

class LeaveSchema(BaseModel):
    leaves_id : str = Field(pattern=AppConfig.REGEX_LEAVE_ID)
    leaves_date : str 
    leave_status : str
    employee_id : str

