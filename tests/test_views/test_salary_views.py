import pytest
from src.views.salary_views import SalaryViews

class TestSalaryViews:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_salary_views = SalaryViews(mocker.Mock())

    def test_display_salary_positive(self,mocker,mock_init):
        mocker.patch('src.views.salary_views.SalaryControllers.view_salary',return_value = ["data"])
        mocker.patch('src.views.salary_views.CommonHelper.display_table')
        assert self.obj_salary_views.display_salary() == None

    def test_display_salary_negative(self,mocker,mock_init):
        mocker.patch('src.views.salary_views.SalaryControllers.view_salary',return_value = [])
        assert self.obj_salary_views.display_salary() == None