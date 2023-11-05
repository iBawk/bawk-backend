from pydantic import BaseModel


class TransactionCreateSchema(BaseModel):
    offer_id: str
    email_buyer: str
    name_buyer: str
    phone_buyer: str
    paymentMethod_id: int
