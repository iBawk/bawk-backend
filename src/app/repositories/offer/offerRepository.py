from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from db.models import OfferModel, ProductModel


class OfferRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, offer: OfferModel):
        try:
            self.db.add(offer)
            self.db.commit()
            self.db.refresh(offer)
            return offer
        except Exception as e:
            self.db.rollback()
            raise e

    def find_by_id(self, offer_id: str):
        return self.db.query(OfferModel).filter_by(id=offer_id).first()

    def delete(self, offer: OfferModel):
        self.db.delete(offer)
        self.db.commit()
        return offer

    def find_offer_by_product_id(self, product_id: str):
        return self.db.query(OfferModel).filter_by(product_id=product_id).all()

    def update_offer(self, newOffer: OfferModel):
        try:
            self.db.add(newOffer)
            self.db.commit()
            self.db.refresh(newOffer)

            return newOffer
        except DatabaseError as e:
            print(e)
            raise (e)

    def find_by_product_id(self, product_id: str):
        return self.db.query(OfferModel).filter_by(product_id=product_id).all()
    
    def findMarketplaceOffersWithSearchAndCategory(self, page, take, search, category):
        return (
        self.db.query(OfferModel, ProductModel)
        .join(ProductModel, OfferModel.product_id == ProductModel.id)
        .filter(OfferModel.marketplace == 1)
        .filter(ProductModel.name.ilike(f"%{search}%"))
        .filter(ProductModel.category == category)
        .limit(take)
        .offset((page - 1) * take)
        .all()
    )

    def findMarketplaceOffersWithSearch(self, page, take, search):
        return (
            self.db.query(OfferModel, ProductModel)
            .join(ProductModel, OfferModel.product_id == ProductModel.id)
            .filter(OfferModel.marketplace == 1)
            .filter(ProductModel.name.ilike(f"%{search}%"))
            .limit(take)
            .offset((page - 1) * take)
            .all()
        )
        
    def findMarketplaceOffersWithCategory(self, page, take, category):
        return (
            self.db.query(OfferModel, ProductModel)
            .join(ProductModel, OfferModel.product_id == ProductModel.id)
            .filter(OfferModel.marketplace == 1)
            .filter(ProductModel.category == category)
            .limit(take)
            .offset((page - 1) * take)
            .all()
        )
        
    def findMarketplaceOffers(self, page, take):
        return (
            self.db.query(OfferModel)
            .filter(OfferModel.marketplace == 1)
            .limit(take)
            .offset((page - 1) * take)
            .all()
        )
        
    def countMarketplaceOffersWithSearchAndCategory(self, search, category):
        return (
        self.db.query(OfferModel, ProductModel).
        join(ProductModel)
        .filter(OfferModel.marketplace == 1)
        .filter(ProductModel.name.ilike(f"%{search}%"))
        .filter(ProductModel.category == category)
        .count()
    )

    def countMarketplaceOffersWithSearch(self, search):
        return (
            self.db.query(OfferModel, ProductModel).
            join(ProductModel)
            .filter(OfferModel.marketplace == 1)
            .filter(ProductModel.name.ilike(f"%{search}%"))
            .count()
        )
        
    def countMarketplaceOffersWithCategory(self, category):
        return (
        self.db.query(OfferModel, ProductModel).
        join(ProductModel)
        .filter(OfferModel.marketplace == 1)
        .filter(ProductModel.category == category)
        .count()
    )
        
    def countMarketplaceOffers(self):
        return (
            self.db.query(OfferModel)
            .filter(OfferModel.marketplace == 1)
            .count()
        )

    def removeMarketplaceFlag(self, offer_id):
        self.db.query(OfferModel).filter_by(id=offer_id).update(
            {OfferModel.marketplace: 0}
        )

    def find_situation_by_id(self, offer_id: str):
        offer = self.db.query(OfferModel).filter_by(id=offer_id).first()
        if offer:
            return offer.situation
        else:
            return None

    def find_price_by_id(self, offer_id: str):
        offer = self.db.query(OfferModel).filter_by(id=offer_id).first()
        if offer:
            return offer.price
        else:
            return None