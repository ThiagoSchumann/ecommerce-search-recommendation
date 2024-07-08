from .sqlalchemy_adapter import SQLAlchemyAdapter


class ORMPort:
    def __init__(self,adapter) -> None:
        self.adapter=adapter
        
    def connect_to_database(self,user,password,host,database):
        self.adapter.connect_to_database(user,password,host,database)


orm = ORMPort(SQLAlchemyAdapter())