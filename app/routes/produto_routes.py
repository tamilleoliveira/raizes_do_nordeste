from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.produto_schema import ProdutoCreate, ProdutoResponse
from app.services import produto_service

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)

@router.post("/", response_model=ProdutoResponse)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return produto_service.criar_produto(db, produto)