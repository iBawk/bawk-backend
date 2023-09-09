from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.controllers.userController import UserController
from app.schemas.userRegisterSchema import UserRegister
from app.schemas.userLoginSchema import UserLogin
from app.schemas.LoginResponseSchema import LoginResponse
from lib.depends import get_db_Session

userRoutes = APIRouter()


@userRoutes.post('/register', summary="Cadastro de usuario.")
def createUser(credentials: UserRegister, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)

    try:
        return user_controller.register_user(credentials)
    except ConnectionAbortedError as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e
        )


@userRoutes.get('/login', summary="Realiza login", response_model=LoginResponse)
def login(credentials: UserLogin, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)

    try:
        return user_controller.login(credentials)
    except ConnectionAbortedError as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )


@userRoutes.get('/refresh-token/{refresh_token}',
                summary="Verifica validade do refresh token")
def refresh_access_token(refresh_token: str, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)

    try:
        return user_controller.refresh_token(refresh_token)
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )


@userRoutes.get('/{id}', summary="Busca usuario pelo id")
def getUserByID(id: str, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)

    try:
        return user_controller.get_by_id_user_service_v1.execute(id)
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )
