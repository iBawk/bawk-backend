from sqlalchemy.orm import Session

from app.repositories.offer.offerRepository import OfferRepository


class GetOffersPrpductService:
    def __init__(self, db=Session):
        self.db = db
        self.offer_repository = OfferRepository(db)
        
    def execute(self, product_id):
            
            offers = self.offer_repository.find_by_product_id(product_id)
            
            return offers