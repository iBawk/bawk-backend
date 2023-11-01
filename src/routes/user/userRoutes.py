import os

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.controllers.userController import UserController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.user.UserFindByIdResponseSchema import \
    UserFindByIdResponseSchema
from app.schemas.user.UserLoginResponseSchema import LoginResponse
from app.schemas.user.UserLoginSchema import UserLogin
from app.schemas.user.UserRegisterResponseSchema import \
    UserRegisterResponseSchema
from app.schemas.user.UserRegisterSchema import UserRegister
from app.schemas.user.UserUpdateResponseSchema import UserUpdateResponseSchema
from app.schemas.user.UserUpdateSchema import UserUpdateSchema
from db.models import UserModel
from lib.depends import get_db_Session

userRoutes = APIRouter()


@userRoutes.post('', summary="Cadastro de usuario.", response_model=UserRegisterResponseSchema)
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
                summary="Verifica validade do refresh token.", response_model=LoginResponse)
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


@userRoutes.get('/id={user_id}', summary="Busca usuario pelo id.", response_model=UserFindByIdResponseSchema)
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


@userRoutes.get("/me", summary="Devolve usuário logado através do token.", response_model=UserFindByIdResponseSchema)
def getUserByToken(user: UserModel = Depends(verifyJWT)):
    return user.as_dict()


@userRoutes.put("/update", summary="Atualiza as informações do usuário.", response_model=UserUpdateResponseSchema)
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
    
@userRoutes.post("/image/{user_id}", summary="Upload imagem do produto.")
def upload_user_image(user_id: str, file: UploadFile = File(...)):
    try:
        base_dir = "images/user"
        id_str = str(user_id)
        path_image_dir = os.path.join(base_dir, id_str)
        
        # todo: verificar se o arquivo é uma imagem (png, jpg, jpeg)
        if file.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
            raise Exception("O arquivo deve ser uma imagem.")
        
        #  todo: armazenar a extensão do arquivo
        ext = file.content_type.split("/")[1]
        
        # todo: mudar extensão do arquivo para png
        file.filename = "userPhoto.png"
        
        # todo: verificar se o arquivo é maior que 2mb
        if file.size > 2097152:
            raise Exception("O arquivo deve ser menor que 2mb.")
        
        #  todo: verificar se ja existe uma imagem para o produto e apagar
        if os.path.exists(os.path.join(path_image_dir, "userPhoto.png")):
            os.remove(os.path.join(path_image_dir, "userPhoto.png"))        

        # Crie o diretório e todos os subdiretórios necessários, se não existirem
        os.makedirs(path_image_dir, exist_ok=True)

        full_image_path = os.path.join(path_image_dir, "userPhoto.png")

        with open(full_image_path, "wb+") as f:
            f.write(file.file.read())
            f.flush()

        # Use FileResponse para retornar o arquivo
        return FileResponse(full_image_path, media_type='image/png')
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))




@userRoutes.get("/image/{user_id}", summary="Get imagem do produto.")
def get_user_image(user_id: str):
    try:
        cwd = os.getcwdb()
        base_dir = "images/user/"
        id_str = str(user_id)
        path_image_dir = os.path.join(base_dir, id_str)
        
        if not os.path.exists(os.path.join(path_image_dir, "userPhoto.png")):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
                        
        full_image_path = os.path.join(cwd.decode('utf-8'), path_image_dir, "userPhoto.png")

        return FileResponse(full_image_path, media_type='image/png')
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
