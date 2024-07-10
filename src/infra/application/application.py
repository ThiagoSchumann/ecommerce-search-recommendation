import os
from src.infra.message_broker.message_broker_port import  message_broker
from src.infra.orm.orm_port import orm
from src.infra.dependency_injection import configure_dependencies
from src.infra.http_server.http_server import HttpServer
from src.infra.logging.logging_port import logger

class Application:
    def __init__(self) -> None:
        self.setup_message_broker()
        self.setup_orm()
        self.setup_http_server()

    def run_server(self):
        logger.info("Running server")
        self.http_server.run()

    def setup_http_server(self):
        self.http_server = HttpServer(configure_dependencies())
        
    def setup_message_broker(self):
        logger.info("Connecting to message broker")
        message_broker.connect(
                username=os.environ['RABBITMQ_DEFAULT_USER'],
                password=os.environ['RABBITMQ_DEFAULT_PASS']
        )

    def setup_orm(self):
        logger.info("Connecting to the database")
        orm.connect_to_database(
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD'],
                host=os.environ['DB_HOST'],
                port=os.environ['DB_PORT'],
                database=os.environ['DB_NAME'],
            )
        orm.create_tables()
