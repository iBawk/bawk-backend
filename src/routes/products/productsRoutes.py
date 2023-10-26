import os

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.controllers.productController import productController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.products.ProductCreateSchema import ProductCreateSchema
from db.models import UserModel
from lib.depends import get_db_Session

productRoutes = APIRouter()


@productRoutes.post("", summary="Cria um produto.")
def create(
    product: ProductCreateSchema,
    user: UserModel = Depends(verifyJWT),
    db: Session = Depends(get_db_Session),
):
    product_controller = productController(db)

    try:
        return product_controller.createProduct(product, user)
    except Exception as e:
        print(e)
        return e


@productRoutes.get("/{product_id}", summary="Busca um produto pelo id.")
def getById(
    product_id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)
):
    product_controller = productController(db)

    try:
        return product_controller.findProductById(product_id)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@productRoutes.get("", summary="Busca todos os produtos do usuario logado.")
def getAll(user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)):
    product_controller = productController(db)

    try:
        return product_controller.findAllProductsUser(user)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@productRoutes.put("/update/{product_id}", summary="Atualiza informações do produto")
def update(
    product_id: str,
    data: ProductCreateSchema,
    db: Session = Depends(get_db_Session),
):
    product_controller = productController(db)

    try:
        return product_controller.update(product_id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@productRoutes.delete("/{product_id}", summary="Delete um produto.")
def delete(
    product_id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)
):
    product_controller = productController(db, user)

    try:
        return product_controller.deleteProduct(product_id)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@productRoutes.post("/image/{product_id}", summary="Upload imagem do produto.")
def upload_product_image(product_id: str, file: UploadFile = File(...)):
    try:
        base_dir = "images/product/"
        id_str = str(product_id)
        path_image_dir = os.path.join(base_dir, id_str)
        
        # todo: verificar se o arquivo é uma imagem (png, jpg, jpeg)
        if file.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
            raise Exception("O arquivo deve ser uma imagem.")
        
        #  todo: armazenar a extensão do arquivo
        ext = file.content_type.split("/")[1]
        
        # todo: mudar extensão do arquivo para png
        file.filename = "productPhoto.png"
        
        # todo: verificar se o arquivo é maior que 2mb
        if file.size > 2097152:
            raise Exception("O arquivo deve ser menor que 2mb.")
        
        #  todo: verificar se ja existe uma imagem para o produto e apagar
        if os.path.exists(os.path.join(path_image_dir, "productPhoto.png")):
            os.remove(os.path.join(path_image_dir, "productPhoto.png"))        

        # Crie o diretório e todos os subdiretórios necessários, se não existirem
        os.makedirs(path_image_dir, exist_ok=True)

        full_image_path = os.path.join(path_image_dir, "productPhoto.png")

        with open(full_image_path, "wb+") as f:
            f.write(file.file.read())
            f.flush()

        # Use FileResponse para retornar o arquivo
        return FileResponse(full_image_path, media_type='image/png')
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))




@productRoutes.get("/image/{product_id}", summary="Get imagem do produto.")
def get_product_image(product_id: str):
    try:
        cwd = os.getcwdb()
        base_dir = "images/product/"
        id_str = str(product_id)
        path_image_dir = os.path.join(base_dir, id_str)
        
        if not os.path.exists(os.path.join(path_image_dir, "productPhoto.png")):
            raise Exception("O produto não possui imagem.")
                        
        full_image_path = os.path.join(cwd.decode('utf-8'), path_image_dir, "productPhoto.png")

        return FileResponse(full_image_path, media_type='image/png')
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
