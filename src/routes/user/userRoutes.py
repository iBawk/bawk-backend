from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.userController import UserController
from app.schemas.userSchema import User
from lib.depends import get_db_Session

userRoutes = APIRouter()

@userRoutes.post('/register', summary="Cadastro de usuario.")
def createUser(user: User, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)
    
    try:
        print('1')
        return user_controller.register_user(email=user.email, password=user.password)
    except Exception as e:
        return e


@userRoutes.get('/{id}', summary="Busca um usuario através do id")
def getUser(id: int):
    return {
        "idUsuraio": id
    };
    