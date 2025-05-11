<svelte:head>
	<title>Information Exchange</title>
</svelte:head>

# Báo cáo Hàng đợi – RPC – JSON

## Bài 1: Cài đặt RabbitMQ

### Cách cài trên máy cá nhân (Windows/macOS/Linux)

#### Bước 1: Dùng Docker (dễ nhất)

```bash
docker run -d --hostname rabbit-host --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

- Cổng `5672`: giao tiếp giữa các service
- Cổng `15672`: giao diện quản lý web

#### Bước 2: Truy cập giao diện quản lý

Mở trình duyệt và truy cập địa chỉ:

```
http://localhost:15672
```

Thông tin đăng nhập mặc định:

- **Username**: `guest`
- **Password**: `guest`

---

#### Bước 3: Gửi và nhận thông điệp (Python demo)

Cài thư viện pika:

```bash
pip install pika
```

Mã nguồn Python demo gửi thông điệp:

```python
import pika

# Kết nối tới RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Tạo queue
channel.queue_declare(queue='hello')

# Gửi thông điệp
channel.basic_publish(exchange='', routing_key='hello', body='Hello RabbitMQ!')
print("Đã gửi: Hello RabbitMQ!")

connection.close()
```

---

## **Bài 2:** Code một hệ thống đơn giản có sử dụng một trong các dịch vụ đó

> Đã chọn: **RabbitMQ**

**Ý tưởng**: Một hệ thống gửi email giả lập, trong đó một tiến trình gửi yêu cầu gửi email vào hàng đợi, một tiến trình khác xử lý và "gửi" email.

### 1. Cài đặt môi trường

```bash
pip install pika
```

### 2. Producer (Gửi yêu cầu)

```python
# email_producer.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='emails')

for i in range(5):
    message = f'Gửi email đến user{i}@example.com'
    channel.basic_publish(exchange='', routing_key='emails', body=message)
    print('Đã gửi:', message)

connection.close()
```

### 3. Consumer (Xử lý yêu cầu)

```python
# email_consumer.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='emails')

def callback(ch, method, properties, body):
    print("Xử lý:", body.decode())

channel.basic_consume(queue='emails', on_message_callback=callback, auto_ack=True)

print('Đang đợi email...')
channel.start_consuming()
```

---

## **Bài 3:** RPC sử dụng JSON – Tìm hiểu và demo

### 1. Giới thiệu

RPC (Remote Procedure Call) cho phép gọi hàm ở server từ client như gọi hàm cục bộ. Khi dùng định dạng **JSON**, ta có thể xây dựng API RPC dễ hiểu và dễ debug hơn.

---

### 2. Một số thư viện hỗ trợ JSON RPC

| Thư viện             | Hỗ trợ JSON | Ngôn ngữ phổ biến |
|----------------------|--------------|--------------------|
| gRPC + JSON Gateway  | ✅           | Go, Python, Java   |
| JSON-RPC             | ✅           | Python, JavaScript |
| FastAPI RPC          | ✅           | Python             |
| Thrift (Apache)      | ✅ (option)  | Java, C++, Python  |
| ZeroRPC              | ✅           | Python             |

---

### 3. Demo sử dụng gRPC + JSON Transcoding

[Project](https://github.com/Phenikaa-team/DCS/tree/RPC)

---

## **Kết luận**

- RabbitMQ dễ cài đặt, hoạt động ổn định, phù hợp cho hệ thống vừa và nhỏ.
- Với RPC, ta nên sử dụng **gRPC + JSON Transcoding** khi cần hiệu suất cao kèm hỗ trợ RESTful JSON.
- JSON là định dạng phổ biến, dễ tích hợp, rất phù hợp để sử dụng trong môi trường microservices hoặc frontend-backend tách rời.

---

## **Tài liệu tham khảo**

- [RabbitMQ](https://www.rabbitmq.com)
- [gRPC](https://grpc.io/)
- [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway)
- [JSON-RPC](https://www.jsonrpc.org/)
