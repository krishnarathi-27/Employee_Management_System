import pytest
from datetime import timedelta
from app import app
from routers.user_routers import oauth2_bearer
from routers.auth_routers import create_access_token
from models.database import Database, AppConfig
 
@pytest.fixture(scope='package',autouse=True)
def create_test_db(package_mocker):
    package_mocker.patch.object(AppConfig,'DATABASE_LOCATION', AppConfig.TEST_DB_PATH)
 
    Database.create_all_table()
  
 
@pytest.fixture(scope='package', autouse=True)
def insert_into_table():
    Database.save_data("INSERT INTO authentication (employee_id, username, password, role) VALUES (?,?,?,?)", ("EMPkris","agrima","Agrima@123","employee"))
    Database.save_data("INSERT INTO employee_details (employee_id,employee_age,employee_mail,employee_gender,employee_phone) VALUES(?,?,?,?,?)",("EMPkris","23","agrima@gmail.com","female","9876543212"))
    Database.save_data("INSERT INTO leaves_table (leaves_id,employee_id,leaves_date) values(?,?,?)", ("LIDkris","EMPkris","2023-10-21"))
    Database.save_data("INSERT INTO salary_table (salary_id,salary_to_paid, salary_month, salary_status, employee_id) VALUES(?,?,?,?,?)", ("SIDkris","30000","01","approved","EMPkris"))
    yield
    Database.delete_data("DROP TABLE authentication")
    Database.delete_data("DROP TABLE employee_details")
    Database.delete_data("DROP TABLE leaves_table")
    Database.delete_data("DROP TABLE salary_table")

@pytest.fixture
def override_employee():
    def get_test_token_employee():
        return create_access_token('employee','EMPded1',timedelta(minutes=15))

    app.dependency_overrides[oauth2_bearer] = get_test_token_employee
    yield
    app.dependency_overrides = {}

@pytest.fixture
def override_admin():
    def get_test_token_admin():
        return create_access_token('admin','EMPdede',timedelta(minutes=15))

    app.dependency_overrides[oauth2_bearer] = get_test_token_admin
    yield
    app.dependency_overrides = {}