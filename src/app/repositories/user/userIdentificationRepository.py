from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError
from db.models import UserIdentificationModel


class UserIdentificationRespository:
    def __init__(self, db: Session):
        self.db = db

    def create_user_identification(self, identification: UserIdentificationModel):
        try:
            self.db.add(identification)
            self.db.commit()
            self.db.refresh(identification)
            return identification
        except DatabaseError as e:
            raise e

    def get_by_id_identification(self, idToSearch: str):
        try:
            return self.db.query(UserIdentificationModel).filter_by(id=idToSearch).first()
        except DatabaseError as e:
            print(e)
            raise e

    def update_ident(self, identification: UserIdentificationModel):
        try:
            self.db.add(identification)
            self.db.commit()
            self.db.refresh(identification)
            return identification
        except DatabaseError as e:
            raise e
