from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError
from db.models import UserAddressModel


class UserAddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user_address(self, address: UserAddressModel):
        try:
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address
        except DatabaseError as e:
            print(e)
            raise e
