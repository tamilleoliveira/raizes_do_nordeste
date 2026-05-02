from fastapi import APIRouter

router = APIRouter(prefix="/fidelidade", tags=["Fidelidade"])

@router.get("/saldo")
def saldo():
    return {"pontos": 120}

@router.get("/historico")
def historico():
    return [{"pontos": 10, "tipo": "compra"}]

@router.post("/comprar")
def comprar():
    return {"message": "Compra realizada"}

@router.post("/recarga")
def recarga():
    return {"message": "Recarga realizada"}