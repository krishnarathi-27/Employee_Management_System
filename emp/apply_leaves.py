from datetime import datetime
from config.print_statements import PrintConfig
from config.queries_emp_config import QueriesEmp
from db import database as db


class ApplyLeaves: 

    def __init__(self,user_id):
        self.user_id = user_id
        self.format = "%Y-%m-%d"
              
    def apply_leaves(self):
        db.add_data(QueriesEmp.QUERY_TO_ADD_IN_LEAVE_TABLE,(self.leave_date,self.user_id))

    def fetch_leaves_date(self): 
        while True:      
            self.leave_date = input(PrintConfig.ENTER_DATE)
            try:
                bool(datetime.strptime(self.leave_date, self.format))
                break
            except ValueError:
                print(PrintConfig.WRONG_DATE_FORMAT)                       
        leaves_applied = db.fetch_data(QueriesEmp.QUERY_TO_FETCH_LEAVES_DATE_FOR_EMPLOYEE,(self.user_id,self.leave_date))
        if len(leaves_applied) == 0:
            self.apply_leaves()
        else:
            print(PrintConfig.LEAVE_ERROR)
        
