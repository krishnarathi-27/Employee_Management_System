import pytest
from src.utils.validations import InputValidations

class TestInputValidations:
    
    def test_input_name(self,mocker):
        mocker.patch('builtins.input', side_effect=[' ','12','_(s)','krishna'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_name() == 'krishna'

    def test_input_email(self,mocker):
        mocker.patch('builtins.input', side_effect=['krish','krish@cs','krish.com','krishna@gmail.com'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_email() == 'krishna@gmail.com'

    def test_input_password(self,mocker):
        mocker.patch('maskpass.askpass', side_effect=['krish','krish@','krish@1','Krishna@1'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_password() == 'Krishna@1'

    def test_input_age(self,mocker):
        mocker.patch('builtins.input', side_effect=[' ','kri','234321','21'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_age() == '21'

    def test_input_phone(self,mocker):
        mocker.patch('builtins.input', side_effect=['krish','3123','2123131','9878798732'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_phone() == '9878798732'

    def test_input_gender(self,mocker):
        mocker.patch('builtins.input', side_effect=[' ','sd','F','M'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,True,True])

        assert InputValidations.input_gender() == 'Female'
        assert InputValidations.input_gender() == 'Male'

    def test_input_user_id(self,mocker):
        mocker.patch('builtins.input', side_effect=[' ','krish@cs','EMP32--','EMP4r32'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_user_id() == 'EMP4r32'

    def test_leave_id(self,mocker):
        mocker.patch('builtins.input', side_effect=[' ','krish@cs','Lsdae','LID3r3r'])
        mocker.patch('src.utils.validations.re.match',side_effect =[False,False,False,True])

        assert InputValidations.input_leave_id() == 'LID3r3r'

    def test_input_date_positive(self,mocker):
        mocker.patch('builtins.input', side_effect=['2021-32-90','2023-32-21','2023-02-21'])

        assert InputValidations.input_date() == '2023-02-21'
