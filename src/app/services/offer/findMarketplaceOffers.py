from app.repositories.offer.offerRepository import OfferRepository


class FindMarketplaceOffers:
    def __init__(self, db):
        self.db = db
        self.offer_repository = OfferRepository(db)
    
    def execute(self, page, take):
        offers = self.offer_repository.findMarketplaceOffers(page, take)
        
        json = {
            "offers": offers,
            "page": page,
            "take": take
        }
        
        return json
        
        
        
        
        
        



        