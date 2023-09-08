import re
from pydantic import BaseModel, validator


class UserRegister(BaseModel):
    name: str
    email: str
    password: str

    @classmethod
    @validator('email')
    def validate_email(cls, value):
        if not value:
            raise ValueError('Email não especificado.')

        if not re.match(
            '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\\.[A-Z|a-z]{2,})+',
                value):
            raise ValueError('Email inválido.')
        return value
