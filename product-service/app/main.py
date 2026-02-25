from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(dd, product)       


@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/products/", response_model=List[schemas.Product])
def get_all_products(db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return products    