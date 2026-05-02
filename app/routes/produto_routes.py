from fastapi import APIRouter, HTTPException, status
from app.schemas.produto_schema import ProdutoSchema
from app.services import produto_service
from app.utils.response import success_response

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/", summary="Listar produtos")
def listar():
    produtos = produto_service.listar_produtos()
    return success_response(produtos, "Lista de produtos")

@router.get("/{produto_id}", summary="Buscar produto por ID")
def buscar(produto_id: int):
    produto = produto_service.buscar_produto(produto_id)

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return success_response(produto)

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar(produto: ProdutoSchema):
    novo = produto_service.criar_produto(produto)
    return success_response(novo, "Produto criado com sucesso")