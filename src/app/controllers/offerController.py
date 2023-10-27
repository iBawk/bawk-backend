from sqlalchemy.orm import Session

from app.services.offer.createOffer import CreateOfferService
from app.services.offer.getByIdOffer import GetOfferByIdService
from app.services.offer.updateOffer import UpdateOfferService


class offerController:
    def __init__(self, db=Session):
        self.db = db
        self.create_offer_service = CreateOfferService(db)
        self.get_by_id_offer_service = GetOfferByIdService(db)
        self.update_offer_service = UpdateOfferService(db)
        
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