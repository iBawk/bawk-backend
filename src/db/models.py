from sqlalchemy import Column, String, Integer, Boolean, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

try:
    from db.base import Base
except ImportError:
    from src.db.base import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column('id', String, primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)
    email = Column('email', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    phone = Column('phone', String, default='')
    photo = Column('photo', LargeBinary, nullable=True)
    isUpdated = Column('isUpdated', Boolean, default=0)
    emailVerified = Column('emailVerified', Boolean, default=0)

    # Relacionamentos
    address = relationship(
        "UserAddressModel", back_populates="user", uselist=False)
    identification = relationship(
        "UserIdentificationModel", back_populates="user", uselist=False)


class UserAddressModel(Base):
    __tablename__ = 'userAddress'

    id = Column('id', String, primary_key=True, nullable=False)
    user_id = Column('user_id', String, ForeignKey('users.id'), unique=True)
    country = Column('country', String)
    zipCode = Column('zipCode', String)
    street = Column('street', String)
    number = Column('number', Integer)
    complement = Column('complement', String)
    city = Column('city', String)
    state = Column('state', String)

    # Define o relacionamento com UserModel
    user = relationship("UserModel", back_populates="address")


class UserIdentificationModel(Base):
    __tablename__ = 'UserIdentification'

    id = Column('id', String, primary_key=True)
    user_id = Column('user_id', String, ForeignKey('users.id'), unique=True)
    nacionality = Column('nacionality', String)
    document = Column('document', String)
    birthDate = Column('birthDate', String)

    # Define o relacionamento com UserModel
    user = relationship("UserModel", back_populates="identification")
