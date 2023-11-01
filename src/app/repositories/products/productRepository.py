from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from db.models import ProductModel


class ProductRepository:
    def __init__(self, db: Session):
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

    def find_by_id(self, product_id: str):
        return self.db.query(ProductModel).filter_by(id=product_id).first()

    def delete(self, product: ProductModel):
        self.db.add(product)
        self.db.commit()
        return product

    def find_products_by_owner_id(self, owner_id: str):
        return self.db.query(ProductModel).filter_by(owner_id=owner_id).filter(ProductModel.situation == 1).all()
    
    def update_product(self, newProduct: ProductModel):
        try:
            self.db.add(newProduct)
            self.db.commit()
            self.db.refresh(newProduct)

            return newProduct
        except DatabaseError as e:
            print(e)
            raise (e)