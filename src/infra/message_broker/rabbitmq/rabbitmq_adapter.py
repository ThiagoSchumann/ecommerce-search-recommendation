import pika
from pika import PlainCredentials

class RabbitMqAdapter:
    def connect(self,username,password):
        credentials = PlainCredentials(username=username,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq',credentials=credentials))
        self.connection = connection.channel()
     
    def queue_declare(self,queue_name):
        self.connection .queue_declare(queue=queue_name)
        
    def basic_publish(self,queue_name,body,exchange=''):
        self.connection.basic_publish(exchange=exchange, routing_key=queue_name, body=body)
    
