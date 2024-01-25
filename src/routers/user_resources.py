import sqlite3
import shortuuid
from fastapi import APIRouter, HTTPException, Body, Path
from starlette import status
from controllers.admin_controllers import AdminControllers
from controllers.employee_controllers import EmployeeControllers
from schemas.leave_schema import LeaveSchema

admin_obj = AdminControllers()
emp_obj = EmployeeControllers()


router = APIRouter()

@router.get("/users",status_code=status.HTTP_200_OK)
async def get_leaves():
    try:
        data = admin_obj.view_user()
        if data:
            return data
        else:
            raise HTTPException(404, "Uer data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.get("/user/{user_id}",status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id):
    try:
        data  = emp_obj.view_details(user_id)
        if data:
            return data
        else:
            raise HTTPException(404, "User data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.post("/leaves",status_code=status.HTTP_201_CREATED)
async def post_leaves(user_data = Body()):
    leave_id = "LID" + shortuuid.ShortUUID().random(length=4)
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


