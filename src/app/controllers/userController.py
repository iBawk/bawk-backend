from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from db.models import UserModel
from app.repositories.userRepository import UserRepository
from app.services.userService import UserService
import uuid

app = FastAPI()


class UserController:
    def __init__(self, db: Session):
        self.user_service = UserService(db)
        
    def register_user(self, email: str, password: str):
        try:
            return self.user_service.create_user(email=email, password=password)
        except Exception as e:
            print(e)
            return e
            
    def login(email: str, password: str):
        return ""
