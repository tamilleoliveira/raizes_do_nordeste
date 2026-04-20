from fastapi import FastAPI
from app.routes import produto_routes

app = FastAPI(
    title="API Raízes do Nordeste",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}

app.include_router(produto_routes.router)