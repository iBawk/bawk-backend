from app.repositories.offer.offerRepository import OfferRepository
from app.repositories.products.productRepository import ProductRepository
from utils.pageNumberCalc import calculate_number_of_pages


class FindMarketplaceOffers:
    def __init__(self, db):
        self.db = db
        self.offer_repository = OfferRepository(db)
        self.product_repository = ProductRepository(db)
    
    def execute(self, page, take):
        offers = self.offer_repository.findMarketplaceOffers(page, take)
        
        for offer in offers:
            product = self.product_repository.find_by_id(offer.product_id)
            offer.product = product
            
        offersCount = self.offer_repository.countMarketplaceOffers()
        
        pageCount = calculate_number_of_pages(offersCount, take)
        
        json = {
            "offers": offers,
            "take": take,
            "page": page,
            "pageCount": pageCount
        }
        
        return json
        
        
        
        
        
        



        