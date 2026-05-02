from fastapi import APIRouter

router = APIRouter(prefix="/estoque", tags=["Estoque"])

@router.get("/")
def consultar_estoque():
    return {"produto": "Cuscuz", "quantidade": 50}

@router.post("/entrada")
def entrada():
    return {"message": "Entrada registrada"}

@router.post("/saida")
def saida():
    return {"message": "Saída registrada"}