<svelte:head>
	<title>Distributed Chat System</title>
</svelte:head>

## Đề tài đề xuất

**Xây dựng hệ thống chat phân tán sử dụng Vert.x và RabbitMQ với Kotlin**

## Mô tả vấn đề

Trong các ứng dụng chat hiện đại, yêu cầu về khả năng mở rộng, hiệu suất cao và độ trễ thấp là vô cùng quan trọng. Hệ thống cần phải xử lý được lượng lớn tin nhắn đồng thời trong thời gian thực, đồng thời đảm bảo tính nhất quán dữ liệu giữa các node.

Chúng tôi đề xuất sử dụng **Vert.x** - một framework reactive đa ngôn ngữ, kết hợp với **RabbitMQ** làm message broker và viết bằng **Kotlin** để xây dựng hệ thống chat phân tán hiệu suất cao.

---

# Trả lời các câu hỏi
## 1. Mục đích của kiến trúc đề xuất

| **Tiêu chí**       | **Nội dung**                                                                                                                                   |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mục đích**       | - Xây dựng hệ thống chat phân tán có khả năng mở rộng ngang hàng<br>- Đảm bảo giao tiếp thời gian thực với độ trễ thấp<br>- Xử lý lượng lớn tin nhắn đồng thời |
| **Giải quyết vấn đề** | - Phân tán tải xử lý tin nhắn<br>- Đảm bảo tính sẵn sàng cao<br>- Hỗ trợ phục hồi khi có node gặp sự cố<br>- Quản lý trạng thái người dùng phân tán |
| **Điểm mạnh**      | - Hiệu suất cao nhờ mô hình event-loop của Vert.x<br>- Khả năng mở rộng dễ dàng<br>- Hỗ trợ đa ngôn ngữ (Kotlin/Java)<br>- Tích hợp tốt với RabbitMQ cho message queue |
| **Điểm yếu**       | - Độ phức tạp khi triển khai hệ thống phân tán<br>- Yêu cầu hiểu biết về lập trình reactive<br>- Quản lý trạng thái phân tán phức tạp |

- **So sánh với kiến trúc khác:**

| Framework/Library | Ưu điểm so với Vert.x         | Nhược điểm so với Vert.x         |
|-------------------|-------------------------------|----------------------------------|
| Spring WebFlux    | Tích hợp tốt với Spring ecosystem | Hiệu suất thấp hơn Vert.x        |
| Node.js           | Cộng đồng lớn, nhiều thư viện | Xử lý CPU-intensive kém hơn      |
| Akka              | Mạnh về xử lý phân tán        | Học phí cao, phức tạp            |
| Socket.IO         | Dễ triển khai                 | Khả năng mở rộng hạn chế         |

- **Ứng dụng:**
  - Hệ thống chat thời gian thực
  - Notification service
  - IoT message processing
  - Game server
  - Collaboration tools

## 2. Kế hoạch dự kiến cho bài giữa kỳ

## 🧠 Đề tài đề xuất

**Xây dựng hệ thống chat phân tán sử dụng Vert.x, RabbitMQ và Kotlin**

---

## 📌 Mô tả vấn đề

Các hệ thống chat truyền thống thường gặp phải các vấn đề về:
- Khả năng mở rộng khi số lượng người dùng tăng đột biến
- Độ trễ khi xử lý tin nhắn ở các khu vực địa lý khác nhau
- Khả năng chịu lỗi khi có server gặp sự cố
- Đồng bộ trạng thái người dùng giữa các node

Giải pháp đề xuất là xây dựng hệ thống chat phân tán với các đặc điểm:
- Mỗi node có thể xử lý độc lập một nhóm người dùng
- Các node giao tiếp với nhau thông qua message broker
- Tin nhắn được định tuyến thông minh đến người nhận
- Hỗ trợ phục hồi khi có node gặp sự cố

---

## 🎯 Mục tiêu đề tài

Xây dựng hệ thống chat phân tán sử dụng Vert.x và RabbitMQ:

- Người dùng kết nối đến node gần nhất
- Tin nhắn được đẩy vào hàng đợi RabbitMQ
- Các node xử lý và định tuyến tin nhắn
- Đảm bảo tin nhắn đến đúng người nhận
- Hỗ trợ phòng chat và tin nhắn riêng tư
- Theo dõi trạng thái người dùng

---

## ⚙️ Công nghệ sử dụng

| Thành phần        | Công nghệ đề xuất                                 |
|-------------------|---------------------------------------------------|
| Backend           | Vert.x (Kotlin)                                   |
| Message Broker    | RabbitMQ                                          |
| Protocol          | WebSocket, HTTP/2                                |
| Serialization     | JSON/Protocol Buffers                            |

---

## 🛠️ Ý tưởng mở rộng

### 1. Kiến trúc phân tán
- Tự động cân bằng tải giữa các node
- Service discovery cho các node mới
- Replication dữ liệu giữa các node

### 2. Tính năng chat
- Phòng chat nhóm
- Tin nhắn riêng tư
- Lịch sử tin nhắn
- Thông báo khi online/offline

### 3. Bảo mật
- Xác thực người dùng
- Mã hóa tin nhắn đầu cuối
- Rate limiting
- Bảo vệ DDoS

### 4. Monitoring
- Theo dõi hiệu năng hệ thống
- Cảnh báo khi quá tải
- Log tập trung

### 5. Tối ưu hiệu suất
- Cluster Vert.x
- Tuning RabbitMQ
- Caching thông tin người dùng
- Nén tin nhắn

---

## 🔁 Lưu lượng hệ thống

1. Người dùng kết nối qua WebSocket đến node gần nhất
2. Node xác thực và lưu trạng thái người dùng
3. Khi gửi tin nhắn:
   - Tin nhắn được đẩy vào RabbitMQ
   - Node nhận xử lý và định tuyến
   - Nếu người nhận ở node khác, tin nhắn được chuyển tiếp
4. Đảm bảo thứ tự tin nhắn

---

## 🔒 Bảo mật và hiệu suất

- Xác thực JWT cho mỗi kết nối
- Giới hạn kích thước tin nhắn
- Rate limiting theo người dùng
- Mã hóa kênh truyền TLS
- Giám sát tài nguyên hệ thống

---

## ✅ Kết luận

**Hệ thống Vert.x + RabbitMQ + Kotlin** cung cấp nền tảng lý tưởng cho hệ thống chat phân tán hiệu suất cao, có khả năng mở rộng và chịu lỗi tốt. Kiến trúc reactive giúp xử lý hàng trăm nghìn kết nối đồng thời với tài nguyên tối thiểu.

**Vấn đề giải quyết:** Xây dựng hệ thống chat có khả năng mở rộng ngang hàng, độ trễ thấp, đảm bảo tính sẵn sàng cao và trải nghiệm người dùng mượt mà.