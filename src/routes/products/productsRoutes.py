from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.productController import productController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.productSchema import Product
from db.models import UserModel
from lib.depends import get_db_Session

productRoutes = APIRouter()


@productRoutes.post('', summary="Cria um produto.")
def createProduct(
        product: Product, user: UserModel = Depends(verifyJWT),
        db: Session = Depends(get_db_Session)
):
    product_controller = productController(db)

    try:
        return product_controller.createProduct(product, user)
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )


@productRoutes.delete('', summary="Delete um produto.")
def deleteProduct(
    id: str,
    user: UserModel = Depends(verifyJWT),
    db: Session = Depends(get_db_Session)
):
    product_controller = productController(db)

    try:
        return product_controller.deleteProduct(id)
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )


@productRoutes.get('/{id}', summary="Mostra um produto pelo id.")
def getProducById(id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    product_controller = productController(db)

    try:
        return product_controller.getProductById(id)

    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )
