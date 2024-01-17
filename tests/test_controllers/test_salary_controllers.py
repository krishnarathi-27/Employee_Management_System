import pytest
from src.controllers.salary_controllers import SalaryControllers

class TestSalaryControllers:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_salary_controller = SalaryControllers(mocker.Mock())

    def test_view_salary(self,mock_init):
        self.obj_salary_controller.db_object.fetch_data.return_value = ["data"]
        assert self.obj_salary_controller.view_salary() == ["data"]

    def test_self_salary(self,mock_init):
        self.obj_salary_controller.db_object.fetch_data.return_value = ["amkds"]
        assert self.obj_salary_controller.view_self_salary("1212") == ["amkds"]

    def test_check_employee_id_positive(self,mock_init):
        self.obj_salary_controller.db_object.fetch_data.return_value = ["amkds"]
        assert self.obj_salary_controller.check_employee_id("1212") == True

    def test_check_employee_id_negative(self,mock_init):
        self.obj_salary_controller.db_object.fetch_data.return_value = []
        assert self.obj_salary_controller.check_employee_id("1212") == False

    def test_save_salary_status_negative(self,mock_init):
        self.obj_salary_controller.db_object.fetch_data.return_value = []
        assert self.obj_salary_controller.save_salary_status("1212","01") == False

    def test_save_salary_status_positive(self,mock_init):
        self.obj_salary_controller.db_object.fetch_data.return_value = [('2023-10-10',), ('2023-11-10',)]
        self.obj_salary_controller.db_object.save_data.return_value = None
        assert self.obj_salary_controller.save_salary_status("1212","01") == True
   