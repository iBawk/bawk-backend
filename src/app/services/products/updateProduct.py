from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository
from app.schemas.productSchema import Product

class UpdateProductService:
    def __init__(self, db: Session):
        self.db = db
        self.product_repository = ProductRepository(db)

    def execute(self, product_id: str, product_data: Product):
        product = self.product_repository.find_by_id(id=product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Produto com ID {product_id} não encontrado.",
            )

        for field, value in product_data.model_dump().items():
            setattr(product, field, value)

        self.product_repository.update_product(product)

        return product