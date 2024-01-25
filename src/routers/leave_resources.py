import sqlite3
import shortuuid
from fastapi import APIRouter, HTTPException, Body, Path
from starlette import status
from controllers.leaves_controllers import LeavesControllers
from schemas.leave_schema import LeaveSchema

leave_obj = LeavesControllers()

router = APIRouter()

@router.get("/leaves",status_code=status.HTTP_200_OK)
async def get_leaves():
    try:
        data = leave_obj.view_leaves()
        if data:
            return data
        else:
            raise HTTPException(404, "Leaves data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.get("/leave/{user_id}",status_code=status.HTTP_200_OK)
async def get_leaves_by_id(user_id):
    try:
        data = leave_obj.view_leaves_employee(user_id)
        if data:
            return data
        else:
            raise HTTPException(404, "Leaves data not found")
        
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
    
@router.post("/leaves",status_code=status.HTTP_201_CREATED)
async def post_leaves(leave_data = Body()):
    leave_id = "LID" + shortuuid.ShortUUID().random(length=4)
    try:  
        result = leave_obj.save_leaves(leave_id,leave_data['employee_id'],leave_data['leaves_date'])

        if result: 

            return {"message" :"Leaves added successfully"}
        
        raise HTTPException(500, detail="Server not responding")
    except sqlite3.IntegrityError:
        raise HTTPException(409, detail="Resource already exists")
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")

@router.patch("/leave/{leave_id}",status_code=status.HTTP_200_OK)
async def update_leaves(leave_id ,leave_data = Body()):  
    try:
        leave_obj.update_leaves(leave_data['leaves_status'],leave_id)
        return {"message" :"Leaves updated successfully"}
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")
