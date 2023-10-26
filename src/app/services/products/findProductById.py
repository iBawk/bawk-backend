from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository


class FindByIdProductService:
    def __init__(self, db=Session):
        self.product_repository = ProductRepository(db)

    def execute(self, product_id: str):
        show_product = self.product_repository.find_by_id(product_id)
        if not show_product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este produto não existe.")

        return show_product
