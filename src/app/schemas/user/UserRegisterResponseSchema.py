from pydantic import BaseModel


class Address(BaseModel):
    id: str
    zipCode: str
    number: int
    city: str
    street: str
    country: str
    complement: str
    state: str


class Identification(BaseModel):
    id: str
    birthDate: str
    document: str
    nationality: str
    
class User(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    isUpdated: bool
    emailVerified: bool
    address: Address
    identification: Identification


class UserRegisterResponseSchema(BaseModel):
    user: User