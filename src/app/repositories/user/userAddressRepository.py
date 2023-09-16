from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

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

    def find_by_id_address(self, idToSearch: str):
        try:
            return self.db.query(UserAddressModel).filter_by(id=idToSearch).first()
        except DatabaseError as e:
            print(e)
            raise e

    def update_address(self, address: UserAddressModel):
        try:
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address
        except DatabaseError as e:
            raise e
