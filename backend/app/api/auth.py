from fastapi import APIRouter

from backend.app.schemas.auth import LoginRequest, RegisterRequest
from backend.app.services.auth_service import login_user, register_user

router = APIRouter()


@router.post("/auth/login")
def login(data: LoginRequest):
    return login_user(data)


@router.post("/auth/register")
def register(data: RegisterRequest):
    return register_user(data)