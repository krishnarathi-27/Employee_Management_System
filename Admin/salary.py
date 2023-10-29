from config.constants_config import ConstantsConfig
from config.print_statements import PrintConfig
from config.queries_admin_config import QueriesAdmin
from db import database


class Salary:  

    def calculate_leaves(self):
        self.employee_id = int(input(PrintConfig.ENTER_EMP_ID))
        self.leaves = len(database.fetch_leaves(QueriesAdmin.QUERY_TO_CALCULATE_LEAVES,self.employee_id))
        self.paid_leaves= ConstantsConfig.PAID_LEAVES
        self.total_leaves = abs(self.leaves - self.paid_leaves)
        return self.total_leaves
        
    def calculate_salary(self):
        self.base_salary = ConstantsConfig.BASE_SALARY
        self.amount_to_deduct = self.base_salary/30
        self.salary_to_pay = self.base_salary - (self.calculate_leaves()*self.amount_to_deduct)
        return self.salary_to_pay

    def add_salary(self):
        self.salary_month = input(PrintConfig.ENTER_SALARY_MONTH)
        self.salary_status = input(PrintConfig.ENTER_SALARY_STATUS)
        database.add_data(QueriesAdmin.QUERY_TO_ADD_SALARY,(self.calculate_salary(),self.salary_month,self.salary_status,self.employee_id))

    def view_salary_status(self):
        database.display_data(QueriesAdmin.QUERY_TO_DISPLAY_SALARY_DETAILS,QueriesAdmin.LIST_TO_DISPLAY_SALARY_DETAILS)