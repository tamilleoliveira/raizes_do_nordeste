from fastapi import APIRouter
from app.schemas.estoque_schema import EstoqueMovimentacao

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

@router.post("/entrada")
def entrada_estoque(dados: EstoqueMovimentacao):
    return {
        "mensagem": "Entrada registrada",
        "dados": dados
    }

@router.post("/saida")
def saida(dados: EstoqueMovimentacao):

    return {
        "msg": "Saída realizada",
        "dados": dados
    }