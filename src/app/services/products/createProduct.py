import uuid
from sqlalchemy.orm import Session
from app.repositories.products.productRepository import ProductRepository
from db.models import ProductModel, UserModel
from fastapi import HTTPException, status
import datetime as datetime
from app.schemas.productSchema import Product


class CreateProductService:
    def __init__(self, db=Session):
        self.db = db
        self.product_repostiry = ProductRepository(db)

    def execute(self, product: Product, user: UserModel):

        product_id = str(uuid.uuid4())
        id_existis = self.product_repostiry.find_by_id(product_id)
        if id_existis:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Houve um problema ao criar seu produto, tente novamente mais tarde.")

        newProduct = self.product_repostiry.create(
            ProductModel(
                id=product_id,
                owner_id=user.id,
                name=product.name,
                description=product.description,
                createDate=datetime.datetime.now(),
                format="mp3",
                status="pending",
                markdown=product.markdown,
            )
        )

        return newProduct
