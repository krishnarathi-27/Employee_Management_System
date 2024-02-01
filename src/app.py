from importlib import metadata
import secrets
from fastapi import FastAPI, Depends, HTTPException
from fastapi import security
from fastapi.responses import HTMLResponse, UJSONResponse
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status
from fastapi.openapi.docs import get_redoc_html,get_swagger_ui_html
from routers.auth_routers import router as auth_router
from routers.leave_routers import router as leave_router
from routers.user_routers import router as user_router
from routers.salary_routers import router as salary_router

security = HTTPBasic()

app = FastAPI(
    title="FastAPI",
    version=metadata.version("FastAPI"),
    docs_url=None,
    redoc_url=None,
    openapi_url="/api/openapi.json",
    default_response_class=UJSONResponse,
)
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    correct_username = secrets.compare_digest(credentials.username, "krishna")
    correct_password = secrets.compare_digest(credentials.password, "Krishna@13")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/docs", response_class=HTMLResponse)
async def get_docs(username: str = Depends(get_current_username)) -> HTMLResponse:
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="docs")


@app.get("/redoc", response_class=HTMLResponse)
async def get_redoc(username: str = Depends(get_current_username)) -> HTMLResponse:
    return get_redoc_html(openapi_url="/api/openapi.json", title="redoc")

app.include_router(auth_router)
app.include_router(leave_router)
app.include_router(user_router)
app.include_router(salary_router)
