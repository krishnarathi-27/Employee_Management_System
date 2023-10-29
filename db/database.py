import hashlib
import logging
import sys
from prettytable import PrettyTable
from config.constants_config import ConstantsConfig
from config.logging_config import LoggingConfig
from config.print_statements import PrintConfig
from config.queries_admin_config import QueriesAdmin
from utils.exceptions import RowDoesNotExistException
from .db_context_manager import DatabaseContextManager

logger = logging.getLogger('database')

def create_table(query) -> None:
    with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(QueriesAdmin.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)

def add_data(query,*args) -> None:
    with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
        cursor = connection.cursor() 
        cursor.execute(QueriesAdmin.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)    
        
def delete_data(query,employee_id: int) -> None:
    with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(QueriesAdmin.QUERY_TO_ENABLE_FOREIGN_KEY)
            var = cursor.execute(query,(employee_id,))
            if var.rowcount == 0:
                logging.critical(LoggingConfig.ERROR_MESSAGE)
                raise RowDoesNotExistException
        except RowDoesNotExistException:
            print(PrintConfig.ROW_NOT_EXISTS_MESSAGE)
            sys.exit()

def display_data(query,table_schema: list,employee_id = 0) -> None:
     with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        if employee_id == 0:
            var = cursor.execute(query)
        else:
            var = cursor.execute(query,(employee_id,))
        if var.rowcount == 0:
            logging.critical(LoggingConfig.ERROR_MESSAGE)
            raise RowDoesNotExistException(PrintConfig.ROW_NOT_EXISTS_MESSAGE)
        else:        
            table = PrettyTable(table_schema)
            for row in cursor.fetchall():
                table.add_row(row)
            print(table)

def update_data(query,*args) -> None:
    with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
        cursor = connection.cursor()   
        cursor.execute(QueriesAdmin.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  

# def display_employee_data(query,employee_id: int, table_schema: list):
#     with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
#         cursor = connection.cursor()
#         var = cursor.execute(query,(employee_id,))       
#         if var.rowcount == 0:
#             logging.critical(LoggingConfig.ERROR_MESSAGE)
#             raise RowDoesNotExistException(PrintConfig.ROW_NOT_EXISTS_MESSAGE)
#         else:
#             table = PrettyTable(table_schema)
#             row = cursor.fetchone()
#             table.add_row(row)
#             print(table)    

def fetch_data(query,tp) -> int:
    with DatabaseContextManager(ConstantsConfig.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query,tp)
        return cursor.fetchall()