from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError
from db.models import UserIdentificationModel


class UserIdentificationRespository:
    def __init__(self, db: Session):
        self.db = db

    def create_user_identification(self, identification: UserIdentificationModel):
        print(identification.__dict__)
        try:
            self.db.add(identification)
            self.db.commit()
            self.db.refresh(identification)
            return identification
        except DatabaseError as e:
            raise e
