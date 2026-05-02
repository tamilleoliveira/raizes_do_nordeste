from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import produto_service

router = APIRouter(prefix="/produtos", tags=["Produtos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar(nome: str, preco: float, db: Session = Depends(get_db)):
    return produto_service.criar_produto(db, nome, preco)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)