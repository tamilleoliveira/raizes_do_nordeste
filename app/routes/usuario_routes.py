from fastapi import APIRouter

router = APIRouter(prefix="/clientes", tags=["Usuarios"])

@router.post("/")
def criar_usuario():
    return {"message": "Usuário criado"}

@router.get("/perfil")
def perfil():
    return {"nome": "Tamile", "email": "tamile.oliveira@hotmail.com"} 