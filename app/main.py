from fastapi import FastAPI

from app.routes import produto_routes
from app.routes import auth_routes
from app.routes import usuario_routes
from app.routes import unidade_routes
from app.routes import estoque_routes
from app.routes import pagamento_routes
from app.routes import fidelidade_routes
from app.routes import pedido_routes

from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(produto_routes.router)
app.include_router(auth_routes.router)
app.include_router(usuario_routes.router)
app.include_router(unidade_routes.router)
app.include_router(estoque_routes.router)
app.include_router(pagamento_routes.router)
app.include_router(fidelidade_routes.router)
app.include_router(pedido_routes.router)