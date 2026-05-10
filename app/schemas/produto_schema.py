from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    estoque: int 
    descricao: str

class ProdutoResponse(ProdutoCreate):
    id: int

    class Config:
        from_attributes = True