from src.infra.orm.orm_port import orm
from src.domain.entities import Category

class CategoryRepository:

    @staticmethod
    def create_category(name):
        session = orm.open_session()
        try:
            if not name:
                raise Exception('Name is required')

            new_category = Category(name=name)
            session.add(new_category)
            session.commit()

            return new_category
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def get_category(category_id: int):
        session = orm.open_session()
        return session.query(Category).filter(Category.id == category_id).first()

    @staticmethod
    def get_categories(skip: int = 0, limit: int = 10):
        session = orm.open_session()
        return session.query(Category).offset(skip).limit(limit).all()

    @staticmethod
    def update_category(category_id: int, name: str = None):
        session = orm.open_session()
        try:
            db_category = session.query(Category).filter(Category.id == category_id).first()
            if not db_category:
                return None
            if name:
                db_category.name = name
            session.commit()
            session.refresh(db_category)
            return db_category
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def delete_category(category_id: int):
        session = orm.open_session()
        try:
            db_category = session.query(Category).filter(Category.id == category_id).first()
            if not db_category:
                return None
            session.delete(db_category)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
