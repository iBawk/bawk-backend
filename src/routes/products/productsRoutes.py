from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session

from app.controllers.productController import productController
from app.middlewares.verifyJWT import verifyJWT
from app.schemas.productSchema import Product
from db.models import UserModel
from lib.depends import get_db_Session
import os
from PIL import Image

productRoutes = APIRouter()


@productRoutes.post("", summary="Cria um produto.")
def create(
    product: Product,
    user: UserModel = Depends(verifyJWT),
    db: Session = Depends(get_db_Session),
):
    product_controller = productController(db)

    try:
        return product_controller.createProduct(product, user)
    except Exception as e:
        print(e)
        return e


@productRoutes.get("/{id}", summary="Busca um produto pelo id.")
def getById(
    id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)
):
    product_controller = productController(db)

    try:
        return product_controller.findProductById(id)
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


@productRoutes.put("/update/{id}", summary="Atualiza informações do produto")
def update(
    id: str,
    data: Product,
    user: UserModel = Depends(verifyJWT),
    db: Session = Depends(get_db_Session),
):
    product_controller = productController(db)

    try:
        return product_controller.update(id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@productRoutes.delete("", summary="Delete um produto.")
def delete(
    id: str, user: UserModel = Depends(verifyJWT), db: Session = Depends(get_db_Session)
):
    product_controller = productController(db, user)

    try:
        return product_controller.deleteProduct(id)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@productRoutes.post("/upload-image/{id}", summary="Upload imagem do produto.")
def upload_product_image(id: str, file: UploadFile = File(...)):
    try:
        cwd = os.getcwdb()
        path_image_dir = "upload-images/product/image" + id + "/"
        full_image_path = os.path.join(cwd, path_image_dir, file.filename)

        if not os.path.exists(path_image_dir):
            os.mkdir(path_image_dir)

        file_name = full_image_path.replace(file.filename, "product.png")

        with open(file_name, "wb+") as f:
            f.write(file.file.read())
            f.flush()
            f.close()

        return {"product_image": os.path.join(path_image_dir, "product.png")}
    except Exception as e:
        print(e)


@productRoutes.get("/upload-image/{id}", summary="Get imagem do produto.")
def get_product_image(id: str):
    try:
        cwd = os.getcwdb()
        path_image_dir = "upload-images/product/image" + id + "/"
        full_image_path = os.path.join(cwd, path_image_dir, "product.png")

        if os.path.exists(full_image_path):
            image = Image.open(full_image_path)
            image.thumbnail((400, 400), Image.ANTIALIAS)

        return {"product_image": os.path.join(path_image_dir, "product_400x400.png")}
    except Exception as e:
        print(e)
