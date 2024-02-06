from fastapi.testclient import TestClient
from fastapi import status
from app import app

client = TestClient(app)

def test_create_leaves(override_employee):
    request_data = {'employee_id': 'EMPkris', 'leaves_date': '2023-02-10'}
    response = client.post("/leaves", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

def test_get_leaves_by_id(override_employee):
    response = client.get("/leave/EMPkris")
    assert response.status_code == status.HTTP_200_OK

def test_get_leaves_by_id_negative(override_employee):
    response = client.get("/leave/EMPkri")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_leaves(override_admin):
    response = client.get("/leaves")
    assert response.status_code == status.HTTP_200_OK

def test_update_leaves(override_admin):
    request_data = {'leaves_status': 'approved'}
    response = client.patch("/leave/LIDkris", json=request_data)
    assert response.status_code == status.HTTP_200_OK
