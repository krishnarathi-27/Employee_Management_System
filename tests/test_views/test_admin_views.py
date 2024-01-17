import pytest
from src.views.admin_views import AdminViews

class TestAdminViews:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_admin_views = AdminViews(mocker.Mock())

    def test_create_user(self,mocker,mock_init):
        mocker.patch('src.views.admin_views.InputValidations.input_name',return_value = "krishna")
        mocker.patch('src.views.admin_views.InputValidations.input_password',return_value = "Krishna@1")
        mocker.patch('src.views.admin_views.InputValidations.input_email',return_value = "krishna@gmail.com")
        mocker.patch('src.views.admin_views.InputValidations.input_age',return_value = "21")
        mocker.patch('src.views.admin_views.InputValidations.input_phone',return_value = "9876785408")
        mocker.patch('src.views.admin_views.InputValidations.input_gender',return_value = "Female") 

        self.obj_admin_views.obj_admin_controller.create_new_user("EMpsda","employee","krishna","Krishna@1")
        self.obj_admin_views.obj_admin_controller.create_employee_details("EMPxaw2","21","krishna@gmail.com","Female","9876785408")  

        assert self.obj_admin_views.create_user() == None

    def test_display_user_negative(self,mock_init,mocker):  
        mocker.patch('src.views.admin_views.AdminControllers.view_user',return_value = [])
        assert self.obj_admin_views.display_user() == None

    def test_display_user_positive(self,mock_init,mocker):  
        mocker.patch('src.views.admin_views.AdminControllers.view_user',return_value = ["data"])
        mocker.patch('src.views.admin_views.CommonHelper.display_table',return_value = None)
        assert self.obj_admin_views.display_user() == None

    def test_delete_user_positive(self,mocker,mock_init):
        mocker.patch('src.views.admin_views.AdminViews.display_user',return_value = None)
        mocker.patch('src.views.admin_views.InputValidations.input_user_id',return_value = "EMPdew2")
        mocker.patch('src.views.admin_views.AdminControllers.check_employee_id',return_value = True)

        mocker.patch('src.views.admin_views.AdminControllers.delete_exisiting_user',return_value = None)

        assert self.obj_admin_views.delete_user() == None

    def test_delete_user_negative(self,mocker,mock_init):
        mocker.patch('src.views.admin_views.AdminViews.display_user',return_value = None)
        mocker.patch('src.views.admin_views.InputValidations.input_user_id',return_value = "EMPdew2")
        mocker.patch('src.views.admin_views.AdminControllers.check_employee_id',return_value = False)

        assert self.obj_admin_views.delete_user() == None

    def test_admin_menu_operations(self,mocker,mock_init):
        mocker.patch('src.views.admin_views.AdminViews.admin_menu',side_effect = [False,True])

        assert self.obj_admin_views.admin_menu_operations() == None

    def test_admin_menu_positive(self,mocker,mock_init):
        mocker.patch('builtins.input',side_effect = ['1','2','3','4','5','6','7','saw'])

        mocker.patch('src.views.admin_views.AdminViews.create_user')
        mocker.patch('src.views.admin_views.AdminViews.delete_user')
        mocker.patch('src.views.admin_views.AdminViews.display_user')
        mocker.patch('src.views.admin_views.LeavesViews.display_leaves')
        mocker.patch('src.views.admin_views.LeavesViews.update_leaves_status')
        mocker.patch('src.views.admin_views.SalaryViews.add_salary')
        mocker.patch('src.views.admin_views.SalaryViews.display_salary')

        for _ in range(8):
            assert self.obj_admin_views.admin_menu() == False
        self.obj_admin_views.create_user.assert_called_once()
        self.obj_admin_views.delete_user.assert_called_once()
        self.obj_admin_views.display_leaves.assert_called_once()
        self.obj_admin_views.update_leaves_status.assert_called_once()
        self.obj_admin_views.add_salary.assert_called_once()
        self.obj_admin_views.display_salary.assert_called_once()

    def test_admin_menu_negative(self,mock_init,mocker):
        mocker.patch('builtins.input',return_value ='8')
        assert self.obj_admin_views.admin_menu() == True