from enum import Enum
from pydantic import BaseModel, Field


class CanalPedido(str, Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"


class PedidoCreate(BaseModel):
    cliente_id: int
    produto_id: int
    quantidade: int = Field(..., gt=0)

    canalPedido: CanalPedido


class PedidoResponse(PedidoCreate):
    id: int

    class Config:
        from_attributes = True