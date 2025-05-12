<svelte:head>
	<title>Plan</title>
</svelte:head>

## Đề tài đề xuất

**Xây dựng hệ thống xử lý tác vụ bất đồng bộ sử dụng Celery trong ứng dụng web.**

## Mô tả vấn đề

Trong các ứng dụng web hiện nay, có rất nhiều tác vụ tốn thời gian (ví dụ: gửi email, xử lý hình ảnh, tính toán nặng, lấy dữ liệu từ API ngoài...) mà nếu thực thi đồng bộ sẽ làm chậm toàn bộ hệ thống. Do đó, cần có một cơ chế để thực hiện các tác vụ này ở chế độ nền (background), đảm bảo hệ thống chính phản hồi nhanh và ổn định hơn.

Chúng tôi đề xuất sử dụng thư viện **Celery** để giải quyết vấn đề xử lý bất đồng bộ này.

---

# Trả lời các câu hỏi
## 1. Mục đích của thư viện Celery

| **Tiêu chí**       | **Nội dung**                                                                                                                                   |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mục đích**       | - Celery là một distributed task queue giúp xử lý các tác vụ bất đồng bộ hoặc chạy theo lịch trình.<br>- Cho phép "giao việc" cho worker.   |
| **Giải quyết vấn đề** | - Giảm tải cho ứng dụng chính.<br>- Hỗ trợ retry khi tác vụ thất bại.<br>- Quản lý và theo dõi tiến trình công việc dễ dàng.               |
| **Điểm mạnh**      | - Hỗ trợ nhiều backend: RabbitMQ, Redis, Amazon SQS,...<br>- Tích hợp tốt với Django, Flask, FastAPI.<br>- Hỗ trợ lập lịch (scheduling).<br>- Khả năng mở rộng và phân tán cao. |
| **Điểm yếu**       | - Cần cài đặt/cấu hình message broker (Redis, RabbitMQ, ...).<br>- Phức tạp nếu triển khai quy mô lớn.<br>- Xử lý timeout/phục hồi task phức tạp. |


- **So sánh với framework/thư viện khác:**

| Framework/Library | Ưu điểm so với Celery         | Nhược điểm so với Celery         |
|-------------------|-------------------------------|----------------------------------|
| RQ                | Dễ dùng hơn, nhẹ hơn           | Không mạnh và linh hoạt bằng Celery |
| Dramatiq          | Hiệu suất cao, đơn giản hơn     | Ít tài liệu và cộng đồng nhỏ hơn   |
| Huey              | Nhẹ, đơn giản                  | Không hỗ trợ nhiều tính năng nâng cao |
| Sidekiq (Ruby)    | Rất mạnh với Ruby ecosystem    | Không hỗ trợ Python              |

- **Ứng dụng:**
  - Gửi email nền.
  - Xử lý video, hình ảnh nền.
  - Push notification.
  - Update dữ liệu background.
  - Chạy job định kỳ (cron jobs).

## 2. Kế hoạch dự kiến cho bài giữa kỳ

**Đề tài:** Hệ Thống Phân Tán Gửi Email Bất Đồng Bộ với Celery + RabbitMQ

**🎯 Mục tiêu đề tài:**
- Xây dựng một hệ thống gửi email xác nhận tài khoản người dùng bất đồng bộ sử dụng Celery và RabbitMQ, nhằm tối ưu hóa hiệu suất backend, tăng trải nghiệm người dùng và khả năng mở rộng hệ thống.

---

**⚙️ Công nghệ sử dụng:**
- **Backend**: Python Flask hoặc Django
- **Task Queue**: RabbitMQ
- **Worker**: Celery
- **Giám sát**: Flower hoặc Celery Events
- **Database**: PostgreSQL hoặc MySQL (tùy chọn để lưu log email)
- **Email API**: SendGrid, Mailgun, Amazon SES (có thể cấu hình fallback)

---

**🧠 Ý tưởng mở rộng hệ thống:**
1. Gửi nhiều loại email theo sự kiện người dùng
- Xác nhận tài khoản
- Chào mừng sau đăng ký
- Thông báo đổi mật khẩu
- Nhắc nhở hoàn tất hồ sơ
- Email marketing định kỳ

Mỗi loại email là một Celery task riêng biệt, có thể sử dụng task routing để phân chia worker phù hợp.

---

2. Sử dụng Celery Beat để lập lịch gửi email định kỳ
- Gửi email sinh nhật mỗi ngày
- Gửi báo cáo mỗi tuần cho admin
- Gửi nhắc nhở sau 3 ngày đăng ký nhưng chưa kích hoạt

  → Dùng `celery-beat` để định nghĩa lịch lặp lại (giống cron).

---

3. Hệ thống retry và log lỗi gửi email
- Tự động retry khi gửi email thất bại (timeout, sai địa chỉ...)
- Lưu log vào DB: trạng thái gửi, số lần retry, lỗi gặp phải
- Flower dùng để theo dõi và giám sát các task

---

4. Phân phối nhiều worker theo vai trò
- Worker 1: Gửi email ngay lập tức (real-time)
- Worker 2: Gửi email định kỳ (qua Celery Beat)
- Worker 3: Retry các task thất bại

  → Giúp tăng hiệu suất và khả năng mở rộng theo chiều ngang.

--- 

5. Tích hợp gửi email đa kênh (Fallback)
- Nếu API chính (ví dụ: SendGrid) bị lỗi → chuyển sang Mailgun hoặc Amazon SES
- Dùng try-catch logic để chuyển kênh
- Tăng độ tin cậy cho hệ thống gửi email

---

6. API theo dõi trạng thái gửi email
- Xem email đã gửi thành công chưa, lúc nào gửi
- Tạo trang admin hiển thị trạng thái từng email (thành công/thất bại/retry)
- Dễ dàng kiểm tra và hỗ trợ người dùng

---

 7. Hệ thống gửi email hàng loạt (Bulk Email)
- Admin upload danh sách người dùng (CSV)
- Celery task chia nhỏ theo batch để gửi
- Giới hạn tốc độ gửi mỗi phút để tránh spam hoặc bị khóa API

---

# Kết luận

Sinh viên đề xuất đề tài: Hệ thống Celery + RabbitMQ không chỉ dừng lại ở gửi email xác nhận, mà có thể mở rộng thành **nền tảng gửi thông báo email mạnh mẽ, linh hoạt và chịu tải tốt**.

Vấn đề giải quyết: **Tối ưu hóa hiệu suất hệ thống bằng cách xử lý các công việc nặng ở background, tăng trải nghiệm người dùng và khả năng mở rộng của hệ thống.**