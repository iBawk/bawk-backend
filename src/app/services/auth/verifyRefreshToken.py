from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.repositories.user.userRepository import UserRepository
from app.services.auth.tokenService import TokenService
from lib.depends import get_db_Session


class VerifyRefreshTokenService:
    def __init__(self, db: Session = Depends(get_db_Session)):
        self.user_repository = UserRepository(db)
        self.token_service = TokenService()

    def execute(self, refresh_token: str):
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
            'id': user_data.id,
            'name': user_data.name,
            'email': user_data.email,
            'phone': user_data.phone,
            'photo': user_data.photo,
            'isUpdated': user_data.isUpdated,
            'emailVerified': user_data.emailVerified,
            'preferences': {
                'theme': user_data.preferences.theme,
                'windowState': user_data.preferences.windowState,
            }
        }

        payloadRefresh = {
            "id": user_data.id,
        }

        access_token = self.token_service.create_access_token(
            data=payloadAccess)
        refresh_token = self.token_service.create_refresh_token(
            data=payloadRefresh)

        return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}
