from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey,SmallInteger
from app.models.base import Base
from sqlalchemy.orm import relationships


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationships("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(30), nullable=False)
    # book = relationships("Book")
    # bid = Column(Integer, ForeignKey("book.id"))
    launched = Column(Boolean, default=False)

