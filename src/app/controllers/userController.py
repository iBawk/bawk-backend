from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.schemas.userUpdateSchema import UserUpdateSchema
from app.services.auth.authenticateUser import authenticateUserServiceV1
from app.services.auth.verifyRefreshToken import verifyRefreshTokenServiceV1
from app.services.user.createUser import createUserServiceV1
from app.services.user.getByIdUser import getByIdUserServiceV1
from app.services.user.updateUser import UpdateUserServiceV1

app = FastAPI()


class UserController:
    def __init__(self, db: Session):
        self.create_user_service_v1 = createUserServiceV1(db)
        self.authenticate_user_service_v1 = authenticateUserServiceV1(db)
        self.verify_refresh_token_service_v1 = verifyRefreshTokenServiceV1(db)
        self.get_by_id_user_service_v1 = getByIdUserServiceV1(db)
        self.update_user_service_v1 = UpdateUserServiceV1(db)

    def register_user(self, credentials):
        try:
            return self.create_user_service_v1.execute(credentials)
        except Exception as e:
            print(e)
            raise e

    def login(self, credentials):
        try:
            return self.authenticate_user_service_v1.execute(credentials)
        except Exception as e:
            print(e)
            raise e

    def refresh_token(self, token):
        try:
            return self.verify_refresh_token_service_v1.execute(token)
        except Exception as e:
            print(e)
            raise e

    def get_by_id(self, id):
        try:
            return self.get_by_id_user_service_v1.execute(id)
        except Exception as e:
            print(e)
            raise e

    def update_user(self, id, data: UserUpdateSchema):
        try:
            return self.update_user_service_v1.execute(id, data)
        except Exception as e:
            raise e
