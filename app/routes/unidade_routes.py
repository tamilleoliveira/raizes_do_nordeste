from fastapi import APIRouter

router = APIRouter(
    prefix="/unidades",
    tags=["Unidades"]
)

# LISTAR UNIDADES
@router.get("/")
def listar_unidades():
    return [
        {
            "id": 1,
            "nome": "Unidade Centro",
            "cidade": "São Paulo"
        },
        {
            "id": 2,
            "nome": "Unidade Zona Sul",
            "cidade": "Rio de Janeiro"
        }
    ]