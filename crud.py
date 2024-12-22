from sqlalchemy.orm import Session
import models, schema

from schema import UserCreate
from models import User

############################ USER ############################
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(name = user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user