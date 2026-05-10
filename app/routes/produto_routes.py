from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.produto_schema import ProdutoCreate, ProdutoResponse
from app.services import produto_service

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

# LISTAR TODOS
@router.get("/", response_model=list[ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)

# BUSCAR POR ID
@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar(produto_id: int, db: Session = Depends(get_db)):
    produto = produto_service.buscar_produto_por_id(db, produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto

# CRIAR
@router.post("/", response_model=ProdutoResponse)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return produto_service.criar_produto(db, produto)

# ATUALIZAR
@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar(produto_id: int, produto: ProdutoCreate, db: Session = Depends(get_db)):
    produto_atualizado = produto_service.atualizar_produto(
        db,
        produto_id,
        produto
    )

    if not produto_atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto_atualizado

# DELETAR
@router.delete("/{produto_id}")
def deletar(produto_id: int, db: Session = Depends(get_db)):
    sucesso = produto_service.deletar_produto(db, produto_id)

    if not sucesso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return {"mensagem": "Produto removido com sucesso"}