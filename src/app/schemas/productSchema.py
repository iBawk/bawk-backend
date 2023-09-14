from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    format: str
    category: str
    markdown: str
