from app.models.produto_model import Produto

def listar_produtos(db):
    return db.query(Produto).all()

def criar_produto(db, produto):
    novo_produto = Produto(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque,
        descricao=produto.descricao
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto