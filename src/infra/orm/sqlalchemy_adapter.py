from sqlalchemy import create_engine

class SQLAlchemyAdapter:
    def connect_to_database(self,user,password,host,database):
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}')
