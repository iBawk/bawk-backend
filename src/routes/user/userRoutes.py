from fastapi import APIRouter

userRoutes = APIRouter()

@userRoutes.post('', summary="Criação de usuario")
def createUser(id: int):
    return {
        "idUsuraio": id
    };
    
@userRoutes.get('/{id}', summary="Busca um usuario através do id")
def getUser(id: int):
    return {
        "idUsuraio": id
    };
    