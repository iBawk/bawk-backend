from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository


class DeleteProductService:
    def __init__(self, db=Session) -> None:
        self.product_repository = ProductRepository(db)

    def execute(self, product_id: str):
        product = self.product_repository.find_by_id(product_id)
        
        if not product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Este produto não existe.")
            
        product.situation = 2    
            
        self.product_repository.delete(product)

        return HTTPException(
            status_code=status.HTTP_200_OK, detail="Produto deletado com sucesso.")
