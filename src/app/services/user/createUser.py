import uuid
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, status
from db.models import UserModel, UserAddressModel, UserIdentificationModel
from app.repositories.user.userRepository import UserRepository
from app.repositories.user.userAddressRepository import UserAddressRepository
from app.repositories.user.userIdentificationRepository import UserIdentificationRespository


class createUserServiceV1:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
        self.user_address_repository = UserAddressRepository(db)
        self.user_identification_repository = UserIdentificationRespository(db)
        self.password_hasher = CryptContext(
            schemes=["sha256_crypt"], deprecated="auto")

    def execute(self, credentials):
        prev_user = self.user_repository.get_user_by_email(credentials.email)
        if prev_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado.")

        hashed_password = self.password_hasher.hash(credentials.password)

        userId = str(uuid.uuid4())
        userAddreesId = str(uuid.uuid4())
        userIdentificationId = str(uuid.uuid4())

        userIdExistis = self.db.query(UserModel).filter_by(id=userId).first()
        addressIdExistis = self.db.query(
            UserAddressModel).filter_by(id=userId).first()
        identIdExistis = self.db.query(
            UserIdentificationModel).filter_by(id=userId).first()

        if (userIdExistis or addressIdExistis or identIdExistis):
            raise HTTPException(
                "Houve um problema ao criar o usuario, tente novamente mais tarde.")

        try:

            self.user_identification_repository.create_user_identification(
                UserIdentificationModel(
                    id=userIdentificationId,
                )
            )

            self.user_address_repository.create_user_address(
                UserAddressModel(
                    id=userAddreesId,
                )
            )

            new_user = self.user_repository.create_user(
                UserModel(
                    id=userId,
                    name=credentials.name,
                    email=credentials.email,
                    password=hashed_password,
                    address_id=userAddreesId,
                    identification_id=userIdentificationId
                )
            )

            return new_user.as_dict()

        except Exception as e:
            print(e)
            raise e
