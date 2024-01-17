"""This module contains all the queries of the project"""

class Queries:
    """Queries class is used to load queries"""

    QUERY_FOR_CREATE_AUTH_TABLE = """
        CREATE TABLE IF NOT EXISTS authentication
        (employee_id TEXT PRIMARY KEY,
        username TEXT UNIQUE, 
        password TEXT, 
        role TEXT,
        is_changed TEXT DEFAULT "false") 
    """

    QUERY_FOR_CREATE_EMP_DETAILS_TABLE = """
        CREATE TABLE IF NOT EXISTS employee_details
        (employee_id TEXT PRIMARY KEY,
        employee_mail TEXT UNIQUE,
        employee_age TEXT,
        employee_phone TEXT UNIQUE,
        employee_gender TEXT,
        FOREIGN KEY (employee_id) REFERENCES authentication(employee_id) ON DELETE CASCADE)
    """

    QUERY_FOR_CREATE_LEAVES_TABLE = """
        CREATE TABLE IF NOT EXISTS leaves_table
        (leaves_id TEXT PRIMARY KEY ,
        leaves_date TEXT,
        leave_status TEXT DEFAULT "pending",
        employee_id TEXT,
        UNIQUE (employee_id, leaves_date),
        FOREIGN KEY (employee_id) REFERENCES authentication(employee_id)
        ON DELETE CASCADE)
        
    """

    QUERY_FOR_CREATE_SALARY_TABLE = """
        CREATE TABLE IF NOT EXISTS salary_table
        (salary_id TEXT PRIMARY KEY,
        salary_to_paid TEXT,
        salary_month TEXT,
        salary_status TEXT,
        employee_id TEXT,
        FOREIGN KEY (employee_id) REFERENCES authentication(employee_id)
        ON DELETE CASCADE)
    """

    INSERT_USER_CREDENTIALS = """
        INSERT INTO authentication
        (employee_id, username, password, role)
        VALUES (?,?,?,?)  
    """

    QUERY_TO_ADD_IN_EMP_DETAILS_TABLE = """
        INSERT INTO employee_details
        (employee_id,employee_age,employee_mail,employee_gender,employee_phone) 
        VALUES(?,?,?,?,?)
    """

    QUERY_TO_VERIFY_LOGIN = """
        SELECT * FROM authentication
        WHERE username=? 
    """
    QUERY_TO_FETCH_EMPLOYEE_EXISTS = """
        SELECT * FROM authentication 
        WHERE employee_id = ?
    """
    QUERY_TO_DELETE_FROM_AUTH_TABLE = """
        DELETE FROM authentication 
        WHERE employee_id = ?
    """

    QUERY_TO_DELETE_FROM_EMPLOYEE_TABLE = """
        DELETE FROM employee_details 
        WHERE employee_id = ?
    """
    
    QUERY_TO_ENABLE_FOREIGN_KEY = """ PRAGMA foreign_keys = 1 """

    QUERY_TO_DISPLAY_EMPLOYEE_DETAILS = """ 
        SELECT authentication.employee_id, username, employee_mail, 
        employee_age, employee_phone, employee_gender
        FROM authentication
        INNER JOIN employee_details ON 
        authentication.employee_id = employee_details.employee_id
    """
    FETCH_AUTHENTICATION_TABLE = """
        SELECT employee_id, username, role
        FROM authentication  
    """
    FETCH_USER_CREDENTIALS = """
        SELECT employee_id, password, role, is_changed 
        FROM authentication WHERE username = ? 
    """
    QUERY_TO_DISPLAY_LEAVES_DETAILS = """ SELECT * FROM leaves_table """

    QUERY_TO_UPDATE_LEAVES_STATUS = """ 
        UPDATE leaves_table 
        SET leave_status = ? 
        WHERE leaves_id = ?
    """

    QUERY_TO_CALCULATE_LEAVES = """
        SELECT leaves_date FROM leaves_table 
        WHERE employee_id = ? AND 
        leave_status = 'approved'
    """

    QUERY_TO_ADD_SALARY = """
        INSERT INTO salary_table
        (salary_id,salary_to_paid, salary_month, salary_status, employee_id)
        VALUES(?,?,?,?,?)
    """

    QUERY_TO_CHECK_IF_DEFAULT_PASWORD = """
        SELECT is_changed
        FROM authentication
        WHERE username = ?
    """

    QUERY_TO_CHANGE_DEFAULT_PASWORD = """
        UPDATE authentication
        SET password = ?,is_changed = "true"
        WHERE username = ?
    """

    QUERY_TO_DISPLAY_SALARY_DETAILS = """ SELECT * FROM salary_table """

    QUERY_TO_ADD_IN_LEAVE_TABLE = """
        INSERT INTO leaves_table
        (leaves_id,employee_id,leaves_date)
        values(?,?,?)
    """

    QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS = """
        SELECT authentication.employee_id, authentication.username, 
        employee_details.employee_mail, employee_details.employee_age,
        employee_details.employee_phone, employee_details.employee_gender 
        FROM authentication 
        INNER JOIN employee_details
        ON authentication.employee_id = employee_details.employee_id 
        AND authentication.employee_id = ?
    """

    QUERY_TO_DISPLAY_SELF_LEAVES_STATUS = """
        SELECT leaves_id,leaves_date,leave_status 
        FROM leaves_table 
        WHERE employee_id = ?
    """
    QUERY_TO_DISPLAY_SELF_SALARY_STATUS = """
        SELECT salary_id,salary_to_paid,salary_month,salary_status 
        FROM salary_table 
        WHERE employee_id = ?
    """

    QUERY_TO_FETCH_LEAVES_DATE_FOR_EMPLOYEE = """
        SELECT leaves_date 
        FROM leaves_table 
        WHERE employee_id = ? 
        AND leaves_date = ?
    """

    QUERY_TO_DISPLAY_SALARY_STATUS = """
        SELECT * FROM salary_table 
        WHERE employee_id = ?
    """

    QUERY_TO_UPDATE_EMP_MAIL = """
        UPDATE employee_details 
        SET employee_mail = ? 
        WHERE employee_id = ?
    """

    QUERY_TO_UPDATE_EMP_AGE = """
        UPDATE employee_details 
        SET employee_age = ? 
        WHERE employee_id = ?
    """

    QUERY_TO_UPDATE_EMP_PHONE = """
        UPDATE employee_details 
        SET employee_phone = ? 
        WHERE employee_id = ?
    """

    QUERY_TO_UPDATE_EMP_GENDER = """
        UPDATE employee_details 
        SET employee_gender = ? 
        WHERE employee_id = ?
    """

class Headers:
     
    LIST_TO_DISPLAY_SELFEMPLOYEE_DETAILS = ['Employee_id','Username','Employee_mail','Employee_age','Employee_phone','Employee_gender']

    LIST_TO_DISPLAY_SELFLEAVES_DETAILS = ['Leave_id','Leave_date','Leave_status']

    LIST_TO_DISPLAY_SELFSALARY_DETAILS = ['Salary_id','Salary_to_paid','Salary_month','Salary_status']

    LIST_TO_DISPLAY_EMPLOYEE_DETAILS = ['Employee_id','Username','Employee_mail','Employee_age','Employee_phone','Employee_gender']

    LIST_TO_DISPLAY_LEAVES_DETAILS = ['Leave_id','Leave_date','Leave_status','Employee_id']

    LIST_TO_DISPLAY_SALARY_DETAILS = ['Salary_id','Salary_Paid','Salary_Month','Salary_status','Employee_id']