from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user.userRepository import UserRepository


class FindByIdUserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def execute(self, user_id: str):
        try:
            user = self.user_repository.get_user_by_id(user_id)

            if not user:
                return HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail='Usuario não encontrado.')

            return user.as_dict()
        except Exception as e:
            print(e)
            raise (e)
