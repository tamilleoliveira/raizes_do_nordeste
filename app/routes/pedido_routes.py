from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", status_code=201)
def criar_pedido():
    return {"msg": "Pedido criado"}

@router.get("/{id}")
def buscar_pedido(id: int):
    return {"pedido_id": id}

@router.patch("/{id}/status")
def atualizar_status(id: int):
    return {"msg": f"Status do pedido {id} atualizado"}