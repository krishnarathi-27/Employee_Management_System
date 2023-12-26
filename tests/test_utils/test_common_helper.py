import pytest
from src.utils.common_helper import CommonHelper

class TestCommonHelper:

    @pytest.fixture
    def mock_init(self,mocker):
        self.obj_common_helper = CommonHelper(mocker.Mock())

    def test_change_default_password(self,mocker,mock_init):
        mocker.patch('src.utils.common_helper.InputValidations.input_password', side_effect = ["Admin@12","Admin@123","Admin@123","Admin@123"])
        mocker.patch('src.controllers.auth_controllers.hashlib.sha256', return_value = mocker.Mock(hexdigest = lambda : "Admin@123"))
        self.obj_common_helper.db_object.save_data.return_value = None

        assert self.obj_common_helper.change_default_password("admin") == None
        