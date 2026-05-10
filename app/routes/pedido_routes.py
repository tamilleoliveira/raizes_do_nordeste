from fastapi import APIRouter

from app.schemas.pedido_schema import PedidoCreate

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

# Simulação temporária
pedidos = []


# CRIAR PEDIDO
@router.post("/", status_code=201)
def criar_pedido(pedido: PedidoCreate):

    novo_pedido = {
        "id": len(pedidos) + 1,
        "cliente_id": pedido.cliente_id,
        "produto_id": pedido.produto_id,
        "quantidade": pedido.quantidade,
        "canalPedido": pedido.canalPedido,
        "status": "Em preparo"
    }

    pedidos.append(novo_pedido)

    return novo_pedido


# CONSULTAR PEDIDO
@router.get("/{id}")
def consultar_pedido(id: int):

    for pedido in pedidos:
        if pedido["id"] == id:
            return pedido

    return {"erro": "Pedido não encontrado"}


# ATUALIZAR STATUS
@router.patch("/{id}/status")
def atualizar_status(id: int, status: str):

    for pedido in pedidos:
        if pedido["id"] == id:
            pedido["status"] = status

            return {
                "msg": "Status atualizado",
                "pedido": pedido
            }

    return {"erro": "Pedido não encontrado"}