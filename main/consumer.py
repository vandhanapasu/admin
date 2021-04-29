import pika, json
from main import Product, db

params = pika.URLParameters('amqps://kjfgcgzo:05xbwRBccXE7KL2FskMW-ljJ5W3V9XAy@orangutan.rmq.cloudamqp.com/kjfgcgzo')
connection = pika.BlockingConnection(params)
channel = connection.channel()

#declare quueue
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received message in main')
    data= json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product_created')
    
    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('product_updated')
    
    elif properties.content_type == 'product_deleted': 
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product_deleted')



channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started Consuming on main....')
channel.start_consuming()
channel.close()