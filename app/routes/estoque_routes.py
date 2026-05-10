from fastapi import APIRouter
from app.schemas.estoque_schema import EstoqueMovimentacao

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

# ENTRADA DE ESTOQUE
@router.post("/entrada")
def entrada_estoque(dados: EstoqueMovimentacao):
    return {
        "mensagem": "Entrada registrada",
        "dados": dados
    }

# SAÍDA DE ESTOQUE
@router.post("/saida")
def saida(dados: EstoqueMovimentacao):

    return {
        "msg": "Saída realizada",
        "dados": dados
    }

# CONSULTA POR UNIDADE
@router.get("/unidade/{unidade_id}")
def consultar_estoque_unidade(unidade_id: int):

    return {
        "unidade_id": unidade_id,
        "produtos": [
            {
                "produto": "Cuscuz",
                "quantidade": 30
            },
            {
                "produto": "Tapioca",
                "quantidade": 15
            }
        ]
    }