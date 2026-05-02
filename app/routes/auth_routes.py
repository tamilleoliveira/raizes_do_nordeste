from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    return {"token": "fake-jwt-token"}

@router.post("/logout")
def logout():
    return {"message": "Logout realizado"}

@router.post("/refresh")
def refresh():
    return {"token": "novo-token"}