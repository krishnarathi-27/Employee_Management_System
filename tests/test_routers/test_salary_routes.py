from fastapi.testclient import TestClient
from fastapi import status
from app import app

client = TestClient(app)

def test_get_salary(override_admin):
    response = client.get('/salary')
    assert response.status_code == status.HTTP_200_OK

def test_get_salary_by_id(override_admin):
    response = client.get('/salary/EMPkris')
    assert response.status_code == status.HTTP_200_OK

def test_get_salary_by_id_negative(override_admin):
    response = client.get('/salary/EMPkr4is')
    assert response.status_code == status.HTTP_404_NOT_FOUND