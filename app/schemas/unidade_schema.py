from pydantic import BaseModel


class UnidadeCreate(BaseModel):
    nome: str
    endereco: str