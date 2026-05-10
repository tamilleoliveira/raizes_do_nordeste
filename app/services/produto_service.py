from app.models.produto_model import Produto

# LISTAR
def listar_produtos(db):
    return db.query(Produto).all()

# BUSCAR POR ID
def buscar_produto_por_id(db, produto_id):
    return db.query(Produto).filter(Produto.id == produto_id).first()

# CRIAR
def criar_produto(db, produto):
    novo_produto = Produto(**produto.dict())

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto

# ATUALIZAR
def atualizar_produto(db, produto_id, produto):
    produto_db = buscar_produto_por_id(db, produto_id)

    if not produto_db:
        return None

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.estoque = produto.estoque
    produto_db.descricao = produto.descricao

    db.commit()
    db.refresh(produto_db)

    return produto_db

# DELETAR
def deletar_produto(db, produto_id):
    produto_db = buscar_produto_por_id(db, produto_id)

    if not produto_db:
        return False

    db.delete(produto_db)
    db.commit()

    return True