from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
