from sqlalchemy import Column, String, Integer, Boolean, LargeBinary, ForeignKey, Text
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

    # Novas colunas
    address_id = Column('address_id', String, ForeignKey('usersAddress.id'))
    identification_id = Column(
        'identification_id', String, ForeignKey('usersIdentifications.id'))

    # Relacionamentos
    address = relationship("UserAddressModel", back_populates="user")
    identification = relationship(
        "UserIdentificationModel", back_populates="user")
    products = relationship("ProductModel", back_populates="user")

    def as_dict(self):
        user_dict = {
            'user': {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'phone': self.phone,
                'photo': self.photo,
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
    __tablename__ = 'usersIdentifications'

    id = Column('id', String, primary_key=True)
    nationality = Column('nationality', String)
    document = Column('document', String)
    birthDate = Column('birthDate', String)

    # Define o relacionamento com UserModel
    user = relationship("UserModel", back_populates="identification")


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column('id', String, primary_key=True, nullable=False)
    owner_id = Column('owner_id', String, ForeignKey(
        'users.id'), nullable=False)
    name = Column('name', String, nullable=False)
    description = Column('description', String, nullable=False)
    createDate = Column('createDate', String, nullable=False)
    format = Column('format', String, nullable=False)
    status = Column('status', String, nullable=False)
    markdown = Column('markdown', Text, nullable=False)

    category_id = Column('category_id', Integer, ForeignKey('categories.id'))

    # Define o relacionamento com UserModel
    user = relationship("UserModel", back_populates="products")
    category = relationship("CategoryModel", back_populates="products")


class CategoryModel(Base):
    __tablename__ = 'categories'

    id = Column('id', String, primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)

    # Define o relacionamento com UserModel
    products = relationship("ProductModel", back_populates="category")
