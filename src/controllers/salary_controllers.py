import logging
import shortuuid

# local imports
from config.app_config import AppConfig
from config.queries import Queries
from config.logs.logging_config import LoggingConfig

class SalaryControllers:

    def __init__(self,db_object):
        self.db_object = db_object
        
    def view_salary(self):
        data = self.db_object.fetch_data(Queries.QUERY_TO_DISPLAY_SALARY_DETAILS)
        return data
    
    def view_self_salary(self,user_id):
        data = self.db_object.fetch_data(Queries.QUERY_TO_DISPLAY_SELF_SALARY_STATUS,(user_id,))
        return data
    
    def check_employee_id(self, employee_id: str):
        data = self.db_object.fetch_data(
                    Queries.QUERY_TO_FETCH_EMPLOYEE_EXISTS,
                    (employee_id,)
                )
        if not data:
            return False
        else:
            return True
        
    def save_salary_status(self,employee_id,salary_month):
        salary_id =  "SID" + shortuuid.ShortUUID().random(length=4)
        data = self.db_object.fetch_data(Queries.QUERY_TO_CALCULATE_LEAVES,(employee_id,))
        
        if not data:
            return False
        else:
            dates = [date[0].split('-')[1] for date in data]
            count_leaves = dates.count(salary_month)
            base_salary_day = AppConfig.BASE_SALARY/30
            total_leaves = abs(count_leaves-AppConfig.PAID_LEAVES)
            total_leaves_amount = total_leaves * base_salary_day
            salary = AppConfig.BASE_SALARY - total_leaves_amount

            self.db_object.save_data(Queries.QUERY_TO_ADD_SALARY,(salary_id,salary,salary_month,'approved',employee_id,))
            return True
