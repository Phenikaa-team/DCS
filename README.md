# Hệ thống phân tán là gì?
Hệ thống phân tán **(Distributed System)** là tập hợp nhiều máy tính độc lập kết nối với nhau qua mạng, phối hợp hoạt động như một hệ thống thống nhất đối với người dùng cuối. Người dùng không cần biết bên dưới có bao nhiêu máy, chúng được vận hành ra sao – mọi thứ giống như chỉ có một hệ thống duy nhất.

## Các ứng dụng của hệ thống phân tán
 > Dịch vụ đám mây: AWS, Google Cloud, Azure

 > Mạng xã hội: Facebook, Instagram, Twitter

 > Ứng dụng chia sẻ file: Dropbox, Google Drive

 > Hệ thống thương mại điện tử: Shopee, Lazada, Amazon

 > Ứng dụng streaming: Netflix, Spotify, YouTube

 > Blockchain và tiền mã hóa: Bitcoin, Ethereum

## Các khái niệm chính của hệ thống phân tán
**Hệ thống phân tán được xây dựng dựa trên các nguyên lý cốt lõi sau:**

>**Scalability** (Khả năng mở rộng)
>
>**Fault Tolerance** (Khả năng chịu lỗi)
>
>**Availability** (Khả dụng)
>
>**Transparency** (Tính trong suốt)
>
>**Concurrency** (Tính đồng thời)
>
>**Parallelism** (Tính song song)
>
>**Openness** (Tính mở)
>
>**Vertical Scaling** (Mở rộng chiều dọc)
>
>**Horizontal Scaling** (Mở rộng chiều ngang)
>
>**Load Balancer** (Bộ cân bằng tải)
>
>**Replication** (Nhân bản)

## Giải thích các thuật ngữ
- **Scalability** (Khả năng mở rộng)
Khả năng hệ thống xử lý lượng tải ngày càng lớn bằng cách nâng cấp phần cứng hoặc mở rộng số lượng máy chủ.

- **Fault Tolerance** (Khả năng chịu lỗi)
Hệ thống vẫn tiếp tục hoạt động bình thường ngay cả khi một số thành phần bị lỗi.

- **Availability** (Khả dụng)
Khả năng hệ thống sẵn sàng phục vụ người dùng tại mọi thời điểm.

- **Transparency** (Tính trong suốt)
Người dùng không nhận thấy sự phức tạp bên dưới: chẳng hạn như vị trí của tài nguyên, lỗi phần cứng, quá trình nhân bản dữ liệu.

- **Concurrency** (Tính đồng thời)
Khả năng nhiều tiến trình hoặc người dùng truy cập tài nguyên hệ thống cùng lúc mà không gây lỗi.

- **Parallelism** (Tính song song)
Chạy nhiều tác vụ đồng thời để cải thiện tốc độ xử lý, thường tận dụng nhiều CPU hoặc nhiều máy chủ.

- **Openness** (Tính mở)
Hệ thống được xây dựng theo các tiêu chuẩn mở, có thể dễ dàng tích hợp thêm thành phần từ bên ngoài.

- **Vertical Scaling** (Mở rộng chiều dọc)
Nâng cấp phần cứng của một máy chủ hiện có (CPU mạnh hơn, RAM nhiều hơn).

- **Horizontal Scaling** (Mở rộng chiều ngang)
Thêm nhiều máy chủ mới vào hệ thống để chia tải.

- **Load Balancer** (Bộ cân bằng tải)
Phân phối lưu lượng truy cập đồng đều tới các máy chủ để tránh quá tải.

- **Replication** (Nhân bản)
Sao chép dữ liệu hoặc dịch vụ ra nhiều nơi để tăng khả năng chịu lỗi và hiệu suất truy cập.

## Ví dụ minh họa
Ví dụ: Hệ thống Netflix

Netflix sử dụng hệ thống phân tán để truyền tải nội dung video tới hàng triệu người dùng trên toàn cầu.

Scalability: Netflix mở rộng hệ thống để đáp ứng nhu cầu người dùng tăng đột biến, nhất là vào các giờ cao điểm.

Fault Tolerance: Nếu một máy chủ phát video bị hỏng, người dùng tự động được chuyển sang máy chủ khác.

Availability: Người dùng có thể xem phim bất kỳ lúc nào, ở bất kỳ đâu.

Transparency: Người dùng không biết (và không cần biết) nội dung được lưu trữ và truyền tải từ máy chủ nào.

Concurrency: Hàng triệu người dùng có thể cùng xem video cùng lúc.

Parallelism: Các đoạn phim được tải đồng thời từ nhiều nguồn để giảm thời gian buffer.

Openness: Netflix sử dụng tiêu chuẩn HTTP, TCP/IP nên dễ dàng tích hợp với nhiều thiết bị.

Vertical Scaling: Netflix nâng cấp phần cứng của các server trọng yếu tại trung tâm dữ liệu.

Horizontal Scaling: Netflix triển khai thêm nhiều server mới tại nhiều khu vực địa lý.

Load Balancer: Điều phối lượng yêu cầu truy cập đến các server.

Replication: Các video nổi bật được sao chép tới nhiều data center để người dùng có thể truy cập nhanh chóng.

Kiến trúc của hệ thống phân tán
Các mô hình kiến trúc phổ biến:

1. Client-Server Architecture
Máy khách (Client) gửi yêu cầu đến máy chủ (Server) để nhận dữ liệu hoặc dịch vụ.

Ví dụ: Web browser và Web server.

2. Peer-to-Peer (P2P) Architecture
Tất cả các nút vừa là máy khách vừa là máy chủ, chia sẻ tài nguyên lẫn nhau.

Ví dụ: BitTorrent, Blockchain.

3. Multi-Tier Architecture
Chia hệ thống thành nhiều lớp (layer): Presentation, Application, Data.

Ví dụ: Ứng dụng web ba tầng (Frontend - Backend - Database).

4. Microservices Architecture
Ứng dụng được chia nhỏ thành nhiều dịch vụ độc lập, giao tiếp qua API.

Ví dụ: Netflix, Uber.

5. Serverless Architecture
Các nhà phát triển viết hàm (function) và triển khai trực tiếp lên nền tảng đám mây, không cần quản lý server.

Ví dụ: AWS Lambda, Azure Functions.

Ví dụ về kiến trúc hệ thống phân tán
Ví dụ: Hệ thống Shopee

Client-Server: App Shopee (client) giao tiếp với server Shopee.

Multi-Tier: Frontend giao tiếp với backend API, backend API giao tiếp với database.

Microservices: Dịch vụ tìm kiếm, dịch vụ thanh toán, dịch vụ vận chuyển hoạt động độc lập.

Load Balancer: Phân tải truy cập giữa nhiều backend server.

Replication: Dữ liệu đơn hàng được nhân bản giữa các trung tâm dữ liệu để đảm bảo an toàn và nhanh chóng.

Scalability: Vào ngày lễ lớn (11/11, 12/12), hệ thống tự động thêm server để đáp ứng lưu lượng cao.