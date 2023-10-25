import hashlib
import sys
from prettytable import PrettyTable
from .exceptions import RowDoesNotExistException
from DAO.db_context_manager import DatabaseContextManager
import DAO.query_base as q


def create_table(query) -> None:
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()
        cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)

def add_data(query,*args) -> None:
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor() 
        cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)

def login_user(query,username: str,password: str) -> str:
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(query,(username,hashed_password))
        record = cursor.fetchone()
        if record == None:
            return None  
        else:
            return (record[3],record[0])        
        
def delete_data(query,employee_id: int) -> None:
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
            var = cursor.execute(query,(employee_id,))
            if var.rowcount == 0:
                raise RowDoesNotExistException
        except RowDoesNotExistException:
            print("Error occured !!! Row does not exist can't delete user")
            sys.exit()

def display_data(query,table_schema: list) -> None:
     with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()
        try:    
            var = cursor.execute(query)
            if var.rowcount == 0:
                raise RowDoesNotExistException
        except RowDoesNotExistException:
            print("Error occured !!! Row does not exist")
            sys.exit()
        else:
            table = PrettyTable(table_schema)
            for row in cursor.fetchall():
                table.add_row(row)
            print(table)

def update_data(query,*args) -> None:
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()   
        cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  

def display_employee_data(query,employee_id: int, table_schema: list):
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()
        table = PrettyTable(table_schema)
        table.add_row(cursor.execute(query,(employee_id,)).fetchone())
        print(table)    

def calculate_leaves(query,employee_id) -> int:
    with DatabaseContextManager('employee_management.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query,(employee_id,))
        var = len(cursor.fetchall())
        return var