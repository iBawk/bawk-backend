from sqlalchemy import Column, String, Integer, Boolean
from app.db.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, nullable=False)
    email = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    emailVerified = Column('emailVerified', Boolean, default='false')