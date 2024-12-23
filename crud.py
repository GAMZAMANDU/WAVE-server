from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schema

from schema import UserCreate, UserLogin, UserLoginOut
from models import User
from jwt_config import create_access_token

default_json = [
    { 
        "hand_id": 0,
        "name": "swipe",
        "icon": "file_open",
        "content": { "0": "https://www.google.com" }
    },
    {
        "hand_id": 1,
        "name": "V",
        "icon": "cancel",
        "content": { "1": "5min" }
    },
    {
        "hand_id": 2,
        "name": "Index finger",
        "icon": "cancel",
        "content": { "2": None }
    },
    {
        "hand_id": 3,
        "name": "Three fingers",
        "icon": "add_circle",
        "content": { "3": None }
    }
]

############################ USER ############################
def create_user(db: Session, user: UserCreate):
    db_user = User(name = user.name, password=user.password, handler_config=default_json)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db:Session, user:UserLogin):
    db_user = db.query(User.id, User.name, User.handler_config).filter(User.name == user.name, User.password == user.password).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유저 이름이나 비밀번호가 잘못되었습니다."
        )

    access_token = create_access_token(data={'sub': db_user.name})

    return UserLoginOut(
        id = db_user.id,
        name = db_user.name,
        handle_config = db_user.handler_config,
        access_token=access_token
    )