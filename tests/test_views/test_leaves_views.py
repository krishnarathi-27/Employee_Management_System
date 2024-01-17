import pytest
from src.views.leaves_views import LeavesViews

class TestLeavesViews:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_leaves_views = LeavesViews(mocker.Mock())

    def test_display_leaves_positive(self,mocker,mock_init):
        mocker.patch('src.views.leaves_views.LeavesControllers.view_leaves',return_value = ["data"])
        mocker.patch('src.views.leaves_views.CommonHelper.display_table')
        assert self.obj_leaves_views.display_leaves() == None

    def test_display_leaves_negative(self,mocker,mock_init):
        mocker.patch('src.views.leaves_views.LeavesControllers.view_leaves',return_value = [])
        assert self.obj_leaves_views.display_leaves() == None

    def test_apply_leaves(self,mocker,mock_init):
        mocker.patch('src.views.leaves_views.InputValidations.input_date',return_value = ['2023-02-20'])
        mocker.patch('src.views.leaves_views.LeavesControllers.save_leaves')

        assert self.obj_leaves_views.apply_leaves("swdew") == None 

    def test_update_leaves_status(self,mocker,mock_init):
        mocker.patch('src.views.leaves_views.LeavesViews.display_leaves')
        mocker.patch('src.views.leaves_views.InputValidations.input_leave_id',return_value=['LIDsd32'])

        mocker.patch('builtins.input',side_effect = ['1','2','3'])

        mocker.patch('src.views.leaves_views.LeavesControllers.update_leaves')

        assert self.obj_leaves_views.update_leaves_status() == None
        assert self.obj_leaves_views.update_leaves_status() == None
        assert self.obj_leaves_views.update_leaves_status() == None

    def test_display_status_positive(self,mocker,mock_init):
        mocker.patch('src.views.leaves_views.LeavesControllers.view_leaves_employee',return_value = ["data"])
        mocker.patch('src.views.leaves_views.CommonHelper.display_table')
        assert self.obj_leaves_views.display_leaves_status("crfv") == None

    def test_display_status_negative(self,mocker,mock_init):
        mocker.patch('src.views.leaves_views.LeavesControllers.view_leaves_employee',return_value = [])
        assert self.obj_leaves_views.display_leaves_status("xsdcr") == None