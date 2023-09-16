from sqlalchemy.orm import Session

from app.services.products.createProduct import CreateProductService
from app.services.products.deleteProduct import DeleteProductService
from app.services.products.findProductById import FindByIdProductService


class productController:
    def __init__(self, db=Session):
        self.db = db
        self.create_product_service = CreateProductService(db)
        self.delete_product_service = DeleteProductService(db)
        self.find_by_id_product_service = FindByIdProductService(db)

    def createProduct(self, product, user):
        try:
            return self.create_product_service.execute(product, user)
        except Exception as e:
            print(e)
            raise e

    def deleteProduct(self, productId):
        try:
            return self.delete_product_service.execute(productId)
        except Exception as e:
            print(e)
            raise e

    def findProductById(self, productId):
        try:
            return self.find_by_id_product_service.execute(productId)
        except Exception as e:
            print(e)
            raise e
