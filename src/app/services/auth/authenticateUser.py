from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.repositories.user.userRepository import UserRepository
from app.services.auth.tokenService import tokenService


class authenticateUserServiceV1:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        self.token_service = tokenService()
        self.password_hasher = CryptContext(
            schemes=["sha256_crypt"], deprecated="auto")

    def execute(self, credentials):
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
