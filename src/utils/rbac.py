import functools
import os
from fastapi import HTTPException
from jose import jwt, JWTError
from dotenv import load_dotenv
from starlette import status

load_dotenv()
SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = 'HS256'

def role_required(roles_list):

    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                token = kwargs.get('token')
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                print(payload)
                role: str = payload.get('sub')
                user_id: int = payload.get('id')
                print(role, user_id)
                if role is None or user_id is None:
                    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail ='Could not validate user.')
                print(roles_list)
                if role in roles_list:
                    return func(*args, **kwargs)
                else:
                    raise HTTPException(status_code=403, detail='Access denied')
            except JWTError as error:
                print(error)
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail ='Could not validate user.')
        return wrapper

    return inner

