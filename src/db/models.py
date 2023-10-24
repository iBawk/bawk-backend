from sqlalchemy import (Boolean, Column, ForeignKey, Integer, LargeBinary,
                        String, Text)
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
    isUpdated = Column('isUpdated', Boolean, default=0)
    emailVerified = Column('emailVerified', Boolean, default=0)

    address_id = Column('address_id', String, ForeignKey('usersAddress.id'))
    identification_id = Column(
        'identification_id', String, ForeignKey('usersIdentifications.id'))
    preferences_id = Column(
        'preferences_id', String, ForeignKey('usersPreferences.id'))

    address = relationship("UserAddressModel", back_populates="user")
    identification = relationship(
        "UserIdentificationModel", back_populates="user")
    preferences = relationship(
        "UserPreferencesModel", back_populates="user")
    products = relationship("ProductModel", back_populates="user")

    def as_dict(self):
        user_dict = {
            'user': {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'phone': self.phone,
                'isUpdated': self.isUpdated,
                'emailVerified': self.emailVerified,
            },
            'address': self.address,
            'identification': self.identification
        }

        return user_dict


class UserAddressModel(Base):
    __tablename__ = 'usersAddress'

    id = Column('id', String, primary_key=True, nullable=False)
    country = Column('country', String, default='')
    zipCode = Column('zipCode', String, default='')
    street = Column('street', String, default='')
    number = Column('number', Integer, default=0)
    complement = Column('complement', String, default='')
    city = Column('city', String, default='')
    state = Column('state', String, default='')

    user = relationship("UserModel", back_populates="address")


class UserIdentificationModel(Base):
    __tablename__ = 'usersIdentifications'

    id = Column('id', String, primary_key=True)
    nationality = Column('nationality', String, default='')
    document = Column('document', String, default='')
    birthDate = Column('birthDate', String, default='')

    user = relationship("UserModel", back_populates="identification")


class UserPreferencesModel(Base):
    __tablename__ = 'usersPreferences'

    id = Column('id', String, primary_key=True)
    theme = Column('theme', Integer, default=1)
    windowState = Column('windowState', Integer, default=1)

    user = relationship("UserModel", back_populates="preferences")


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column('id', String, primary_key=True, nullable=False)
    owner_id = Column('owner_id', String, ForeignKey(
        'users.id'), nullable=False)
    name = Column('name', String, nullable=False)
    description = Column('description', String, nullable=False)
    format = Column('format', String, nullable=False)
    status = Column('status', Integer, default=1)
    markdown = Column('markdown', Text, nullable=False)
    created_at = Column('created_at', String, nullable=False)
    # todo: adicionar relacionamento com a tabela de categorias depois
    category = Column('category', String, nullable=False)

    sallerInName = Column('sallerName', String, nullable=False)
    sallerInEmail = Column('sallerEmail', String, nullable=False)
    sallerInPhone = Column('sallerPhone', String, nullable=False)

    # category_id = Column('category_id', Integer, ForeignKey('categories.id'))

    user = relationship("UserModel", back_populates="products")
    # category = relationship("CategoryModel", back_populates="products")


class CategoryModel(Base):
    __tablename__ = 'categories'

    id = Column('id', String, primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)

    # products = relationship("ProductModel", back_populates="category")
