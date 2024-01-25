import sqlite3
import shortuuid
from fastapi import APIRouter, HTTPException, Body, Path
from starlette import status
from controllers.salary_controllers import SalaryControllers

salary_obj = SalaryControllers()

router = APIRouter()

@router.get("/salary",status_code=status.HTTP_200_OK)
async def get_salary():
    try:
        data = salary_obj.view_salary()
        if data:
            return data
        else:
            raise HTTPException(404, "Salary data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.get("/salary/{user_id}",status_code=status.HTTP_200_OK)
async def get_salary_by_user_id(user_id):
    try:
        data = salary_obj.view_self_salary(user_id)
        if data:
            return data
        else:
            raise HTTPException(404, "Salary data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.post("/salary",status_code=status.HTTP_201_CREATED)
async def post_salary(salary_data = Body()):
    salary_id = "LID" + shortuuid.ShortUUID().random(length=4)
    try:  
        result = salary_obj.save_salary_status(salary_data['employee_id'],salary_data['salary_month'])

        if result: 
            return {"message" :"Leaves added successfully"}
            
        raise HTTPException(500, detail="Server not responding")
    
    except sqlite3.IntegrityError:
        raise HTTPException(409, detail="Resource already exists")
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")

