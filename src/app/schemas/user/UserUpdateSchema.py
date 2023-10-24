from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    isUpdated: bool
    phone: str
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
    birthDate: str
    document: str
    nationality: str


class UserUpdateSchema(BaseModel):
    user: User
    address: Address
    identification: Identification
