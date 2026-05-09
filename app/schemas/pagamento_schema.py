from pydantic import BaseModel


class PagamentoRequest(BaseModel):
    pedido_id: int
    valor: float
    metodo: str