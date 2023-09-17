from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository
from db.models import UserModel


class FindAllProductUserService:
    def __init__(self, db=Session):
        self.product_repository = ProductRepository(db)

    def execute(self, user: UserModel):
        show_products = self.product_repository.find_products_by_owner_id(
            owner_id=user.id
        )

        return show_products
