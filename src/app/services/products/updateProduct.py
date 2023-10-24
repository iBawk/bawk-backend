from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository
from app.schemas.products.productSchema import Product


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

        product.name = product_data.name or product.name
        product.description = product_data.description or product.description
        product.category = product_data.category or product.category
        product.format = product_data.format or product.format
        product.markdown = product_data.markdown or product.markdown
        product.sallerInEmail = product_data.sallerInEmail or product.sallerInEmail
        product.sallerInName = product_data.sallerInName or product.sallerInName
        product.sallerInPhone = product_data.sallerInPhone or product.sallerInPhone
        product.status = product_data.status or product.status

        newProduct = self.product_repository.update_product(product)

        return newProduct
