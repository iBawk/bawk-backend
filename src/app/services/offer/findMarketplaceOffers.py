from app.repositories.offer.offerRepository import OfferRepository


class FindMarketplaceOffers:
    def __init__(self, db):
        self.db = db
        self.offer_repository = OfferRepository(db)
    
    def execute(self, page, take):
        try:
            return self.offer_repository.findMarketplaceOffers(page, take)
        except Exception as e:
            print(e)
            raise e


        