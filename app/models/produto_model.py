from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)
    
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco