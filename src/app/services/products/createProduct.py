import datetime
import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.products.productRepository import ProductRepository
from app.schemas.productSchema import Product
from db.models import ProductModel, UserModel


class CreateProductService:
    def __init__(self, db=Session):
        self.db = db
        self.product_repository = ProductRepository(db)

    def execute(self, product: Product, user: UserModel):

        product_id = str(uuid.uuid4())
        id_existis = self.product_repository.find_by_id(product_id)
        if id_existis:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Houve um problema ao criar seu produto, tente novamente mais tarde."
            )

        newProduct = self.product_repository.create(
            ProductModel(
                id=product_id,
                owner_id=user.id,
                name=product.name,
                description=product.description,
                format=product.format,
                status=product.status,
                markdown=product.markdown,
                sallerInName=product.sallerInName,
                sallerInEmail=product.sallerInEmail,
                sallerInPhone=product.sallerInPhone,
                created_at=datetime.datetime.now()
            )
        )

        return newProduct
