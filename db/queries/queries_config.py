import yaml
F_PATH_ADMIN_QUERIES = 'db\\queries\\queries_base_admin.yml'
F_PATH_EMP_QUERIES = 'db\\queries\\queries_base_emp.yml'

class QueriesConfig:
    """
    Maintains all the config variables
    """
    @classmethod
    def loadAdminQueries(cls):
        with open(F_PATH_ADMIN_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_FOR_CREATE_AUTH_TABLE = data['QUERY_FOR_CREATE_AUTH_TABLE']
            cls.QUERY_FOR_CREATE_EMP_DETAILS_TABLE = data['QUERY_FOR_CREATE_EMP_DETAILS_TABLE']
            cls.QUERY_FOR_CREATE_LEAVES_TABLE = data['QUERY_FOR_CREATE_LEAVES_TABLE']
            cls.QUERY_FOR_CREATE_SALARY_TABLE = data['QUERY_FOR_CREATE_SALARY_TABLE']
            cls.QUERY_TO_ADD_IN_AUTH_TABLE = data['QUERY_TO_ADD_IN_AUTH_TABLE']
            cls.QUERY_TO_ADD_IN_EMP_DETAILS_TABLE = data['QUERY_TO_ADD_IN_EMP_DETAILS_TABLE']
            cls.QUERY_TO_VERIFY_LOGIN = data['QUERY_TO_VERIFY_LOGIN']
            cls.QUERY_TO_DELETE_FROM_AUTH_TABLE = data['QUERY_TO_DELETE_FROM_AUTH_TABLE']
            cls.QUERY_TO_DELETE_FROM_EMPLOYEE_TABLE = data['QUERY_TO_DELETE_FROM_EMPLOYEE_TABLE']
            cls.QUERY_TO_ENABLE_FOREIGN_KEY = data['QUERY_TO_ENABLE_FOREIGN_KEY']
            cls.QUERY_TO_DISPLAY_EMPLOYEE_DETAILS = data['QUERY_TO_DISPLAY_EMPLOYEE_DETAILS']
            cls.QUERY_TO_DISPLAY_LEAVES_DETAILS = data['QUERY_TO_DISPLAY_LEAVES_DETAILS']
            cls.QUERY_TO_UPDATE_LEAVES_STATUS = data['QUERY_TO_UPDATE_LEAVES_STATUS']
            cls.QUERY_TO_CALCULATE_LEAVES = data['QUERY_TO_CALCULATE_LEAVES']
            cls.QUERY_TO_ADD_SALARY = data['QUERY_TO_ADD_SALARY']
            cls.QUERY_TO_CHECK_IF_DEFAULT_PASWORD = data['QUERY_TO_CHECK_IF_DEFAULT_PASWORD']
            cls.QUERY_TO_CHANGE_DEFAULT_PASWORD = data['QUERY_TO_CHANGE_DEFAULT_PASWORD']
            cls.LIST_TO_DISPLAY_EMPLOYEE_DETAILS = data['LIST_TO_DISPLAY_EMPLOYEE_DETAILS']
            cls.LIST_TO_DISPLAY_LEAVES_DETAILS = data['LIST_TO_DISPLAY_LEAVES_DETAILS']

    @classmethod
    def loadEmployeeQueries(cls):
        with open(F_PATH_EMP_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_ADD_IN_LEAVE_TABLE = data['QUERY_TO_ADD_IN_LEAVE_TABLE']
            cls.QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS = data['QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS']
            cls.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS = data['QUERY_TO_DISPLAY_SELF_LEAVES_STATUS']
            cls.QUERY_TO_DISPLAY_SALARY_STATUS = data['QUERY_TO_DISPLAY_SALARY_STATUS']
            cls.QUERY_TO_UPDATE_EMP_MAIL = data['QUERY_TO_UPDATE_EMP_MAIL']
            cls.QUERY_TO_UPDATE_EMP_AGE = data['QUERY_TO_UPDATE_EMP_AGE']
            cls.QUERY_TO_UPDATE_EMP_PHONE = data['QUERY_TO_UPDATE_EMP_PHONE']
            cls.QUERY_TO_UPDATE_EMP_GENDER = data['QUERY_TO_UPDATE_EMP_GENDER']
            cls.LIST_TO_DISPLAY_SELFEMPLOYEE_DETAILS = data['LIST_TO_DISPLAY_SELFEMPLOYEE_DETAILS']
            cls.LIST_TO_DISPLAY_SELFLEAVES_DETAILS = data['LIST_TO_DISPLAY_SELFLEAVES_DETAILS']
            cls.LIST_TO_DISPLAY_SELFSALARY_DETAILS = data['LIST_TO_DISPLAY_SELFSALARY_DETAILS']
