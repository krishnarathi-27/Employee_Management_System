import yaml
F_PATH_EMP_QUERIES = 'config_files\\queries_base_emp.yml'

class QueriesEmp:
    """
    Maintains all the config variables
    """
    @classmethod
    def load(cls):
        with open(F_PATH_EMP_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_ADD_IN_LEAVE_TABLE = data['QUERY_TO_ADD_IN_LEAVE_TABLE']
            cls.QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS = data['QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS']
            cls.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS = data['QUERY_TO_DISPLAY_SELF_LEAVES_STATUS']
            cls.QUERY_TO_DISPLAY_SALARY_STATUS = data['QUERY_TO_DISPLAY_SALARY_STATUS']
            cls.QUERY_TO_FETCH_LEAVES_DATE_FOR_EMPLOYEE = data['QUERY_TO_FETCH_LEAVES_DATE_FOR_EMPLOYEE']
            cls.QUERY_TO_UPDATE_EMP_MAIL = data['QUERY_TO_UPDATE_EMP_MAIL']
            cls.QUERY_TO_UPDATE_EMP_AGE = data['QUERY_TO_UPDATE_EMP_AGE']
            cls.QUERY_TO_UPDATE_EMP_PHONE = data['QUERY_TO_UPDATE_EMP_PHONE']
            cls.QUERY_TO_UPDATE_EMP_GENDER = data['QUERY_TO_UPDATE_EMP_GENDER']
            cls.LIST_TO_DISPLAY_SELFEMPLOYEE_DETAILS = data['LIST_TO_DISPLAY_SELFEMPLOYEE_DETAILS']
            cls.LIST_TO_DISPLAY_SELFLEAVES_DETAILS = data['LIST_TO_DISPLAY_SELFLEAVES_DETAILS']
            cls.LIST_TO_DISPLAY_SELFSALARY_DETAILS = data['LIST_TO_DISPLAY_SELFSALARY_DETAILS']