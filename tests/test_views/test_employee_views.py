import pytest
from src.views.employee_views import EmployeeViews

class TestEmployeeViews:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_employee_views = EmployeeViews(mocker.Mock(),"EMPis21")

    def test_display_user_display_negative(self,mock_init,mocker):  
        mocker.patch('src.views.employee_views.EmployeeControllers.view_details',return_value = [])
        assert self.obj_employee_views.display_user_details() == None

    def test_display_user_display_positive(self,mock_init,mocker):  
        mocker.patch('src.views.employee_views.EmployeeControllers.view_details',return_value = ["data"])
        mocker.patch('src.views.employee_views.CommonHelper.display_table',return_value = None)
        assert self.obj_employee_views.display_user_details() == None

    def test_employee_menu_operations(self,mocker,mock_init):
        mocker.patch('src.views.employee_views.EmployeeViews.employee_menu',side_effect = [False,True])

        assert self.obj_employee_views.employee_menu_operations() == None

    def test_update_menu_operations(self,mocker,mock_init):
        mocker.patch('src.views.employee_views.EmployeeViews.update_menu',side_effect = [False,True])

        assert self.obj_employee_views.update_menu_operations() == None

    def test_employee_menu_positive(self,mocker,mock_init):
        mocker.patch('builtins.input',side_effect = ['1','2','3','4','5','saw'])

        mocker.patch('src.views.employee_views.EmployeeViews.display_user_details')
        mocker.patch('src.views.employee_views.EmployeeViews.update_menu_operations')
        mocker.patch('src.views.employee_views.LeavesViews.apply_leaves')
        mocker.patch('src.views.employee_views.LeavesViews.display_leaves_status')
        mocker.patch('src.views.employee_views.SalaryViews.display_salary_status')

        for _ in range(6):
            assert self.obj_employee_views.employee_menu() == False
        self.obj_employee_views.display_user_details.assert_called_once()
        self.obj_employee_views.update_menu_operations.assert_called_once()
        self.obj_employee_views.apply_leaves.assert_called_once()
        self.obj_employee_views.display_leaves_status.assert_called_once()
        self.obj_employee_views.display_salary_status.assert_called_once()

    def test_update_menu_positive(self,mocker,mock_init):
        mocker.patch('builtins.input',side_effect = ['1','2','3','4','saw'])

        mocker.patch('src.views.employee_views.InputValidations.input_email',return_value = "lro@gmail.com")
        mocker.patch('src.views.employee_views.EmployeeControllers.update_email')
        mocker.patch('src.views.employee_views.InputValidations.input_age',return_value = "21")
        mocker.patch('src.views.employee_views.EmployeeControllers.update_age')
        mocker.patch('src.views.employee_views.InputValidations.input_phone',return_value = "9864534098")
        mocker.patch('src.views.employee_views.EmployeeControllers.update_phone')
        mocker.patch('src.views.employee_views.InputValidations.input_gender',return_value = "Male")
        mocker.patch('src.views.employee_views.EmployeeControllers.update_gender')

        for _ in range(5):
            assert self.obj_employee_views.update_menu() == False

    def test_employee_menu_negative(self,mock_init,mocker):
        mocker.patch('builtins.input',return_value ='6')
        assert self.obj_employee_views.employee_menu() == True

    def test_update_menu_negative(self,mock_init,mocker):
        mocker.patch('builtins.input',return_value ='5')
        assert self.obj_employee_views.update_menu() == True