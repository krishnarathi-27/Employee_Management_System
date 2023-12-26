import pytest
from src.controllers.leaves_controllers import LeavesControllers

class TestLeavesControllers:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_leaves_controller = LeavesControllers(mocker.Mock())

    def test_view_leaves(self,mock_init):
        self.obj_leaves_controller.db_object.fetch_data.return_value = ["data"]
        assert self.obj_leaves_controller.view_leaves() == ["data"]

    def test_save_leaves(self,mock_init):
        self.obj_leaves_controller.db_object.save_data.return_value = None
        assert self.obj_leaves_controller.save_leaves("sa","sdew","1212") == None

    def test_update_leaves(self,mock_init):
        self.obj_leaves_controller.db_object.save_data.return_value = None
        assert self.obj_leaves_controller.update_leaves("sa","1212") == None

    def test_view_leaves_employee(self,mock_init):
        self.obj_leaves_controller.db_object.fetch_data.return_value = ["saw"]
        assert self.obj_leaves_controller.view_leaves_employee("1212") == ["saw"]