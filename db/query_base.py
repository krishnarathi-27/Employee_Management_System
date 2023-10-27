QUERY_FOR_CREATE_AUTH_TABLE ='''CREATE TABLE IF NOT EXISTS authentication
                                (employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT, 
                                password TEXT, 
                                role TEXT,
                                is_changed INTEGER) 
                            '''

QUERY_FOR_CREATE_EMP_DETAILS_TABLE ='''CREATE TABLE IF NOT EXISTS employee_details
                                    (employee_id INTEGER PRIMARY KEY,
                                     employee_mail TEXT UNIQUE,
                                     employee_age INTEGER,
                                     employee_phone INTEGER UNIQUE,
                                     employee_gender TEXT,
                                     FOREIGN KEY (employee_id) REFERENCES authentication(employee_id) ON DELETE CASCADE)
                                    '''

QUERY_FOR_CREATE_LEAVES_TABLE = '''CREATE TABLE IF NOT EXISTS leaves_table
                                   (leaves_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    leaves_date TEXT,
                                    leave_status TEXT DEFAULT "pending",
                                    employee_id INTEGER,
                                    FOREIGN KEY (employee_id) REFERENCES authentication(employee_id)
                                    ON DELETE CASCADE)
                                '''

QUERY_FOR_CREATE_SALARY_TABLE = '''CREATE TABLE IF NOT EXISTS salary_table
                                   (salary_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    salary_to_paid INTEGER,
                                    salary_month TEXT,
                                    salary_status TEXT,
                                    employee_id INTEGER,
                                    FOREIGN KEY (employee_id) REFERENCES authentication(employee_id)
                                    ON DELETE CASCADE)
                                '''

QUERY_TO_CREATE_CONFIG_TABLE = '''CREATE TABLE IF NOT EXISTS config_table
                                  (config_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   config_name TEXT,
                                   config_value INTEGER)
                               '''


QUERY_TO_ADD_IN_AUTH_TABLE = '''INSERT INTO authentication
                                (username,password,role,is_changed) 
                                VALUES(?,?,?,0)
                            '''

QUERY_TO_ADD_IN_EMP_DETAILS_TABLE = '''INSERT INTO employee_details
                                       (employee_mail,employee_age,employee_phone,employee_gender) 
                                        VALUES(?,?,?,?)
                                    '''

QUERY_TO_ADD_IN_CONFIG_TABLE = '''INSERT INTO config_table
                                       (config_name, config_value) 
                                        VALUES(?,?)
                                    '''

QUERY_TO_VERIFY_LOGIN = '''SELECT * FROM authentication
                           WHERE username=? AND
                           password=?
                        '''

QUERY_TO_DELETE_FROM_AUTH_TABLE = '''DELETE FROM authentication 
                              WHERE employee_id = ?
                           '''


QUERY_TO_DELETE_FROM_EMPLOYEE_TABLE = '''DELETE FROM employee_details 
                                        WHERE employee_id = ?
                                      '''

QUERY_TO_ENABLE_FOREIGN_KEY = '''PRAGMA foreign_keys = 1
                              '''

QUERY_TO_DISPLAY_EMPLOYEE_DETAILS = '''SELECT authentication.employee_id, username, employee_mail, employee_age, employee_phone, employee_gender
                                       FROM authentication
                                       INNER JOIN employee_details ON authentication.employee_id = employee_details.employee_id
                                    '''

QUERY_TO_DISPLAY_LEAVES_DETAILS = '''SELECT * FROM leaves_table'''

QUERY_TO_UPDATE_LEAVES_STATUS = '''UPDATE leaves_table 
                                   SET leave_status = ? 
                                   WHERE leaves_id = ?
                                '''

QUERY_TO_FETCH_CONFIG_DATA = '''SELECT config_value 
                                FROM config_table
                                WHERE config_name = ?
                             '''

QUERY_TO_CALCULATE_LEAVES = '''SELECT * FROM leaves_table 
                               WHERE employee_id = ? AND 
                               leave_status = 'approved'
                            '''

QUERY_TO_ADD_SALARY = ''' INSERT INTO salary_table
                          (salary_to_paid, salary_month, salary_status, employee_id)
                          VALUES(?,?,?,?)
                      '''

QUERY_TO_CHECK_IF_DEFAULT_PASWORD = '''SELECT is_changed
                                     FROM authentication
                                     WHERE username = ?
                                  '''

QUERY_TO_CHANGE_DEFAULT_PASWORD = '''UPDATE authentication
                                     SET password = ?,is_changed = 1
                                     WHERE username = ?
                                  '''

LIST_TO_DISPLAY_EMPLOYEE_DETAILS = ['Employee_id','Username','Employee_mail','Employee_age','Employee_phone','Employee_gender']

LIST_TO_DISPLAY_LEAVES_DETAILS = ['Leave_id','Leave_date','Leave_status','Employee_id']