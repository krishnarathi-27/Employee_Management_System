"""Module having buisness logic of admin functionalities"""
import logging
import hashlib

# local imports
from config.queries import Queries
from config.logs.logging_config import LoggingConfig

logger = logging.getLogger("admin_controller")


class LeavesControllers:
    """
    Class containing methods to create new user
    """
    def __init__(self,db_object):
        self.db_object = db_object

    def view_leaves(self):
        data = self.db_object.fetch_data(Queries.QUERY_TO_DISPLAY_LEAVES_DETAILS)
        return data
    
    def save_leaves(self,leave_id,user_id,leaves_date):
        self.db_object.save_data(Queries.QUERY_TO_ADD_IN_LEAVE_TABLE,(leave_id,user_id,leaves_date,))

    def update_leaves(self,leave_status,leave_id) : 
        self.db_object.save_data(Queries.QUERY_TO_UPDATE_LEAVES_STATUS,(leave_status,leave_id,))

    def view_leaves_employee(self,user_id):
        data = self.db_object.fetch_data(Queries.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS, (user_id,))
        return data