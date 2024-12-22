from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schema

from schema import UserCreate, UserLogin, UserLoginOut
from models import User, Handle
from jwt_config import create_access_token

############################ USER ############################
def create_user(db: Session, user: UserCreate):
    db_user = User(name = user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db:Session, user:UserLogin):
    db_user = db.query(User.id, User.name).filter(User.name == user.name, User.password == user.password).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유저 이름이나 비밀번호가 잘못되었습니다."
        )

    db_handle = db.query(Handle.id, Handle.controles).filter(Handle.id == db_user.id).all()
    access_token = create_access_token(data={'sub': db_user.name})

    return UserLoginOut(
        id = db_user.id,
        name = db_user.name,
        handle_config = db_handle,
        access_token=access_token
    )