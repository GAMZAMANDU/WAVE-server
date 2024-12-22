from sqlalchemy.orm import Session
import models, schema

from schema import UserCreate, UserLogin, UserLoginOut
from models import User, Handle

############################ USER ############################
def create_user(db: Session, user: UserCreate):
    db_user = User(name = user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db:Session, user:UserLogin):
    db_user = db.query(User.id, User.name).filter(User.name == user.name, User.password == user.password).first()
    db_handle = db.query(Handle.id, Handle.controles).filter(Handle.id == db_user.id).all()
    return UserLoginOut(
        id = db_user.id,
        name = db_user.name,
        handle_config = db_handle
    )