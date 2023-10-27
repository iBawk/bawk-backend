from pydantic import BaseModel

from utils.enum import Situation


class CreateOfferSchema(BaseModel):
    price: float
    marketplace: bool
    situation: Situation
    product_id: str
        
        
