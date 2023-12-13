from app.repositories.offer.offerRepository import OfferRepository
from app.repositories.products.productRepository import ProductRepository
from utils.pageNumberCalc import calculate_number_of_pages


class FindMarketplaceOffers:
    def __init__(self, db):
        self.db = db
        self.offer_repository = OfferRepository(db)
        self.product_repository = ProductRepository(db)
    
    def execute(self, page, take, search, category):
        
        if search == '':
            search = None
        if category == '' or category == 'Todos':
            category = None
        
        elif search and category:
            print("Entrou no elif de search e categoria")
            
            offers = self.offer_repository.findMarketplaceOffersWithSearchAndCategory(page, take, search, category)
            offersCount = self.offer_repository.countMarketplaceOffersWithSearchAndCategory(search, category)
            
            # Lista para armazenar todas as ofertas
            all_offers = []

            for offer, product in offers:
                new_offer = offer.__dict__
                new_offer["product"] = product.__dict__

                # Adiciona a oferta atual à lista
                all_offers.append(new_offer)
        if search and not category:
            print("Entrou no elif de apenas serach")
            offers = self.offer_repository.findMarketplaceOffersWithSearch(page, take, search)
            offersCount = self.offer_repository.countMarketplaceOffersWithSearch(search)
            
                    # Lista para armazenar todas as ofertas
            all_offers = []

            for offer, product in offers:
                new_offer = offer.__dict__
                new_offer["product"] = product.__dict__

                # Adiciona a oferta atual à lista
                all_offers.append(new_offer)
        elif not search and category:
            print("Entrou no elif de apenas categoria")
            offers = self.offer_repository.findMarketplaceOffersWithCategory(page, take, category)
            offersCount = self.offer_repository.countMarketplaceOffersWithCategory(category)
            
            # Lista para armazenar todas as ofertas
            all_offers = []

            for offer, product in offers:
                new_offer = offer.__dict__
                new_offer["product"] = product.__dict__

                # Adiciona a oferta atual à lista
                all_offers.append(new_offer)
        elif not search and not category:    
            print("Entrou no elif de nada")
            offers = self.offer_repository.findMarketplaceOffers(page, take)
            offersCount = self.offer_repository.countMarketplaceOffers()
            
            for offer in offers:
                product = self.product_repository.find_by_id(offer.product_id)
                offer.product = product
            
            all_offers = offers
        

        pageCount = calculate_number_of_pages(offersCount, take)

        json_data = {
        "offers": all_offers,
        "take": take,
        "page": page,
        "pageCount": pageCount
        }

        return json_data
        
        
        
        
        
        



        