import os
from src.infra.message_broker.message_broker_port import message_broker
from src.infra.orm.orm_port import orm
from src.infra.http_server.http_server import HttpServer

message_broker.connect(username=os.environ['RABBITMQ_DEFAULT_USER'],password=os.environ['RABBITMQ_DEFAULT_PASS'])

orm.connect_to_database(
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_NAME'],
    database=os.environ['DB_PORT'],
)
orm.create_tables()
http_server = HttpServer()
http_server.run()


