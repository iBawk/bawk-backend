from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.services.userService import UserService

app = FastAPI()


class UserController:
    def __init__(self, db: Session):
        self.user_service = UserService(db)

    def register_user(self, credentials):
        try:
            return self.user_service.create_user(credentials)
        except Exception as e:
            print(e)
            raise e

    def login(self, credentials):
        try:
            return self.user_service.authenticate_user(credentials)
        except Exception as e:
            print(e)
            raise e

    def refresh_token(self, token):
        try:
            return self.user_service.verify_refresh_token(token)
        except Exception as e:
            print(e)
            raise e
