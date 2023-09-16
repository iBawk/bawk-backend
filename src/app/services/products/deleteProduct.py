import datetime as datetime

from app.repositories.products.productRepository import ProductRepository
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


class DeleteProductService:
    def __init__(self, db=Session) -> None:
        self.product_repository = ProductRepository(db)

    def execute(self, id: str):
        product_to_delete = self.product_repository.find_by_id(id)
        if not product_to_delete:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Este produto não existe.")

        self.product_repository.delete(product=product_to_delete)

        return HTTPException(
            status_code=status.HTTP_200_OK, detail="Produto deletado com sucesso.")
