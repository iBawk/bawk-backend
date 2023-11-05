from pydantic import BaseModel

from utils.enum import PaymentMethod


class TransactionCreateSchema(BaseModel):
    offer_id: str
    email_buyer: str
    name_buyer: str
    phone_buyer: str
    paymentMethod_id: PaymentMethod
