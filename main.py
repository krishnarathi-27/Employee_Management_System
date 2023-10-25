from pwinput import pwinput
from DAO import database 
from Admin.admin import Admin
from Employee.employee import Employee
import DAO.query_base as query


class Mainclass:
    def __init__(self):
        print("------------Welcome to employee management system--------------")   
        database.create_table(query.QUERY_FOR_CREATE_AUTH_TABLE)
        database.create_table(query.QUERY_FOR_CREATE_EMP_DETAILS_TABLE)
        database.create_table(query.QUERY_FOR_CREATE_LEAVES_TABLE)
        database.create_table(query.QUERY_FOR_CREATE_SALARY_TABLE)

    def login(self):
        print("Login into the system. You have total of 3 attempts")
        attempts = 3
        while attempts:
            self.username = input("Enter your username:- ")
            self.password = pwinput(prompt='Enter your password: ')        
            login_success = database.login_user(query.QUERY_TO_VERIFY_LOGIN,self.username,self.password)
            if login_success == None:
                attempts-=1
                print(f"Login failed!! Try again. Total attempts left {attempts}/3")
            else:
                return login_success    

if __name__ == '__main__':  
    obj = Mainclass()

    return_value = obj.login()
    if return_value == None:
        exit()
    role, userid = return_value
    if role == 'admin':
        objAdmin= Admin()
        objAdmin.menu_admin()
    else:
        objEmployee = Employee(userid)
        objEmployee.menu_employee()        