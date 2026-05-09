from fastapi import APIRouter

router = APIRouter(prefix="/fidelidade", tags=["Fidelidade"])

@router.get("/saldo")
def saldo():
    return {"pontos": 120}

@router.get("/historico")
def historico():
    return [{"pontos": 10, "tipo": "compra"}]

from app.schemas.fidelidade_schema import FidelidadeRequest


@router.post("/comprar")
def comprar_pontos(dados: FidelidadeRequest):

    return {
        "msg": "Compra realizada",
        "dados": dados
    }

@router.post("/recarga")
def recarga_pontos(dados: FidelidadeRequest):

    return {
        "msg": "Recarga realizada",
        "dados": dados
    }