"""This Module provides all methods related for database operations"""
import sqlite3
from typing import Union

# local imports
from config.app_config import AppConfig
from models.database_connection import DatabaseConnection
from config.queries import Queries


class Database:

    @staticmethod
    def create_all_table() -> None:
        with DatabaseConnection(AppConfig.DATABASE_LOCATION) as connection:
            cursor = connection.cursor()
            cursor.execute(Queries.QUERY_FOR_CREATE_AUTH_TABLE)
            cursor.execute(Queries.QUERY_FOR_CREATE_EMP_DETAILS_TABLE)
            cursor.execute(Queries.QUERY_FOR_CREATE_LEAVES_TABLE)
            cursor.execute(Queries.QUERY_FOR_CREATE_SALARY_TABLE)

    @staticmethod
    def save_data(query: Union[str, list], data: Union[tuple, list]) -> None:
        with DatabaseConnection(AppConfig.DATABASE_LOCATION) as connection:
            cursor = connection.cursor()
            if isinstance(query, str):
                cursor.execute(query, data)
            else:
                for i in range(0, len(query)):
                    cursor.execute(query[i], data[i])
            connection.commit()
            return cursor.lastrowid

    @staticmethod
    def fetch_data( query: str, tup: tuple = None) -> list:
        with DatabaseConnection(AppConfig.DATABASE_LOCATION) as connection:
            cursor = connection.cursor()
            if not tup:
                cursor.execute(query)
            else:
                cursor.execute(query, tup)
            data = cursor.fetchall()
            return data

    @staticmethod
    def delete_data( query: str, tup: tuple = None) -> None:
        with DatabaseConnection(AppConfig.DATABASE_LOCATION) as connection:
            cursor = connection.cursor()
            if not tup:
                cursor.execute(query)
            else:
                cursor.execute(query, tup)
            data = cursor.fetchall()
            return data
        