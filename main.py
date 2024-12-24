from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_user, login_user
from schema import UserCreate, UserRes, UserLogin, UserLoginRes,JWTverify
from database import get_db
from fastapi.middleware.cors import CORSMiddleware
import crud, models, schema
from database import SessionLocal, engine
from jwt_config import decode_access_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
####################### USER #######################

@app.post("/users", response_model=UserRes)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  return crud.create_user(db=db, user=user)

@app.post("/login", response_model=UserLoginRes)
def get_login(user: UserLogin, db: Session = Depends(get_db)):
  return crud.login_user(db=db, user=user)

# @app.get("/run", response_model=runRes)
# def run(data : JWTverify , db: Session = Depends(get_db)):
#   return crud.get_handler(db=db, data=data)

# @app.get("/test")
# def test(access_token: str):
#   return decode_access_token(access_token)