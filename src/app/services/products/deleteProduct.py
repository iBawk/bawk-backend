from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository


class DeleteProductService:
    def __init__(self, db=Session) -> None:
        self.product_repository = ProductRepository(db)

    def execute(self, idToSerach: str):
        product_to_delete = self.product_repository.find_by_id(product_id=idToSerach)
        if not product_to_delete:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Este produto não existe.")

        self.product_repository.delete(product=product_to_delete)

        return HTTPException(
            status_code=status.HTTP_200_OK, detail="Produto deletado com sucesso.")
