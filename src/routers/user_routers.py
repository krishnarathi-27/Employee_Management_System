import sqlite3
import shortuuid
from fastapi import APIRouter, HTTPException, Body, Path, Depends
from starlette import status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from utils.rbac import role_required
from controllers.admin_controllers import AdminControllers
from controllers.employee_controllers import EmployeeControllers

admin_obj = AdminControllers()
emp_obj = EmployeeControllers()

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/login')
token_dependency = Annotated[dict, Depends(oauth2_bearer)]

router = APIRouter()

@router.get("/users",status_code=status.HTTP_200_OK)
@role_required(["admin"])
def get_users(token : token_dependency):
    try:
        data = admin_obj.view_user()
        if data:
            return data
        else:
            raise HTTPException(404, "Uer data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.get("/user/{user_id}",status_code=status.HTTP_200_OK)
@role_required(["admin","employee"])
def get_user_by_id(user_id):
    try:
        data  = emp_obj.view_details(user_id)
        if data:
            return data
        else:
            raise HTTPException(404, "User data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.post("/users",status_code=status.HTTP_201_CREATED)
@role_required(["employee"])
def post_leaves(user_data = Body()):
    try:  
        employee_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        result = admin_obj.create_new_user(employee_id,user_data['role'],user_data['username'],user_data['password'],user_data['age'],
                                    user_data['mail'],user_data['gender'],user_data['phone'])

        if result: 
            
            return {"message" :"User created successfully"}
        
        raise HTTPException(500, detail="Server not responding")
    except sqlite3.IntegrityError:
        raise HTTPException(409, detail="Resource already exists")
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")

