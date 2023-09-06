from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from decouple import config
from jose import jwt
from lib.depends import get_db_Session
from db.models import  UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verifyJWT(db: Session = Depends(get_db_Session), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config('SECRET_KEY'), algorithms=["HS256"]) 
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        return user
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail="Token expirado") from e
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail="Erro ao decodificar token") from e
