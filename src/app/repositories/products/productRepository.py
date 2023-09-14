from sqlalchemy.orm import Session
from fastapi import Depends
from lib.depends import get_db_Session
from db.models import ProductModel


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
