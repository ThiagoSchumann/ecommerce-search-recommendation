from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.domain.entities.base import Base

class SQLAlchemyAdapter:
    def __init__(self):
        self.engine = None

    def connect_to_database(self, user, password, host, port, database):
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

    def open_session(self,expire_on_commit=False):
        Session = scoped_session(sessionmaker(bind=self.engine,expire_on_commit=expire_on_commit))
        return Session()

    def create_tables(self):
        if not self.engine:
            raise Exception("Database connection is not established.")
        Base.metadata.create_all(self.engine)
