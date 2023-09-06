import uuid
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models import UserModel
from app.repositories.userRepository import UserRepository
from app.services.tokenService import tokenService
from lib.depends import get_db_Session


class UserService:
    def __init__(self, db: Session = Depends(get_db_Session)):
        self.db = db
        self.user_repository = UserRepository(db)
        self.token_service = tokenService()
        self.password_hasher = CryptContext(
            schemes=["sha256_crypt"], deprecated="auto")

    def create_user(self, credentials):
        prev_user = self.user_repository.get_user_by_email(credentials.email)
        if prev_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado.")

        hashed_password = self.password_hasher.hash(credentials.password)
        userId = str(uuid.uuid4())

        try:
            user = UserModel(id=userId, email=credentials.email,
                             password=hashed_password)
            return self.user_repository.create_user(user)
        except Exception as e:
            print(e)
            raise e

    def authenticate_user(self, credentials):
        user_on_db = self.user_repository.get_user_by_email(credentials.email)
        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "error": "true",
                    "message": "Usuario ou senha incorretos."
                },
            )

        if not self.password_hasher.verify(credentials.password, user_on_db.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "error": "true",
                    "message": "Usuario ou senha incorretos."
                },
            )

        payloadAccess = {
            "id": user_on_db.id,
            "email": user_on_db.email,
            "emailVerified": user_on_db.emailVerified
        }

        payloadRefresh = {
            "id": user_on_db.id,
        }

        access_token = self.token_service.create_access_token(
            data=payloadAccess)
        refresh_token = self.token_service.create_refresh_token(
            data=payloadRefresh)

        return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}

    def verify_refresh_token(self, refresh_token: str):
        try:
            refresh_data = self.token_service.verify_token(refresh_token)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=401, detail="Token de atualização inválido") from e

        if not refresh_data:
            raise HTTPException(
                status_code=401, detail="Token de atualização inválido")

        user_data = self.user_repository.get_user_by_id(refresh_data['id'])

        payloadAccess = {
            "id": user_data.id,
            "email": user_data.email,
            "emailVerified": user_data.emailVerified
        }

        payloadRefresh = {
            "id": user_data.id,
        }

        access_token = self.token_service.create_access_token(
            data=payloadAccess)
        refresh_token = self.token_service.create_refresh_token(
            data=payloadRefresh)

        return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}
