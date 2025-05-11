import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='emails')

def callback(ch, method, properties, body):
    print("Xử lý:", body.decode())

channel.basic_consume(queue='emails', on_message_callback=callback, auto_ack=True)

print('Đang đợi email...')
channel.start_consuming()