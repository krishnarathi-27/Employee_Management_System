"""This Module provides all methods related for database operations"""
import sqlite3
from typing import Union

# local imports
from config.app_config import AppConfig
from config.queries import Queries


class Database:
    """
    This class contains method to perform all database related operations
    ...
    Methods
    -------
    init() : To create connection and cursor
    create_all_tables() : To create all the table
    save_data() : To save data in database
    fetch_data() : TO fetch data from database
    """

    def __init__(self) -> None:
        """
        This method creates sqlite connection and cursor
        Parameters = self
        Return Type = None
        """
        try:
            self.connection = sqlite3.connect(AppConfig.DATABASE_LOCATION)
            self.cursor = self.connection.cursor()
        except sqlite3.Error:
            raise sqlite3.Error

    def create_all_table(self) -> None:
        """
        This method creates all tables of not exists
        Parameters = self
        Return Type = None
        """
        self.cursor.execute(Queries.QUERY_FOR_CREATE_AUTH_TABLE)
        self.cursor.execute(Queries.QUERY_FOR_CREATE_EMP_DETAILS_TABLE)
        self.cursor.execute(Queries.QUERY_FOR_CREATE_LEAVES_TABLE)
        self.cursor.execute(Queries.QUERY_FOR_CREATE_SALARY_TABLE)

    def save_data(self, query: Union[str, list], data: Union[tuple, list]) -> None:
        """
        This saves data in the database
        Parameters = query that can we either string or list, tuple
        Return Type = None
        """
        if isinstance(query, str):
            self.cursor.execute(query, data)
        else:
            for i in range(0, len(query)):
                self.cursor.execute(query[i], data[i])
        self.connection.commit()

    def fetch_data(self, query: str, tup: tuple = None) -> list:
        """
        This fetches data in the database
        Parameters = query, tuple
        Return Type = List
        """
        if not tup:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tup)
        data = self.cursor.fetchall()
        return data


db = Database()