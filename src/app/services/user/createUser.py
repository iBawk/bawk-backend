import uuid

from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.repositories.user.userAddressRepository import UserAddressRepository
from app.repositories.user.userIdentificationRepository import (
    UserIdentificationRespository,
)
from app.repositories.user.userPreferencesRepository import UserPreferencesRepository
from app.repositories.user.userRepository import UserRepository
from db.models import (
    UserAddressModel,
    UserIdentificationModel,
    UserModel,
    UserPreferencesModel,
    WalletsModel,
)


class CreateUserServiceV1:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
        self.user_address_repository = UserAddressRepository(db)
        self.user_identification_repository = UserIdentificationRespository(db)
        self.user_preferences_repository = UserPreferencesRepository(db)
        self.password_hasher = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

    def execute(self, credentials):
        prev_user = self.user_repository.get_user_by_email(credentials.email)
        if prev_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado."
            )

        hashed_password = self.password_hasher.hash(credentials.password)

        walletId = str(uuid.uuid4())
        userId = str(uuid.uuid4())
        userAddreesId = str(uuid.uuid4())
        userIdentificationId = str(uuid.uuid4())
        userPreferencesId = str(uuid.uuid4())

        userIdExistis = self.db.query(UserModel).filter_by(id=userId).first()
        addressIdExistis = (
            self.db.query(UserAddressModel).filter_by(id=userAddreesId).first()
        )
        identIdExistis = (
            self.db.query(UserIdentificationModel)
            .filter_by(id=userIdentificationId)
            .first()
        )
        preferencesIdExistis = (
            self.db.query(UserPreferencesModel).filter_by(id=userPreferencesId).first()
        )

        if userIdExistis or addressIdExistis or identIdExistis or preferencesIdExistis:
            raise HTTPException(
                "Houve um problema ao criar o usuario, tente novamente mais tarde."
            )

        try:
            self.user_preferences_repository.create_user_preferences(
                UserPreferencesModel(
                    id=userPreferencesId,
                )
            )

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
                    identification_id=userIdentificationId,
                    preferences_id=userPreferencesId,
                )
            )

            self.user_repository.create_wallet_user(
                WalletsModel(
                    id=walletId, amount_recluse=0, amount_free=0, user_id=userId
                )
            )

            return new_user.as_dict()

        except Exception as e:
            print(e)
            raise e
