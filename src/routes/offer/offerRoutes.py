from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.offerController import offerController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.offer.CreateOfferSchema import CreateOfferSchema
from app.schemas.offer.UpdateOfferSchema import UpdateOfferSchema
from db.models import UserModel
from lib.depends import get_db_Session

offerRoutes = APIRouter()

@offerRoutes.post("", summary="Cria uma oferta.")
def create(offer: CreateOfferSchema, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    offer_controller = offerController(db)
    
    try:
        return offer_controller.createOffer(offer)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    
    
@offerRoutes.get("/{offer_id}", summary="Busca uma oferta pelo id.")
def getById(offer_id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    offer_controller = offerController(db)
    
    try:
        return offer_controller.getOfferById(offer_id)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    
@offerRoutes.put("/{offer_id}", summary="Atualiza uma oferta pelo id.")
def update(offer_id: str, offer: UpdateOfferSchema, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    offer_controller = offerController(db)
    
    try:
        return offer_controller.updateOffer(offer_id, offer)
    except ConnectionAbortedError as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )
        
@offerRoutes.get("/marketplace", summary="Busca todas as ofertas.")
def marketpalceOffers(user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    offer_controller = offerController(db)
    
    try:
        return offer_controller.marketplaceOffers()
    except ConnectionAbortedError as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )
    
    