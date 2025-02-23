from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_menu():
    return [{"id": 1, "nome": "Pizza", "descricao": "Deliciosa pizza de queijo", "preco": 39.90}]
