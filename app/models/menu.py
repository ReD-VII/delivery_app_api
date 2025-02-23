from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class MenuItem(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
