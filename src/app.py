from fastapi import FastAPI
from routers.auth_resources import router as auth_router
from routers.leave_resources import router as leave_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(leave_router)