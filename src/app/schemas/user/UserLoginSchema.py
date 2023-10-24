import re

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class UserLogin(BaseModel):
    email: str
    password: str

    @validator('email')
    def validate_email(cls, value):
        if not value:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email não especificado")

        if not re.match(
            '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
                value):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email inválido.")

        return value
