from fastapi import Depends
from sqlalchemy.orm import Session

from db.models import ProductModel
from lib.depends import get_db_Session


class ProductRepository:
    def __init__(self, db: Session = Depends(get_db_Session)):
        self.db = db

    def create(self, product: ProductModel):
        try:
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            self.db.rollback()
            raise e

    def find_by_id(self, id: str):
        return self.db.query(ProductModel).filter_by(id=id).first()

    def delete(self, product: ProductModel):
        self.db.delete(product)
        self.db.commit()
        return product

    def find_products_by_owner_id(self, owner_id: str):
        return self.db.query(ProductModel).filter_by(owner_id=owner_id).all()
