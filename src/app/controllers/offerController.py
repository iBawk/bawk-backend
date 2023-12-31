from sqlalchemy.orm import Session

from app.services.offer.createOffer import CreateOfferService
from app.services.offer.findMarketplaceOffers import FindMarketplaceOffers
from app.services.offer.getByIdOffer import GetOfferByIdService
from app.services.offer.updateOffer import UpdateOfferService


class offerController:
    def __init__(self, db=Session):
        self.db = db
        self.create_offer_service = CreateOfferService(db)
        self.get_by_id_offer_service = GetOfferByIdService(db)
        self.update_offer_service = UpdateOfferService(db)
        self.find_marketplace_offers = FindMarketplaceOffers(db)
        
    def createOffer(self, offer):
        try:
            return self.create_offer_service.execute(offer)
        except Exception as e:
            print(e)
            raise e
        
    def getOfferById(self, offer_id):
        try:
            return self.get_by_id_offer_service.execute(offer_id)
        except Exception as e:
            print(e)
            raise e
        
    def updateOffer(self, offer_id, offer):
        try:
            return self.update_offer_service.execute(offer_id, offer)
        except Exception as e:
            print(e)
            raise e
        
    def marketplaceOffers(self, page, take, search, category):
        
        try:
            return self.find_marketplace_offers.execute(page, take, search, category)
        except Exception as e:
            print(e)
            raise e