from sqlalchemy import Column, Integer, Enum
from app.database import Base

from app.schemas.pedido_schema import CanalPedido


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, nullable=False)

    produto_id = Column(Integer, nullable=False)

    quantidade = Column(Integer, nullable=False)

    canalPedido = Column(
        Enum(CanalPedido),
        nullable=False
    )