from fastapi import APIRouter
from app.schemas.pagamento_schema import PagamentoRequest

router = APIRouter(
    prefix="/pagamento",
    tags=["Pagamento"]
)

# SIMULAÇÃO DE PAGAMENTO
@router.post("/")
def simular_pagamento(pagamento: PagamentoRequest):

    return {
        "mensagem": "Pagamento processado com sucesso",
        "status": "processando",
        "dados": pagamento
    }


# CONFIRMAÇÃO DE PAGAMENTO
@router.post("/confirmar")
def confirmar_pagamento(pagamento: PagamentoRequest):

    return {
        "mensagem": "Pagamento confirmado",
        "status": "confirmado",
        "dados": pagamento
    }