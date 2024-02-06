from fastapi.testclient import TestClient
from fastapi import status
from app import app
 
client = TestClient(app)

 
def test_get_all_users(override_admin):
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK

def test_get_all_users_by_id(override_admin):
    response = client.get("/user/EMPkris")
    assert response.status_code == status.HTTP_200_OK

def test_get_all_users_by_id_negative(override_admin):
    response = client.get("/user/EMPkrde")
    assert response.json() == {"detail" :"User data not found"}
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_post_new_user(override_admin):
    request_data = {'role': 'employee','username': 'krishna','password': 'Krishna@12','age': '23',
                        'mail': 'krishna@gmail.com','gender': 'female',
                                    'phone': '6776767676'}
    response = client.post("/users",json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

