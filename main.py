from flask import Flask
from pika.credentials import PlainCredentials
import os

app = Flask(__name__)
import pika

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/rabbitmq")
def rabbitmq_connection():
    try:
        username=os.environ['RABBITMQ_DEFAULT_USER']
        password=os.environ['RABBITMQ_DEFAULT_PASS']
        credentials = PlainCredentials(username=username,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq',credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
        return "<p>Rabbitmq is connected</p>"
    except Exception as e:
        return str(e)
