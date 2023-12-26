import pytest
from src.controllers.employee_controllers import EmployeeControllers

class TestEmployeeControllers:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_employee_controller = EmployeeControllers(mocker.Mock())

    def test_view_details(self,mock_init):
        self.obj_employee_controller.db_object.fetch_data.return_value = ["data"]
        assert self.obj_employee_controller.view_details("1212") == ["data"]

    def test_update_email(self,mock_init):
        self.obj_employee_controller.db_object.save_data.return_value = None
        assert self.obj_employee_controller.update_email("sa","1212") == None

    def test_update_age(self,mock_init):
        self.obj_employee_controller.db_object.save_data.return_value = None
        assert self.obj_employee_controller.update_age("sa","1212") == None

    def test_update_phone(self,mock_init):
        self.obj_employee_controller.db_object.save_data.return_value = None
        assert self.obj_employee_controller.update_phone("sa","1212") == None

    def test_update_gender(self,mock_init):
        self.obj_employee_controller.db_object.save_data.return_value = None
        assert self.obj_employee_controller.update_gender("sa","1212") == None