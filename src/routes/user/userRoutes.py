from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.userController import UserController
from app.schemas.userSchema import User
from lib.depends import get_db_Session

userRoutes = APIRouter()

@userRoutes.post('/register', summary="Cadastro de usuario.")
def createUser(credentials: User, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)
    
    try:
        return user_controller.register_user(credentials)
    except Exception as e:
        return e


@userRoutes.get('/login', summary="Realiza login")
def login(credentials: User, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)
    
    try:
        return user_controller.login(credentials)
    except Exception as e:
        print(e)
        return e

@userRoutes.get('/refresh-token/{refresh_token}', summary="Verifica validade do refresh token")
async def refresh_access_token(refresh_token: str, db: Session = Depends(get_db_Session)):    
    user_controller = UserController(db)
    
    try:
        return user_controller.refresh_token(refresh_token)
    except Exception as e:
        print(e)
        return e
    