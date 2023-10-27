from db import database
from utils.config_class import Config
from db.queries.queries_config import QueriesConfig

class Salary:
    def __init__(self):
        self.employee_id = int(input(Config.ENTER_EMP_ID))

    def calculate_leaves(self):
        self.leaves = database.fetch_leaves(QueriesConfig.QUERY_TO_CALCULATE_LEAVES,self.employee_id)
        self.paid_leaves= Config.PAID_LEAVES
        self.total_leaves = abs(self.leaves - self.paid_leaves)
        return self.total_leaves
        
    def calculate_salary(self):
        self.base_salary = Config.BASE_SALARY
        self.amount_to_deduct = self.base_salary/30
        self.salary_to_pay = self.base_salary - (self.calculate_leaves()*self.amount_to_deduct)
        return self.salary_to_pay

    def add_salary(self):
        self.salary_month = input(Config.ENTER_SALARY_MONTH)
        self.salary_status = input(Config.ENTER_SALARY_STATUS)
        database.add_data(QueriesConfig.QUERY_TO_ADD_SALARY,(self.calculate_salary(),self.salary_month,self.salary_status,self.employee_id))