import sqlite3
from fastapi import APIRouter, HTTPException
from controllers.auth_controllers import AuthControllers
from starlette import status
from schemas.user_schema import LoginSchema

obj_auth_controller = AuthControllers()

router = APIRouter()

@router.post("/login",status_code=status.HTTP_200_OK)
async def login_user(request_data : LoginSchema):

    try:
        role = obj_auth_controller.validate_user(request_data['username'],request_data['password'])

        if not role:
            raise HTTPException(401, detail="Invalid credeentials")
        return {"message": "User logged in "}
    except sqlite3.Error:
        raise HTTPException(500, detail="Server not responding")