import pytest
from src.controllers.admin_controllers import AdminControllers

class TestAdminControllers:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj = AdminControllers(mocker.Mock())
        
    def test_view_user(self,mock_init):
        self.obj.db_object.fetch_data.return_value = ["data"]
        assert self.obj.view_user() == ["data"]

    def test_create_new_user(self,mock_init):
        self.obj.db_object.save_data.return_value = None
        assert self.obj.create_new_user("EMPdwes","employee","emp","Emp@123") == None

    def test_create_employee_details(self,mock_init):
        self.obj.db_object.save_data.return_value = None
        assert self.obj.create_employee_details("1","22","emp@mail.com","F","9876567897") == None

    def test_check_employee_id_positive(self,mock_init):
        self.obj.db_object.fetch_data.return_value = []
        assert self.obj.check_employee_id("121") == False

    def test_check_employee_id_negative(self,mock_init):
        self.obj.db_object.fetch_data.return_value = ["data"]
        assert self.obj.check_employee_id("121") == True

    def test_delete_existing_user(self,mock_init):
        self.obj.db_object.save_data.return_value = None
        assert self.obj.delete_exisiting_user("1ds") == None
        