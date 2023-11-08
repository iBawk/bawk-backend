from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user.userAddressRepository import UserAddressRepository
from app.repositories.user.userIdentificationRepository import (
    UserIdentificationRespository,
)
from app.repositories.user.userRepository import UserRepository
from app.schemas.user.UserUpdateSchema import UserUpdateSchema


class UpdateUserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
        self.address_repository = UserAddressRepository(db)
        self.ident_repository = UserIdentificationRespository(db)

    def execute(self, user_id: str, data: UserUpdateSchema):
        if not id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Id do usuario não especificado.",
            )

        user_on_db = self.user_repository.get_user_by_id(user_id)

        if not user_on_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuario não encontrado.",
            )

        user_address_on_db = self.address_repository.find_by_id_address(
            idToSearch=user_on_db.address_id
        )

        user_identification_on_db = self.ident_repository.find_by_id_identification(
            idToSearch=user_on_db.identification_id
        )

        if data.user.email != user_on_db.email:
            if self.user_repository.get_user_by_email(data.user.email):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email já utilizado.",
                )
            user_on_db.email = data.user.email

        user_on_db.name = data.user.name
        user_on_db.isUpdated = data.user.isUpdated
        user_on_db.phone = data.user.phone
        user_on_db.emailVerified = data.user.emailVerified

        user_address_on_db.country = data.address.country
        user_address_on_db.zipCode = data.address.zipCode
        user_address_on_db.complement = data.address.complement
        user_address_on_db.state = data.address.state
        user_address_on_db.street = data.address.street
        user_address_on_db.number = data.address.number
        user_address_on_db.city = data.address.city
        user_address_on_db.district = data.address.district

        user_identification_on_db.birthDate = data.identification.birthDate
        user_identification_on_db.document = data.identification.document
        user_identification_on_db.nationality = data.identification.nationality
        user_identification_on_db.language = data.identification.language

        try:
            self.user_repository.update_user(user_on_db)
            self.address_repository.update_address(user_address_on_db)
            self.ident_repository.update_ident(user_identification_on_db)

            return user_on_db.as_dict()
        except Exception as e:
            raise e
