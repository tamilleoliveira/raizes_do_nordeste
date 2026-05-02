from pydantic import BaseModel, Field

class ProdutoSchema(BaseModel):
    id: int
    nome: str = Field(..., min_length=3, max_length=100)
    preco: float = Field(..., gt=0)
    estoque: int = Field(..., ge=0)