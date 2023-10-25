QUERY_TO_ADD_IN_LEAVE_TABLE = '''INSERT INTO leaves_table
                                 (leaves_date,employee_id)
                                    values(?,?)
                              '''

QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS = '''SELECT * FROM employee_details
                                                WHERE employee_id = ?
                                             '''

QUERY_TO_DISPLAY_SELF_LEAVES_STATUS = '''SELECT * FROM leaves_table 
                                         WHERE employee_id = ?
                                      '''

QUERY_TO_DISPLAY_SALARY_STATUS = '''SELECT * FROM salary_table 
                                         WHERE employee_id = ?
                                      '''
QUERY_TO_UPDATE_EMP_MAIL =      '''UPDATE employee_details 
                                   SET employee_mail = ? 
                                   WHERE employee_id = ?
                                '''

QUERY_TO_UPDATE_EMP_AGE =      '''UPDATE employee_details 
                                   SET employee_age = ? 
                                   WHERE employee_id = ?
                                '''

QUERY_TO_UPDATE_EMP_PHONE =      '''UPDATE employee_details 
                                   SET employee_phone = ? 
                                   WHERE employee_id = ?
                                '''

QUERY_TO_UPDATE_EMP_GENDER =      '''UPDATE employee_details 
                                   SET employee_gender = ? 
                                   WHERE employee_id = ?
                                '''

LIST_TO_DISPLAY_EMPLOYEE_DETAILS = ['Username','Employee_mail','Employee_age','Employee_phone','Employee_gender']

LIST_TO_DISPLAY_LEAVES_DETAILS = ['Leave_id','Leave_date','Leave_status']

LIST_TO_DISPLAY_SALARY_DETAILS = ['Salary_id','Salary_to_paid','Salary_month','Salary_details']