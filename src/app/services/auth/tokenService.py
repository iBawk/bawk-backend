from datetime import datetime, timedelta

from decouple import config as env
from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt

SECRET_KEY = env('SECRET_KEY')
ALGORITHM = env('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 50
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 5


class tokenService:

    def create_access_token(self, data: dict):
        to_encode = data
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self, data: dict):
        to_encode = data
        expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            expiration_time = payload.get('exp')
            current_time = datetime.utcnow().timestamp()

            if current_time > expiration_time:
                raise ExpiredSignatureError("Token de atualização expirado")

            return payload
        except ExpiredSignatureError as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "error": True,
                    "message": "Token de atualização expirado"
                }
            ) from e
        except JWTError as e:
            raise JWTError from e
