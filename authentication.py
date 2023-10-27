import hashlib
from pwinput import pwinput
from utils.config_class import Config
from db import database 
from admin.admin import Admin
from emp.employee import Employee
import db.query_base as query

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
        self.default_password = pwinput(prompt='Enter your default password: ')
        login_success = database.fetch_user(query.QUERY_TO_VERIFY_LOGIN,self.username,self.default_password)
        if login_success == None:
            return False
        self.new_password = pwinput(prompt='Enter new password: ')
        self.confirm_password = pwinput(prompt='Enter new password to confirm: ')
        if self.new_password != self.confirm_password:
            return False
        self.hashed_password = hashlib.sha256(self.new_password.encode()).hexdigest()
        database.update_data(query.QUERY_TO_CHANGE_DEFAULT_PASWORD,(self.hashed_password,self.username))
            
    def login(self):
        print("Login into the system. You have total of 3 attempts")
        while Config.ATTEMPT:
            self.username = input("Enter your username:- ")
            record = database.fetch_data(query.QUERY_TO_CHECK_IF_DEFAULT_PASWORD,self.username)
            if record == 0:
                check = self.change_default_password()      
                if check == False:
                    Config.ATTEMPT-=1
                    continue
            self.password = pwinput(prompt='Enter your password: ')        
            login_success = database.fetch_user(query.QUERY_TO_VERIFY_LOGIN,self.username,self.password)
            if login_success == None:
                Config.ATTEMPT-=1
                print(f"Login failed!! Try again. Total attempts left {Config.ATTEMPT}/3")
            else:
                return login_success 
            