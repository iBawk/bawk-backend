from pydantic import BaseModel


class WalletAddSchema(BaseModel):
    amount_free: int
