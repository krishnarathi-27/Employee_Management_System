import sqlite3
import os
from jose import jwt
from starlette import status
from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

from controllers.auth_controllers import AuthControllers
from schemas.user_schema import LoginSchema

obj_auth_controller = AuthControllers()

router = APIRouter()

load_dotenv()
SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = 'HS256'

@router.post("/login",status_code=status.HTTP_200_OK)
async def login_user(request_data: LoginSchema):

    try:
        result = obj_auth_controller.validate_user(request_data.username,request_data.password)

        if not result:
            raise HTTPException(401, detail="Invalid credeentials")

        token = create_access_token(result[0], result[1], timedelta(minutes=15))
        return {'token' : token,
                'message': "User logged in Successfully"
                }
    
    except sqlite3.Error as Error:
        print(Error)
        raise HTTPException(500, detail="Server not responding")
    
def create_access_token(role: str, user_id: str, expires_delta: timedelta):

    encode = {'sub': role, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)   
    