from app.repositories.offerRepository import OfferRepository

class FindMarketplaceOffers:
    def __init__(self, db):
        self.db = db
        self.offer_repository = OfferRepository(db)
    
    def execute()
        

        