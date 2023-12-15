import logging
import shortuuid
from config.queries import Headers
from config.prompts.prompts_config import PromptsConfig
from utils.common_helper import CommonHelper
from utils.validations import InputValidations
from config.logs.logging_config import LoggingConfig
from controllers.leaves_controllers import LeavesControllers

class LeavesViews:

    def __init__(self,db_object) -> None:
        self.obj_common_helper = CommonHelper(db_object)
        self.obj_leaves_controller = LeavesControllers(db_object)

    def display_leaves(self) -> None:
        """ Method to display fetched leaves from table """

        data = self.obj_leaves_controller.view_leaves()
        if not data:
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Headers.LIST_TO_DISPLAY_LEAVES_DETAILS)

    def apply_leaves(self,user_id) -> None:

        leave_id = "LID" + shortuuid.ShortUUID().random(length=4)
        date = InputValidations.input_date()
        self.obj_leaves_controller.save_leaves(leave_id,user_id,date)

        print("Leave applied successfully")

    def update_leaves_status(self) -> None:
        self.display_leaves()
        leave_id = InputValidations.input_leave_id()

        while True:
            leave_status = input(PromptsConfig.LEAVE_STATUS_PROMPT)
            if leave_status == '1':
                leave_status = "approved"
                break
            elif leave_status == '2':
                leave_status = "rejected"
                break
            elif leave_status == "3":
                leave_status = "cancelled"
                break
            else:
                print(PromptsConfig.INVALID_INPUT)

        self.obj_leaves_controller.update_leaves(leave_status,leave_id)
        print("Leaves status updated successfully")

    def display_leaves_status(self, user_id) -> None:

        data = self.obj_leaves_controller.view_leaves_employee(user_id)
        print(data)
        if not data:
            print(PromptsConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Headers.LIST_TO_DISPLAY_SELFLEAVES_DETAILS)