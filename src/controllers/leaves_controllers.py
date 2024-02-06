"""Module having buisness logic of admin functionalities"""
import logging

# local imports
from models.database import Database
from config.queries import Queries

logger = logging.getLogger("leave_controller")


class LeavesControllers:
    """
    Class containing methods to create new user
    """

    def view_leaves(self):
        data = Database.fetch_data(Queries.QUERY_TO_DISPLAY_LEAVES_DETAILS)
        return data
    
    def save_leaves(self,leave_id,user_id,leaves_date):
        result = Database.save_data(Queries.QUERY_TO_ADD_IN_LEAVE_TABLE,(leave_id,user_id,leaves_date,))
        return result

    def update_leaves(self,leave_status,leave_id) : 
        result = Database.save_data(Queries.QUERY_TO_UPDATE_LEAVES_STATUS,(leave_status,leave_id,))
        return result

    def view_leaves_employee(self,user_id):
        data = Database.fetch_data(Queries.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS, (user_id,))
        return data
    