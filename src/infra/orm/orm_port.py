from .sqlalchemy_adapter import SQLAlchemyAdapter


class ORMPort:
    def __init__(self,adapter) -> None:
        self.adapter=adapter
        
    def connect_to_database(self,user,password,host,port,database):
        self.adapter.connect_to_database(user,password,host,port,database)
    
    def open_session(self):
        return self.adapter.open_session()
    def create_tables(self):
        self.adapter.create_tables()
        
orm = ORMPort(SQLAlchemyAdapter())