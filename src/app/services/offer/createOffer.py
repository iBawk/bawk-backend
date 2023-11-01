import datetime
import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.offer.offerRepository import OfferRepository
from app.repositories.products.productRepository import ProductRepository
from app.schemas.offer.CreateOfferSchema import CreateOfferSchema
from db.models import OfferModel


class CreateOfferService:
    def __init__(self, db=Session):
        self.db = db
        self.offer_repository = OfferRepository(db)
        self.product_repository = ProductRepository(db)

    def execute(self, offer: CreateOfferSchema):

        offer_id = str(uuid.uuid4())
        id_existis = self.offer_repository.find_by_id(offer_id)
        if id_existis:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Houve um problema ao criar esta oferta, tente novamente mais tarde."
            )
            
        product = self.product_repository.find_by_id(offer.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O produto referente a este id não existe."
            )
            
        product_offers = self.db.query(OfferModel).filter_by(product_id=offer.product_id).all()
        for product_offer in product_offers:
            if product_offer.marketplace is True and offer.marketplace is True:
                self.offer_repository.removeMarketplaceFlag(product_offer.id)
        

        newOffer = self.offer_repository.create(
            OfferModel(
                id=offer_id,
                price=offer.price,
                marketplace=offer.marketplace,
                situation=offer.situation,
                product_id=product.id,
                created_at=datetime.datetime.now()
            )
        )

        return newOffer
