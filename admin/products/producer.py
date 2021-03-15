import pika

params = pika.URLParameters('amqps://kjfgcgzo:05xbwRBccXE7KL2FskMW-ljJ5W3V9XAy@orangutan.rmq.cloudamqp.com/kjfgcgzo')
connection = pika.BlockingConnection(params)
channel = connection.channel()

#publish now
def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello from publish in Products')
