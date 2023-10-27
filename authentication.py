import hashlib
import logging
from pwinput import pwinput
from utils.config_class import Config
from db import database 
from db.queries.queries_config import QueriesConfig
from admin.admin import Admin
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
        self.default_password = pwinput(prompt=Config.ENTER_DEFAULT_PASSWORD)
        login_success = database.fetch_user(QueriesConfig.QUERY_TO_VERIFY_LOGIN,self.username,self.default_password)
        if login_success == None:
            return False
        self.new_password = pwinput(prompt=Config.ENTER_NEW_PASSWORD)
        self.confirm_password = pwinput(prompt=Config.CONFIRM_PASSWORD)
        if self.new_password != self.confirm_password:
            return False
        self.hashed_password = hashlib.sha256(self.new_password.encode()).hexdigest()
        database.update_data(QueriesConfig.QUERY_TO_CHANGE_DEFAULT_PASWORD,(self.hashed_password,self.username))
            
    def login(self):
        print(Config.PRINT_LOGIN)
        while Config.ATTEMPT:
            self.username = input(Config.PRINT_USERNAME)
            record = database.fetch_data(QueriesConfig.QUERY_TO_CHECK_IF_DEFAULT_PASWORD,self.username)
            if record == 0:
                check = self.change_default_password()      
                if check == False:
                    Config.ATTEMPT-=1
                    continue
            self.password = pwinput(prompt=Config.PRINT_PASSWORD)        
            login_success = database.fetch_user(QueriesConfig.QUERY_TO_VERIFY_LOGIN,self.username,self.password)
            if login_success == None:
                Config.ATTEMPT-=1
                print(f"{Config.LOGIN_FAILED} {Config.ATTEMPT}/3")
            else:
                return login_success 
            