import os
from src.infra.message_broker.rabbitmq.rabbitmq_adapter import RabbitMqAdapter


class MessageBrokerPort:
    def __init__(self,interface) -> None:
        self.interface=interface

    def connect(self,username,password):
        self.interface.connect(username,password)
    
    def queue_declare(self,queue_name):
        self.interface.queue_declare(queue_name)
        
    def basic_publish(self,queue_name,body,exchange=''):
        self.interface.basic_publish(queue_name=queue_name,body=body,exchange=exchange)


message_broker = MessageBrokerPort(RabbitMqAdapter())
