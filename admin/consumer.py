import pika

params = pika.URLParameters('amqps://kjfgcgzo:05xbwRBccXE7KL2FskMW-ljJ5W3V9XAy@orangutan.rmq.cloudamqp.com/kjfgcgzo')
connection = pika.BlockingConnection(params)
channel = connection.channel()

#declare quueue
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received message in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print('Started Consuming on admin....')
channel.start_consuming()
channel.close()