from fastapi import FastAPI
from app.routes import produto_routes

app = FastAPI(
    title="Raízes do Nordeste API",
    description="API para gestão de pedidos e produtos",
    version="1.0.0"
)

app.include_router(produto_routes.router)