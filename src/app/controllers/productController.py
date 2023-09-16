from sqlalchemy.orm import Session
from fastapi import Depends
from app.services.products.createProduct import CreateProductService
from app.services.products.deleteProduct import DeleteProductService
from app.services.products.getProductById import GetProductByIdService


class productController:
    def __init__(self, db=Session):
        self.db = db
        self.create_product_service = CreateProductService(db)
        self.delete_product_service = DeleteProductService(db)
        self.get_product_by_id = GetProductByIdService(db)

    def createProduct(self, product, user):
        return self.create_product_service.execute(product, user)

    def deleteProduct(self, id):
        return self.delete_product_service.execute(id)

    def getProductById(self, id):
        return self.get_product_by_id.execute(id)