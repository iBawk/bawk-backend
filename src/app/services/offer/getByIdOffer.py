from sqlalchemy.orm import Session

from app.repositories.offer.offerRepository import OfferRepository
from app.repositories.products.productRepository import ProductRepository
from app.repositories.user.userRepository import UserRepository


class GetOfferByIdService:
    def __init__(self, db=Session):
        self.db = db
        self.offer_repository = OfferRepository(db)
        self.product_repository = ProductRepository(db)
        self.user_repository = UserRepository(db)
        
    def execute(self, offer_id):
        
        offer = self.offer_repository.find_by_id(offer_id)
        if not offer:
            return {}
        
        product = self.product_repository.find_by_id(offer.product_id)
        
        saller = self.user_repository.get_user_by_id(product.owner_id)
        
        return {
            "id": offer.id,
            "price": offer.price,
            "marketplace": offer.marketplace,
            "situation": offer.situation,
            "product": {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "saller": {
                    "id": saller.id,
                    "name": saller.name,
                    "email": saller.email,
                }
            }
        }