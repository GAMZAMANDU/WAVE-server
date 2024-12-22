from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_user, login_user
from schema import UserCreate, UserOut, UserLogin
from database import get_db
from fastapi.middleware.cors import CORSMiddleware
import crud, models, schema
from database import SessionLocal, engine

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

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  return crud.create_user(db=db, user=user)

@app.post("/login")
def get_login(user: UserLogin, db: Session = Depends(get_db)):
  return crud.login_user(db=db, user=user)