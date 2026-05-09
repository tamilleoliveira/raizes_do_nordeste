from fastapi import APIRouter
from typing import Optional

from app.schemas.pedido_schema import (
    PedidoCreate,
    CanalPedido
)

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

# Simulação temporária
pedidos = []


@router.post("/", status_code=201)
def criar_pedido(pedido: PedidoCreate):

    novo_pedido = {
        "id": len(pedidos) + 1,
        "cliente_id": pedido.cliente_id,
        "produto_id": pedido.produto_id,
        "quantidade": pedido.quantidade,
        "canalPedido": pedido.canalPedido
    }

    pedidos.append(novo_pedido)

    return novo_pedido


@router.get("/")
def listar_pedidos(
    canalPedido: Optional[CanalPedido] = None
):

    if canalPedido:
        return [
            pedido for pedido in pedidos
            if pedido["canalPedido"] == canalPedido
        ]

    return pedidos


@router.get("/{id}")
def buscar_pedido(id: int):

    for pedido in pedidos:
        if pedido["id"] == id:
            return pedido

    return {"erro": "Pedido não encontrado"}


@router.patch("/{id}/status")
def atualizar_status(id: int):

    return {
        "msg": f"Status do pedido {id} atualizado"
    }