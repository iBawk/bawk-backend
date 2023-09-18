from sqlalchemy.orm import Session

from app.services.products.createProduct import CreateProductService
from app.services.products.deleteProduct import DeleteProductService
from app.services.products.findProductById import FindByIdProductService
from app.services.products.findAllProductUser import FindAllProductUserService
from app.services.products.updateProduct import UpdateProductService
from app.schemas.productSchema import Product
from db.models import UserModel


class productController:
    def __init__(self, db=Session):
        self.db = db
        self.create_product_service = CreateProductService(db)
        self.delete_product_service = DeleteProductService(db)
        self.find_by_id_product_service = FindByIdProductService(db)
        self.find_all_product_user_service = FindAllProductUserService(db)
        self.update_service = UpdateProductService(db)

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

    def findAllProductsUser(self, user: UserModel):
        try:
            return self.find_all_product_user_service.execute(user)
        except Exception as e:
            print(e)
            raise e
    
    def update(self, productId, Product: Product):
        try:
            return self.update_service.execute(productId, Product)
        except Exception as e:
            print(e)
            raise e