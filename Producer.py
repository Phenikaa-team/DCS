import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='emails')

for i in range(5):
    message = f'Gửi email đến user{i}@example.com'
    channel.basic_publish(exchange='', routing_key='emails', body=message)
    print('Đã gửi:', message)

connection.close()