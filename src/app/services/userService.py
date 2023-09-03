from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models import UserModel
from app.repositories.userRepository import UserRepository
from passlib.context import CryptContext
from lib.depends import get_db_Session
import uuid

class UserService:
    def __init__(self, db: Session = Depends(get_db_Session)):
        self.db = db
        self.user_repository = UserRepository(db)
        self.password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_user(self, email: str, password: str):
        prev_user = self.user_repository.get_user_by_email(email)
        if prev_user:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado.")
        
        hashed_password = self.password_hasher.hash(password)
        userId = str(uuid.uuid4())
                
        try:
            user = UserModel(id=userId, email=email, password=hashed_password)
            return self.user_repository.create_user(user)
        except Exception as e:
            print(e)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and self.password_hasher.verify(password, user.password):
            return user
        return None
