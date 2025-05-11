<svelte:head>
	<title>Information Exchange</title>
</svelte:head>

# Information Exchange

### **Bài 1(Báo cáo):** Tìm hiểu dịch vụ truyền thông điệp – RabbitMQ, Kafka, ActiveMQ, Redis Pub/Sub, Google Pub/Sub

### 1. Giới thiệu

Dịch vụ truyền thông điệp (Message Broker) là một thành phần trung gian giúp gửi và nhận thông điệp giữa các thành phần của hệ thống phân tán. Chúng đóng vai trò quan trọng trong việc đảm bảo khả năng mở rộng, tính linh hoạt và độ tin cậy của hệ thống.

---

### 2. Một số dịch vụ truyền thông điệp phổ biến

#### 2.1 RabbitMQ

- **Cơ chế hoạt động**:  
  Sử dụng giao thức AMQP. Thông điệp được gửi từ Producer vào Queue, và được Consumer lấy ra xử lý.

- **Chức năng**:
  - Hỗ trợ nhiều kiểu trao đổi: direct, fanout, topic, headers.
  - Cơ chế phân phối thông điệp hiệu quả.
  - Hỗ trợ thông điệp bền vững (persistent).
  - Giao diện quản lý trực quan.

- **Ưu điểm**:
  - Dễ triển khai và cấu hình.
  - Phù hợp với hệ thống vừa và nhỏ.

---

#### 2.2 Kafka

- **Cơ chế hoạt động**:  
  Hoạt động theo mô hình Publish-Subscribe. Producer gửi thông điệp vào Topic, Consumer đăng ký để nhận dữ liệu.

- **Chức năng**:
  - Xử lý luồng dữ liệu thời gian thực.
  - Lưu trữ thông điệp trong thời gian dài.
  - Hỗ trợ phân vùng và replication.

- **Ưu điểm**:
  - Rất phù hợp với hệ thống lớn, xử lý dữ liệu Big Data.

---

#### 2.3 ActiveMQ

- **Cơ chế hoạt động**:  
  Hỗ trợ cả Pub/Sub và Queue. Sử dụng giao thức JMS chủ yếu trong Java.

- **Chức năng**:
  - Giao tiếp đồng bộ và không đồng bộ.
  - Hỗ trợ nhiều giao thức: AMQP, MQTT, STOMP.

- **Ưu điểm**:
  - Phù hợp với hệ sinh thái Java.

---

#### 2.4 Redis Pub/Sub

- **Cơ chế hoạt động**:  
  Publisher gửi thông điệp đến một channel, các subscriber đăng ký channel sẽ nhận được thông điệp.

- **Chức năng**:
  - Truyền thông điệp theo thời gian thực.
  - Tốc độ rất nhanh, cấu trúc đơn giản.

- **Nhược điểm**:
  - Không có tính năng lưu trữ/thử lại thông điệp nếu subscriber chưa kết nối.

---

#### 2.5 Google Pub/Sub

- **Cơ chế hoạt động**:  
  Dịch vụ nhắn tin của Google Cloud. Cho phép tích hợp Publisher và Subscriber theo mô hình Pub/Sub.

- **Chức năng**:
  - Khả năng mở rộng lớn.
  - Tích hợp tốt với hệ sinh thái Google Cloud.
  - Hỗ trợ kiểm soát độ trễ và phân phối thông điệp bảo mật.

- **Ưu điểm**:
  - Sử dụng đơn giản, hiệu suất cao trên quy mô lớn.
  - Quản lý và giám sát qua Google Cloud Console.

---

### 3. Tiêu chí so sánh

| Tiêu chí             | RabbitMQ           | Kafka              | ActiveMQ          | Redis Pub/Sub     | Google Pub/Sub        |
|----------------------|--------------------|---------------------|-------------------|-------------------|------------------------|
| Mô hình              | Queue              | Pub/Sub             | Queue/PubSub      | Pub/Sub           | Pub/Sub                |
| Giao thức            | AMQP               | Tùy chỉnh riêng     | JMS, STOMP, AMQP  | Redis             | HTTPS + gRPC           |
| Lưu trữ thông điệp   | Có                 | Có (dài hạn)        | Có                | Không             | Có                     |
| Quản lý dễ dàng      | ✔️                 | Khó hơn             | Trung bình        | Rất dễ            | ✔️ (GCP Console)        |
| Phù hợp hệ thống     | Vừa và nhỏ         | Lớn (Big Data)      | Java-based        | Nhẹ, đơn giản     | Cloud-native           |

---

### 4. Cài đặt RabbitMQ (ví dụ)

#### Bước 1: Cài đặt bằng Docker

```bash
docker run -d --name rabbitmq \
  -p 5672:5672 -p 15672:15672 \
  rabbitmq:management
```

