from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.schemas.user.UserUpdateSchema import UserUpdateSchema
from app.services.auth.authenticateUser import AuthenticateUserService
from app.services.auth.verifyRefreshToken import VerifyRefreshTokenService
from app.services.user.createUser import CreateUserServiceV1
from app.services.user.findByIdUser import FindByIdUserService
from app.services.user.updateUser import UpdateUserService

app = FastAPI()


class UserController:
    def __init__(self, db: Session):
        self.create_user_service = CreateUserServiceV1(db)
        self.authenticate_user_service = AuthenticateUserService(db)
        self.verify_refresh_token_service = VerifyRefreshTokenService(db)
        self.find_by_id_user_service = FindByIdUserService(db)
        self.update_user_service = UpdateUserService(db)

    def register_user(self, credentials):
        try:
            return self.create_user_service.execute(credentials)
        except Exception as e:
            print(e)
            raise e

    def login(self, credentials):
        try:
            return self.authenticate_user_service.execute(credentials)
        except Exception as e:
            print(e)
            raise e

    def refresh_token(self, token):
        try:
            return self.verify_refresh_token_service.execute(token)
        except Exception as e:
            print(e)
            raise e

    def find_by_id(self, user_id: str):
        try:
            return self.find_by_id_user_service.execute(user_id)
        except Exception as e:
            print(e)
            raise e

    def update_user(self, user_id: str, data: UserUpdateSchema):
        try:
            return self.update_user_service.execute(user_id, data)
        except Exception as e:
            raise e
        
    def get_user_image(self, user_id):
        try:
            return self.find_by_id_user_service.get_user_image(user_id)
        except Exception as e:
            raise e
