from fastapi import FastAPI
from app.routes import menu

app = FastAPI(title="API de Cardápio", version="1.0")

# Incluindo as rotas
app.include_router(menu.router, prefix="/menu", tags=["Menu"])

@app.get("/")
def home():
    return {"message": "Bem-vindo à API de Cardápio!"}
