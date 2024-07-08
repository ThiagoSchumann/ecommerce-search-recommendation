from flask import request
from src.infra.orm.orm_port import orm
from src.domain.entities.product import Product
from sqlalchemy.exc import IntegrityError

class ProductRepository:
    
    @staticmethod
    def create_product(name):
        session = orm.open_session()
        try:
            data = request.get_json()
            name = data.get('name')

            if not name:
                raise Exception('name is required')

            new_product = Product(name=name)
            session.add(new_product)
            session.commit()
            return new_product
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    from sqlalchemy.orm import Session

    @staticmethod
    def get_product(product_id: int):
        session = orm.open_session()
        return session.query(Product).filter(Product.id == product_id).first()
   
    @staticmethod
    def get_products(skip: int = 0, limit: int = 10):
        session = orm.open_session()
        return session.query(Product).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None, quantity: int = None):
        session = orm.open_session()
        db_product = session.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            return None
        if name:
            db_product.name = name
        if description:
            db_product.description = description
        if price:
            db_product.price = price
        if quantity:
            db_product.quantity = quantity
        session.commit()
        session.refresh(db_product)
        return db_product

    @staticmethod
    def delete_product(product_id: int):
        session = orm.open_session()
        db_product = session.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            return None
        session.delete(db_product)
        session.commit()
        return db_product