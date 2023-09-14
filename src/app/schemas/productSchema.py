from pydantic import BaseModel

# class ProductModel(Base):
#     __tablename__ = 'products'

#     id = Column('id', String, primary_key=True, nullable=False)
#     name = Column('name', String, nullable=False)
#     description = Column('description', String, nullable=False)
#     createDate = Column('createDate', String, nullable=False)
#     format = Column('format', String, nullable=False)
#     status = Column('status', String, nullable=False)
#     fileDeliverable_id = Column('fileDeliverable_id', Integer, nullable=False)

#     category = Column('category_id', Integer, ForeignKey('categories.id'))

#     # Define o relacionamento com UserModel
#     user = relationship("UserModel", back_populates="products")


class Product(BaseModel):
    name: str
    description: str
    format: str
    category: str
    fileDeliverable_id: int
