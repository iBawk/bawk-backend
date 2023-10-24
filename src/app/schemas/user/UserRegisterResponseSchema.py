from datetime import date

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    photo: bytes
    isUpdated: bool
    emailVerified: bool


class Address(BaseModel):
    id: str
    zipCode: str
    number: str
    city: str
    street: str
    country: str
    complement: str
    state: str


class Identification(BaseModel):
    id: str
    birthDate: date
    document: str
    nationality: str


class UserRegisterResponseSchema(BaseModel):
    user: User
    address: Address
    identification: Identification