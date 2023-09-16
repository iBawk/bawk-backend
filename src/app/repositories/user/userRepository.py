from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from db.models import UserModel


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserModel):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except DatabaseError as e:
            print(e)
            raise e

    def get_user_by_email(self, emailToSearch: str):
        try:
            user = self.db.query(UserModel).filter(
                UserModel.email == emailToSearch).first()
            return user
        except DatabaseError as e:
            print(e)
            raise e

    def get_user_by_id(self, idSearch: str):
        try:
            user = self.db.query(UserModel).filter(
                UserModel.id == idSearch).first()
            return user
        except DatabaseError as e:
            print(e)
            raise e

    def update_user(self, newUser: UserModel):
        try:
            self.db.add(newUser)
            self.db.commit()
            self.db.refresh(newUser)

            return newUser
        except DatabaseError as e:
            print(e)
            raise (e)
