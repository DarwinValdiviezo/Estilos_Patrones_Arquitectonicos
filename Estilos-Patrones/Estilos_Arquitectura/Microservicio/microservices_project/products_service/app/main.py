from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/products", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)
