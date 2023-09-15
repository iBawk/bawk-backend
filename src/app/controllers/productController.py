from sqlalchemy.orm import Session
from fastapi import Depends
from app.services.products.createProduct import CreateProductService


class productController:
    def __init__(self, db=Session):
        self.db = db
        self.create_product_service = CreateProductService(db)

    def createProduct(self, product, user):
        return self.create_product_service.execute(product, user)
