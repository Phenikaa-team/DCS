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

- **Mục đích:**
  - Celery là một distributed task queue giúp xử lý các tác vụ bất đồng bộ hoặc chạy theo lịch trình.
  - Nó cho phép "giao việc" cho worker xử lý các công việc nặng hoặc tốn thời gian, giúp hệ thống phản hồi nhanh hơn.

- **Giải quyết vấn đề:**
  - Giảm tải cho ứng dụng chính.
  - Hỗ trợ retry khi tác vụ thất bại.
  - Quản lý và theo dõi tiến trình công việc dễ dàng.

- **Điểm mạnh:**
  - Đa backend hỗ trợ (RabbitMQ, Redis, Amazon SQS,...).
  - Tích hợp dễ dàng với Django, Flask, FastAPI.
  - Hỗ trợ scheduling tasks (thực hiện theo lịch).
  - Khả năng mở rộng và phân tán cao.

- **Điểm yếu:**
  - Cần cài đặt và cấu hình môi trường message broker (ví dụ Redis hoặc RabbitMQ).
  - Độ phức tạp cao nếu triển khai trên hệ thống lớn.
  - Xử lý task timeout/phục hồi cần làm thêm nhiều thủ công nếu task phức tạp.

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

**Đề tài:** Xây dựng hệ thống bất đồng bộ gửi email xác thực tài khoản người dùng với Celery + Redis.

**Bài toán:**
- Khi người dùng đăng ký, hệ thống gửi email xác nhận.
- Việc gửi email được chuyển sang worker Celery thực hiện nền để không làm chậm phản hồi.

**Chi tiết:**
- Backend sử dụng Python Flask hoặc Django.
- Task Queue: Redis.
- Celery worker đảm nhiệm gửi email.
- Có dashboard giám sát task (Flower hoặc Celery events).

---

# Kết luận

Sinh viên đề xuất đề tài: **Xây dựng hệ thống bất đồng bộ gửi email xác nhận tài khoản sử dụng Celery**.

Vấn đề giải quyết: **Tối ưu hóa hiệu suất hệ thống bằng cách xử lý các công việc nặng ở background, tăng trải nghiệm người dùng và khả năng mở rộng của hệ thống.**