from pydantic import BaseModel


class Address(BaseModel):
    id: str
    zipCode: str
    number: int
    city: str
    street: str
    country: str
    complement: str
    district: str
    state: str


class Identification(BaseModel):
    id: str
    birthDate: str
    document: str
    nationality: str
    language: str
    
class User(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    isUpdated: bool
    emailVerified: bool
    address: Address
    identification: Identification


class UserFindByIdResponseSchema(BaseModel):
    user: User