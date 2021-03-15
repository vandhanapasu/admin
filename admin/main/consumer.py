import pika

params = pika.URLParameters('amqps://kjfgcgzo:05xbwRBccXE7KL2FskMW-ljJ5W3V9XAy@orangutan.rmq.cloudamqp.com/kjfgcgzo')
connection = pika.BlockingConnection(params)
channel = connection.channel()

#declare quueue
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received message in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started Consuming on main....')
channel.start_consuming()
channel.close()