import pytest
from src.controllers.auth_controllers import AuthControllers

class TestAuthControllers:

    @pytest.fixture
    def mock_init(self,mocker):
        self.auth_controller_obj = AuthControllers(mocker.Mock())
    
    def test_valid_first_login_positive(self,mock_init,mocker):
        mocker.patch('src.controllers.auth_controllers.CommonHelper.change_default_password',return_value = None)
        assert self.auth_controller_obj.valid_first_login("admin","Admin@123","Admin@123") == True
    
    def test_valid_first_login_negative(self,mock_init):
        assert self.auth_controller_obj.valid_first_login("admin","Admin123","Admin@123") == False

    @pytest.mark.parametrize('roles',['admin','employee'])
    def test_role_based_access_positive(self,mock_init,mocker,roles):
        mocker.patch('src.controllers.auth_controllers.AdminViews.admin_menu_operations',return_value = None)
        mocker.patch('src.controllers.auth_controllers.EmployeeViews.employee_menu_operations',return_value = None)

        assert self.auth_controller_obj.role_based_access(roles,'snwuiqn') == True

    def test_role_based_access_negative(self,mock_init):
        assert self.auth_controller_obj.role_based_access("sadcre",'snwuiqn') == False

    def test_validate_user_positive(self, mock_init,mocker) -> bool:
        self.auth_controller_obj.db_object.fetch_data.side_effect = [
            [("EMPdsse", "User@1234", "admin", "true")],
            [("EMPdsse", "User@1234", "admin", "false")],
        ]
        mocker.patch('src.controllers.auth_controllers.hashlib.sha256', return_value = mocker.Mock(hexdigest = lambda : "User@1234"))
        mocker.patch('src.controllers.auth_controllers.AuthControllers.valid_first_login', return_value = True)
        mocker.patch('src.controllers.auth_controllers.AuthControllers.role_based_access', return_value = True)
        assert self.auth_controller_obj.validate_user("name", "pwd") == True
        assert self.auth_controller_obj.validate_user("name", "User@1234") == True

    def test_validate_user_negative(self, mock_init):
        self.auth_controller_obj.db_object.fetch_data.return_value = []
        assert self.auth_controller_obj.validate_user("name", "pwd") == False