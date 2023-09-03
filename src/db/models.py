from sqlalchemy import Column, String, Integer, Boolean
from db.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    
    id = Column('id', String, primary_key=True, nullable=False)
    email = Column('email', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    emailVerified = Column('emailVerified', Boolean, default=0)