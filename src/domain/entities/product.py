from src.domain.entities.category import Category
from .base import Base
from sqlalchemy import  Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Double)
    amount = Column(Double)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f'Product(id:{self.id}, name: {self.name}, category_id: {self.category_id}, amount: {self.amount})'

Category.products = relationship("Product", order_by=Product.id, back_populates="category")


