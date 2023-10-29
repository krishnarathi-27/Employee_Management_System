import hashlib
import logging
from pwinput import pwinput
from admin.admin import Admin
from config.constants_config import ConstantsConfig
from config.print_statements import PrintConfig
from config.queries_admin_config import QueriesAdmin
from db import database as db
from emp.employee import Employee

logger = logging.getLogger('authentication')

class Authentication:
    
    def __init__(self):  
        return_value = self.login()
        if return_value == None:
            exit()
        role, userid = return_value
        if role == 'admin':
            objAdmin= Admin()
            objAdmin.menu_admin()
        else:
            objEmployee = Employee(userid)
            objEmployee.menu_employee()  
  
    def change_default_password(self):        
        while True:
            self.new_password = pwinput(prompt=PrintConfig.ENTER_NEW_PASSWORD)
            self.confirm_password = pwinput(prompt=PrintConfig.CONFIRM_PASSWORD)
            if self.new_password != self.confirm_password:
                print("Passwords does not match")
                continue
            else:
                self.hashed_password = hashlib.sha256(self.new_password.encode()).hexdigest()
                db.update_data(QueriesAdmin.QUERY_TO_CHANGE_DEFAULT_PASWORD,(self.hashed_password,self.username))
                break
  
    def login(self):
        print(PrintConfig.PRINT_LOGIN)
        attempts = ConstantsConfig.ATTEMPT

        while attempts:
            self.username = input(PrintConfig.PRINT_USERNAME)
            self.password = pwinput(prompt=PrintConfig.PRINT_PASSWORD)
            self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
            user_data = db.fetch_data(QueriesAdmin.QUERY_TO_VERIFY_LOGIN,(self.username,))
            if not any(user_data):
                print(f"{PrintConfig.LOGIN_FAILED} {attempts}/3")
                attempts=attempts-1               
            elif user_data[0][2] == self.hashed_password:
                if user_data[0][4] == 0:
                    print("You need to change your default password")
                    self.change_default_password()
                    break
                else:
                    break

        if attempts <= 0:
            return None
        else:
            return user_data[0][3],user_data[0][0] 