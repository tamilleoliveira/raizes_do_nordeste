from sqlalchemy.orm import Session
from app.models.produto_model import Produto

def criar_produto(db: Session, nome: str, preco: float):
    produto = Produto(nome=nome, preco=preco)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def listar_produtos(db: Session):
    return db.query(Produto).all()