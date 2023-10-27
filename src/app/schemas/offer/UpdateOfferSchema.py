from pydantic import BaseModel

from utils.enum import Situation


class UpdateOfferSchema(BaseModel):
    marketplace: bool
    situation: Situation
        
        
