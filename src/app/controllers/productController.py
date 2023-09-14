from sqlalchemy.orm import Session
from fastapi import Depends


class productController:
    def __init__(self, db=Session):
        self.db = db

    def createProduct(self, product, user):
        pass
