from db import database
from db import query_base as q

class Salary:
    def __init__(self):
        self.employee_id = int(input("Enter employee id to calculate total salary:- "))

    def calculate_leaves(self):
        self.leaves = database.fetch_leaves(q.QUERY_TO_CALCULATE_LEAVES,self.employee_id)
        self.paid_leaves= database.fetch_data(q.QUERY_TO_FETCH_CONFIG_DATA,'paid_leaves')
        self.total_leaves = abs(self.leaves - self.paid_leaves)
        return self.total_leaves
        
    def calculate_salary(self):
        self.base_salary = database.fetch_data(q.QUERY_TO_FETCH_CONFIG_DATA,'base_salary')
        self.amount_to_deduct = self.base_salary/30
        self.salary_to_pay = self.base_salary - (self.calculate_leaves()*self.amount_to_deduct)
        return self.salary_to_pay

    def add_salary(self):
        self.salary_month = input("Enter month of salary:- ")
        self.salary_status = input("Enter status of salary:- ")
        database.add_data(q.QUERY_TO_ADD_SALARY,(self.calculate_salary(),self.salary_month,self.salary_status,self.employee_id))