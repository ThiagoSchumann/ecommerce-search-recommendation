import os
import logging
from src.infra.message_broker.message_broker_port import message_broker
from src.infra.orm.orm_port import orm
from src.infra.http_server.http_server import HttpServer
from src.infra.dependency_injection import configure_dependencies

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Connecting to message broker")
        message_broker.connect(
            username=os.environ['RABBITMQ_DEFAULT_USER'],
            password=os.environ['RABBITMQ_DEFAULT_PASS']
        )

        logger.info("Connecting to the database")
        orm.connect_to_database(
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT'],
            database=os.environ['DB_NAME'],
        )
        orm.create_tables()

        logger.info("Configuring API documentation adapter")
        api_docs_adapter = configure_dependencies()

        logger.info("Starting HTTP server")
        http_server = HttpServer(api_docs_adapter)
        http_server.run()
    except Exception as e:
        logger.error(f"Error during initialization: {e}", exc_info=True)
        raise

if __name__ == '__main__':
    main()
