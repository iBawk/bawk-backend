from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.offerController import offerController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.offer.CreateOfferSchema import CreateOfferSchema
from db.models import UserModel
from lib.depends import get_db_Session

offerRoutes = APIRouter()

@offerRoutes.post("", summary="Cria uma oferta.")
def create(offer: CreateOfferSchema, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    offer_Controller = offerController(db)
    
    try:
        return offer_Controller.createOffer(offer)
    except Exception as e:
        return e
    
    
@offerRoutes.get("/{offer_id}", summary="Busca uma oferta pelo id.")
def getById(offer_id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    offer_Controller = offerController(db)
    
    try:
        return offer_Controller.getOfferById(offer_id)
    except Exception as e:
        return e