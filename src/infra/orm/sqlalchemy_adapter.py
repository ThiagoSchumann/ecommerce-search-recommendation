from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from src.domain.entities.base import Base
class SQLAlchemyAdapter:
    engine = None
    
    def connect_to_database(self,user,password,host,database):
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}')
    
    def open_session(self):
        session_factory = sessionmaker(bind=self.engine)
        Session = scoped_session(session_factory)
        return Session()
    
    def create_tables(self):
        Base.metadata.create_all(self.engine)