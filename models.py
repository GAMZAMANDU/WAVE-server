from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column
from database import Base

class User(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)

class Handle(Base):
    __tablename__ = "handle"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    title = mapped_column(String(255), nullable=False)
    description = mapped_column(String(255))
    controles = mapped_column(String(1000))