from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from db.models import UserModel
from db.models import WalletsModel


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wallet_user(self, wallet: WalletsModel):
        try:
            self.db.add(wallet)
            self.db.commit()
            self.db.refresh(wallet)
            return wallet
        except DatabaseError as e:
            print(e)
            raise e

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
            user = (
                self.db.query(UserModel)
                .filter(UserModel.email == emailToSearch)
                .first()
            )
            return user
        except DatabaseError as e:
            print(e)
            raise e

    def get_user_by_id(self, user_id: str):
        try:
            user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
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

    def get_user_image_profile(self, user_id: str):
        try:
            user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
            return user.photo
        except DatabaseError as e:
            print(e)
            raise (e)

    def get_wallet_by_user_id(self, user_id: str):
        try:
            wallet = (
                self.db.query(WalletsModel)
                .filter(WalletsModel.user_id == user_id)
                .first()
            )
            return wallet
        except DatabaseError as e:
            print(e)
            raise (e)
