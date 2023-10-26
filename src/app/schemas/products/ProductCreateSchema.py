from fastapi import HTTPException, status
from pydantic import BaseModel, validator

from utils.enum import Situation


class ProductCreateSchema(BaseModel):
    name: str
    description: str
    format: str
    category: str
    markdown: str
    situation: Situation
    format: str
    sallerInName: str
    sallerInEmail: str
    sallerInPhone: str

    @validator('situation')
    def status_must_be_valid(cls, value):
        if value not in Situation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Status inválido. Os status válidos são: '0 - INATIVO', '1 - ATIVO'."
            )
            
        return value

