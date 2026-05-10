from fastapi import APIRouter

router = APIRouter(
    prefix="/fidelidade",
    tags=["Fidelidade"]
)

# SALDO DE PONTOS
@router.get("/saldo")
def saldo():

    return {
        "cliente_id": 1,
        "pontos": 120
    }


# HISTÓRICO DE PONTOS
@router.get("/historico")
def historico():

    return [
        {
            "tipo": "compra",
            "pontos": 10
        },
        {
            "tipo": "resgate",
            "pontos": -5
        }
    ]


# CONSULTA GERAL DE PONTOS
@router.get("/pontos")
def pontos():

    return {
        "mensagem": "Consulta de pontos realizada",
        "saldo_atual": 120
    }