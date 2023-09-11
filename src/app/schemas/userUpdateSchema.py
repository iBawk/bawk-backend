from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    name: str
    email: str
    isUpdated: bool
    phone: str
    photo: str
    emailVerified: bool


class Address(BaseModel):
    country: str
    zipCode: str
    complement: str
    state: str
    street: str
    number: str
    city: str


class Identification(BaseModel):
    birthDate: date
    document: str
    nationality: str


class UserUpdateSchema(BaseModel):
    user: User
    address: Address
    identification: Identification
