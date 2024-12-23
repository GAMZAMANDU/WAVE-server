from typing import Dict, Union
from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import mapped_column
from database import Base
import json

ContentType = Dict[str, Union[str, None]]

class User(Base):
    __tablename__ = "users"
    
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)
    handler_config = mapped_column(JSON, nullable=True)
