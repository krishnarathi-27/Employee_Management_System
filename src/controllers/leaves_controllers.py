"""Module having buisness logic of admin functionalities"""
import logging

# local imports
from models.database import db as db_object
from config.queries import Queries

logger = logging.getLogger("leave_controller")


class LeavesControllers:
    """
    Class containing methods to create new user
    """
    # def __init__(self,db_object):
    #     self.db_object = db_object

    def view_leaves(self):
        data = db_object.fetch_data(Queries.QUERY_TO_DISPLAY_LEAVES_DETAILS)
        return data
    
    def save_leaves(self,leave_id,user_id,leaves_date):
        result = db_object.save_data(Queries.QUERY_TO_ADD_IN_LEAVE_TABLE,(leave_id,user_id,leaves_date,))
        return result

    def update_leaves(self,leave_status,leave_id) : 
        result = db_object.save_data(Queries.QUERY_TO_UPDATE_LEAVES_STATUS,(leave_status,leave_id,))
        return result

    def view_leaves_employee(self,user_id):
        data = db_object.fetch_data(Queries.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS, (user_id,))
        return data