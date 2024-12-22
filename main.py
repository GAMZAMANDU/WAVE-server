from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_user
from schema import UserCreate, UserOut
from database import get_db

import crud, models, schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

####################### USER #######################

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  return crud.create_user(db=db, user=user)