from fastapi import APIRouter
from app.schemas.auth_schema import LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(dados: LoginRequest):

    return {
        "token": "fake-jwt-token",
        "email": dados.email
    }

@router.post("/logout")
def logout():
    return {"message": "Logout realizado"}

@router.post("/refresh")
def refresh():
    return {"token": "novo-token"}