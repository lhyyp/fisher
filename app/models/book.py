from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), nullable=False, default="二营长")
    isbn = Column(String(30), nullable=False, unique=True)
    price = Column(String(20))
    binding = Column(String(50))
    publisher = Column(String(50))
    image = Column(String(50))
    summary = Column(String(1000))
    pages = Column(Integer)
    pubdate = Column(String(20))
