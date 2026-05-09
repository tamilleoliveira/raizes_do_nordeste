from pydantic import BaseModel


class EstoqueMovimentacao(BaseModel):
    produto_id: int
    quantidade: int