#### Bước 2: Truy cập giao diện quản lý
> Mở trình duyệt:

```bash
http://localhost:15672  
Username: guest  
Password: guest
```

### Bước 3: Gửi và nhận thông điệp
> Sử dụng thư viện pika trong Python:

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

### 5. Kết luận
> Mỗi hệ thống truyền thông điệp có ưu và nhược điểm riêng.
> 
> - RabbitMQ phù hợp với các hệ thống vừa và nhỏ cần độ tin cậy cao.
> 
> - Kafka dành cho hệ thống lớn, xử lý dữ liệu luồng.
> 
> - Redis Pub/Sub đơn giản, dùng cho hệ thống nhẹ.
> 
> - Google Pub/Sub phù hợp khi triển khai hệ thống trên cloud.
> 
> → Việc lựa chọn đúng message broker sẽ giúp hệ thống hoạt động hiệu quả và ổn định hơn.

### 6. Tài liệu tham khảo

- [RabbitMQ](https://www.rabbitmq.com)
- [Kafka](https://kafka.apache.org)
- [ActiveMQ](https://activemq.apache.org)
- [Redis](https://redis.io/docs/interact/pubsub/)
- [GoogleCloud](https://cloud.google.com/pubsub)

### **Bài 2:** Code một hệ thống đơn giản có sử dụng một trong các dịch vụ đó.

### **Bài 3:** Với RPC, ngoài thư viện xmlrpc demo trước. còn các thư viện nào khác. Viết báo cáo tìm hiểu và demo một thư viện có sử dụng định dạng JSON.

### 1. Giới thiệu về RPC

**RPC (Remote Procedure Call)** là phương thức giúp gọi hàm từ xa như thể nó là hàm cục bộ. RPC giúp các hệ thống phân tán giao tiếp với nhau một cách đơn giản và hiệu quả.

Trong các hệ thống hiện đại, ngoài định dạng XML (như `xmlrpc`), nhiều hệ thống chuyển sang sử dụng JSON nhờ tính đơn giản, nhẹ và dễ tích hợp.

---

### 2. Một số thư viện RPC hỗ trợ định dạng JSON

| Tên thư viện       | Mô tả ngắn                                          | Hỗ trợ JSON |
|--------------------|-----------------------------------------------------|-------------|
| **gRPC + JSON Transcoding** | gRPC tốc độ cao, hỗ trợ mapping REST/JSON qua HTTP/1.1 | ✅ Có        |
| **JSON-RPC**       | Giao thức RPC nhẹ, thuần JSON                      | ✅ Có        |
| **Thrift (Apache)**| Đa ngôn ngữ, có thể định cấu hình hỗ trợ JSON      | ✅ Tùy chọn  |
| **FastAPI RPC**    | Giao tiếp RPC JSON qua HTTP trong Python           | ✅ Có        |
| **ZeroRPC**        | Xây dựng trên ZeroMQ, dùng JSON làm định dạng mặc định | ✅ Có    |

Trong số đó, **gRPC với JSON Transcoding** nổi bật nhờ:
- Hiệu suất cao.
- Hỗ trợ HTTP + JSON → dễ tích hợp với frontend, REST API.
- Phù hợp cho cả nội bộ và public API.

---

### 3. Giới thiệu gRPC với JSON Transcoding

- gRPC thông thường sử dụng **Protocol Buffers (Protobuf)** làm định dạng.
- Tuy nhiên, bằng cách dùng **gRPC-Gateway (hoặc transcoding)**, có thể chuyển đổi sang RESTful JSON.

#### Lợi ích:
- Hỗ trợ song song gRPC (hiệu suất cao) và HTTP/JSON (dễ dùng).
- Giảm chi phí duy trì API khác nhau.

---

### 4. Demo đơn giản (Python với gRPC + JSON qua HTTP)

- [Project](https://github.com/Phenikaa-team/DCS/tree/RPC)

---

### 5. Kết luận
- RPC là giải pháp hiệu quả để xây dựng các dịch vụ microservice giao tiếp nhanh chóng.

- Bên cạnh XML-RPC, các thư viện hỗ trợ JSON như gRPC-Gateway, JSON-RPC, Thrift đều phù hợp cho ứng dụng hiện đại.

- gRPC + JSON Transcoding mang lại hiệu suất cao của gRPC và tính dễ sử dụng của RESTful JSON API.

- Có thể sử dụng Envoy hoặc gRPC-Gateway (Go) để triển khai JSON Transcoding cho gRPC.

---

### 6. Tài liệu tham khảo
- [gRPC Official](https://grpc.io/)

- [gRPC Gateway (Go)](https://github.com/grpc-ecosystem/grpc-gateway)

- [Envoy Proxy JSON Transcoding](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/grpc_json_transcoder_filter)

- [JSON-RPC Spec](https://www.jsonrpc.org/specification)