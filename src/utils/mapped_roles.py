import os
from dotenv import load_dotenv

load_dotenv()

class MappedRole:
    ADMIN_ROLE = os.getenv('ADMIN')
    EMPLOYEE_ROLE = os.getenv('EMPLOYEE')

    @classmethod
    def get_mapped_role(cls, role: str):
        if role == "admin":
            return cls.ADMIN_ROLE
        elif role == "employee":
            return cls.EMPLOYEE_ROLE
        