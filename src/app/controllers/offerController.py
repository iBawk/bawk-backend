from sqlalchemy.orm import Session

from app.services.offer.createOffer import CreateOfferService


class offerController:
    def __init__(self, db=Session):
        self.db = db
        self.create_offer_service = CreateOfferService(db)
        
    def createOffer(self, offer):
        try:
            return self.create_offer_service.execute(offer)
        except Exception as e:
            print(e)
            raise e