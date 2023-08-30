from fastapi import APIRouter

userRoutes = APIRouter()

@userRoutes.get('/{id}')
def getUser(id: int):
    return {
        "idUsuraio": id
    };