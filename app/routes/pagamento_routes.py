from fastapi import APIRouter

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])

@router.post("/simular")
def simular():
    return {"status": "aprovado"}

@router.post("/confirmar")
def confirmar():
    return {"message": "Pagamento confirmado"}  

@router.post("/cancelar")
def cancelar():
    return {"message": "Pagamento cancelado"}