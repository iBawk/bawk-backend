from sqlalchemy.orm import Session
from db.models import WalletsModel

from app.repositories.products.productRepository import ProductRepository
from db.models import UserModel


class FindAllValluesService:
    def __init__(self, db=Session):
        self.product_repository = ProductRepository(db)
        self.db = db

    def execute(self, user: UserModel):
        show_vallues = self.db.query(WalletsModel).filter_by(user_id=user.id).first()

        return show_vallues
