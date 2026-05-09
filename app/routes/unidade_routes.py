from fastapi import APIRouter

router = APIRouter(prefix="/unidades", tags=["Unidades"])
from app.schemas.unidade_schema import UnidadeCreate


@router.post("/")
def criar_unidade(unidade: UnidadeCreate):

    return unidade