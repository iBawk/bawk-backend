from fastapi import HTTPException, status
from pydantic import BaseModel, validator

from utils.enum import ProductStatus


class Product(BaseModel):
    name: str
    description: str
    format: str
    category: str
    markdown: str
    status: ProductStatus
    format: str
    sallerInName: str
    sallerInEmail: str
    sallerInPhone: str

    @validator('status')
    def status_must_be_valid(cls, value):
        if value not in ProductStatus:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Status inválido. Os status válidos são: '0 - INATIVO', '1 - ATIVO'."
            )
