from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.middlewares.verifyJWT import verifyJWT
from app.controllers.walletsController import walletsController
from db.models import UserModel
from lib.depends import get_db_Session

walletsRoutes = APIRouter()


@walletsRoutes.get("", summary="Busca todos os valores na carteira do usuario logado.")
def getAll(user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    wallet_controller = walletsController(db)

    try:
        return wallet_controller.findAllValues(user)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
