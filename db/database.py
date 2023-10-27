import hashlib
import sys
from prettytable import PrettyTable
from utils.exceptions import RowDoesNotExistException
from utils.config_class import Config
from .db_context_manager import DatabaseContextManager
import db.query_base as q


def create_table(query) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)

def add_data(query,*args) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor() 
        cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)

def fetch_user(query,username: str,password: str) -> str:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(query,(username,hashed_password))
        record = cursor.fetchone()
        if record == None:
            return None  
        else:
            return (record[3],record[0])        
        
def delete_data(query,employee_id: int) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
            var = cursor.execute(query,(employee_id,))
            if var.rowcount == 0:
                raise RowDoesNotExistException
        except RowDoesNotExistException:
            print(Config.ROW_NOT_EXISTS_MESSAGE)
            sys.exit()

def display_data(query,table_schema: list) -> None:
     with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        var = cursor.execute(query)
        if var.rowcount == 0:
            raise RowDoesNotExistException(Config.ROW_NOT_EXISTS_MESSAGE)
        else:        
            table = PrettyTable(table_schema)
            for row in cursor.fetchmany(5):
                table.add_row(row)
            print(table)

def update_data(query,*args) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()   
        cursor.execute(q.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  

def display_employee_data(query,employee_id: int, table_schema: list):
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        var = cursor.execute(query,(employee_id,))       
        if var.rowcount == 0:
            raise RowDoesNotExistException(Config.ROW_NOT_EXISTS_MESSAGE)
        else:
            table = PrettyTable(table_schema)
            table.add_row(cursor.fetchone())
            print(table)    

def fetch_leaves(query,employee_id) -> int:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query,(employee_id,))
        var = len(cursor.fetchall())
        return var
    
def fetch_data(query,str) -> list:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        record = cursor.execute(query,(str,)).fetchone()
        return record[0]