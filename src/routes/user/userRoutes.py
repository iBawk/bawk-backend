from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.controllers.userController import UserController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.user.UserLoginResponseSchema import LoginResponse
from app.schemas.user.UserLoginSchema import UserLogin
from app.schemas.user.UserRegisterResponseSchema import \
    UserRegisterResponseSchema
from app.schemas.user.UserRegisterSchema import UserRegister
from app.schemas.user.UserUpdateSchema import UserUpdateSchema
from db.models import UserModel
from lib.depends import get_db_Session

userRoutes = APIRouter()


@userRoutes.post('', summary="Cadastro de usuario.")
def createUser(credentials: UserRegister, db: Session = Depends(get_db_Session)):
    user_controller = UserController(db)

    try:
        return user_controller.register_user(credentials)
    except ConnectionAbortedError as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )


@userRoutes.post('/login', summary="Realiza login.", response_model=LoginResponse)
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


@userRoutes.get('/refresh-token',
                summary="Verifica validade do refresh token.")
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


@userRoutes.get('/id={id}', summary="Busca usuario pelo id.")
def getUserByID(user_id: str, db: Session = Depends(get_db_Session), user: UserModel = Depends(verifyJWT)):
    user_controller = UserController(db)

    try:
        return user_controller.find_by_id(user_id)
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )


@userRoutes.get("/me", summary="Devolve usuário logado através do token.")
def getUserByToken(user: UserModel = Depends(verifyJWT)):
    return {'loggedUserInfo': user.as_dict()}


@userRoutes.put("/update", summary="Atualiza as informações do usuário.")
def updateUser(
        data: UserUpdateSchema,
        db: Session = Depends(get_db_Session),
        user: UserModel = Depends(verifyJWT)
):
    user_controller = UserController(db)

    try:
        return user_controller.update_user(user.id, data)
    except Exception as e:
        return e