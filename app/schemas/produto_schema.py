from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    preco: float = Field(..., gt=0)
    estoque: int = Field(..., ge=0)
    descricao: str

class ProdutoResponse(ProdutoCreate):
    id: int

    class Config:
        from_attributes = True