from fastapi import APIRouter
from app.schemas.pagamento_schema import PagamentoRequest

router = APIRouter(
    prefix="/pagamento",
    tags=["Pagamento"]
)

@router.post("/pagamento")
def realizar_pagamento(pagamento: PagamentoRequest):
    return {
        "mensagem": "Pagamento realizado com sucesso",
        "dados": pagamento
    }

@router.post("/confirmar")
def confirmar_pagamento(dados: PagamentoRequest):

    return {
        "status": "confirmado",
        "dados": dados
    }
@router.post("/cancelar")
def cancelar_pagamento(dados: PagamentoRequest):

    return {
        "status": "cancelado",
        "dados": dados
    }