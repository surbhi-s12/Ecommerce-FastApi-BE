from sqlalchemy.orm import Session
from . import model, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = model.Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_all_products(db: Session):
    return db.query(model.Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(model.Product).filter(model.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(model.Product).filter(model.Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(model.Product).filter(model.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product