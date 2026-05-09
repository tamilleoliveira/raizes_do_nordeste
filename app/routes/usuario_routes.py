from fastapi import APIRouter
from app.schemas.usuario_schema import UsuarioCreate

router = APIRouter(prefix="/clientes", tags=["Usuarios"])


@router.post("/")
def criar_usuario(usuario: UsuarioCreate):

    return {
        "msg": "Usuário criado",
        "usuario": usuario
    }

@router.get("/perfil")
def perfil():
    return {"nome": "Tamile", "email": "tamile.oliveira@hotmail.com"} 