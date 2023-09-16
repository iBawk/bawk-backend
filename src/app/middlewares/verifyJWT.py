from decouple import config
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from db.models import UserModel
from lib.depends import get_db_Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verifyJWT(
    db: Session = Depends(get_db_Session),
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(token, config('SECRET_KEY'), config('ALGORITHM'))
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        return user
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido") from e
    except jwt.JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido") from e
