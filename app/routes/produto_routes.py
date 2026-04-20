from fastapi import APIRouter, HTTPException
from app.schemas.produto_schema import Produto
from app.models.produto import produtos

router = APIRouter()

@router.get("/produtos")
def listar_produtos():
    return produtos

@router.post("/produtos")
def criar_produto(produto: Produto):
    produto.id = len(produtos) + 1
    produtos.append(produto)
    return produto

@router.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    for produto in produtos:
        if produto.id == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, novo_produto: Produto):
    for i, produto in enumerate(produtos):
        if produto.id == produto_id:
            novo_produto.id = produto_id
            produtos[i] = novo_produto
            return novo_produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    for produto in produtos:
        if produto.id == produto_id:
            produtos.remove(produto)
            return {"mensagem": "Produto removido"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")