from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.offer.offerRepository import OfferRepository
from app.schemas.offer.UpdateOfferSchema import UpdateOfferSchema


class UpdateOfferService:
    def __init__(self, db = Session):
        self.db = db
        self.offer_repository = OfferRepository(db)
        
    def execute(self, offer_id, newOfferData: UpdateOfferSchema):
        
        offer = self.offer_repository.find_by_id(offer_id)
        if not offer:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Oferta não encontrada."
                )
        
        product_offers = self.offer_repository.find_by_product_id(offer.product_id)
        for product_offer in product_offers:
            if product_offer.marketplace is True and newOfferData.marketplace is True and product_offer.id != offer.id:
                self.offer_repository.removeMarketplaceFlag(product_offer.id)
        
        offer.marketplace = newOfferData.marketplace
        offer.situation = newOfferData.situation
        
        return self.offer_repository.update_offer(offer)
        
        