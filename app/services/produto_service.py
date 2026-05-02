from app.models.produto_model import Produto

produtos_db = []  # simulação

def listar_produtos():
    return produtos_db

def buscar_produto(produto_id: int):
    for p in produtos_db:
        if p.id == produto_id:
            return p
    return None

def criar_produto(produto):
    produtos_db.append(produto)
    return produto