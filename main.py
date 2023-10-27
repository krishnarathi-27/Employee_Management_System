from authentication import Authentication
from utils.config_class import Config

class EmployeeManagementClass:
    def __init__(self):
        print(Config.WELCOME_MESSAGE)   
        Authentication()       

if __name__ == '__main__':
    Config.load()  
    obj = EmployeeManagementClass()