from fastapi import APIRouter

router = APIRouter(prefix="/unidades", tags=["Unidades"])

@router.get("/")
def listar_unidades():
    return [
        {"id": 1, "nome": "Unidade Centro"},
        {"id": 2, "nome": "Unidade Norte"}
    ]