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

## 🧠 Đề tài đề xuất

**Xây dựng hệ thống xử lý ảnh/video lớn bất đồng bộ với Celery và RabbitMQ**

---

## 📌 Mô tả vấn đề

Trong các hệ thống web hiện đại, việc xử lý dữ liệu lớn như ảnh độ phân giải cao, video dung lượng lớn, hoặc file nặng thường tốn thời gian và tài nguyên, ảnh hưởng đến trải nghiệm người dùng nếu xử lý đồng bộ.

Ví dụ:
- Nén hoặc resize ảnh sau khi người dùng upload.
- Trích xuất keyframe từ video.
- Chuyển đổi định dạng video/ảnh.
- Tính toán đặc trưng hình ảnh (ví dụ cho AI/ML).
- Tạo thumbnail hoặc preview động.

Vì vậy, cần một hệ thống để xử lý các tác vụ nặng này ở **chế độ nền (background)**, đảm bảo phản hồi frontend vẫn nhanh chóng.

---

## 🎯 Mục tiêu đề tài

Xây dựng hệ thống xử lý ảnh/video nặng bất đồng bộ sử dụng Celery và RabbitMQ:

- Người dùng upload ảnh/video/file → lưu tạm → đẩy task vào hàng đợi.
- Worker thực hiện xử lý (nén, resize, trích keyframe…).
- Lưu kết quả vào storage/database.
- Gửi thông báo khi hoàn tất (nếu cần).

---

## ⚙️ Công nghệ sử dụng

| Thành phần        | Công nghệ đề xuất                                 |
|-------------------|---------------------------------------------------|
| Backend API       | Python + Flask / Django                          |
| Task Queue        | Celery                                            |
| Message Broker    | RabbitMQ hoặc Redis                               |
| Xử lý ảnh/video   | Pillow, OpenCV, ffmpeg-python, moviepy, etc.     |
| Storage           | FileSystem hoặc Amazon S3                        |
| Giám sát          | Flower hoặc Celery Events                        |

---

## 🛠️ Ý tưởng mở rộng

### 1. Hệ thống xử lý ảnh
- Tự động resize ảnh về nhiều kích thước (thumbnail, medium, full).
- Tự động nén để giảm dung lượng.
- Chuyển định dạng (PNG → JPG…).
- Detect ảnh lỗi hoặc sai định dạng.

### 2. Xử lý video
- Trích xuất ảnh đại diện từ video (thumbnail, keyframe).
- Cắt video theo khoảng thời gian.
- Chuyển đổi định dạng video (mp4 → webm...).
- Nén video hoặc thay đổi độ phân giải.

### 3. Theo dõi tiến trình xử lý
- API lấy trạng thái file: đang xử lý, đã xử lý, lỗi.
- Kết hợp WebSocket hoặc polling để cập nhật trạng thái cho người dùng.

### 4. Tích hợp retry khi xử lý lỗi
- Worker tự động thử lại nếu xử lý thất bại (mất kết nối, lỗi file…).
- Ghi log lỗi vào DB để giám sát.

### 5. Tải lên file lớn
- Hỗ trợ upload chia nhỏ (chunk upload) nếu cần.
- Giao diện xử lý upload + chờ xử lý (UX tốt hơn).

---

## 🔁 Lịch trình xử lý định kỳ

- Dùng Celery Beat để xử lý lại các file chưa hoàn tất sau một khoảng thời gian.
- Dọn dẹp các file tạm/lỗi sau 24 giờ.

---

## 🔒 Bảo mật và hiệu suất

- Giới hạn định dạng, dung lượng file upload.
- Sử dụng hàng đợi để phân phối đều cho worker, tránh nghẽn cổ chai.
- Hạn chế người dùng thực hiện quá nhiều upload cùng lúc (rate limit).

---

## ✅ Kết luận

**Hệ thống Celery + RabbitMQ** không chỉ giúp tối ưu hiệu suất mà còn có thể mở rộng thành nền tảng xử lý ảnh/video mạnh mẽ, linh hoạt, hỗ trợ nhiều công nghệ backend hiện đại.

**Vấn đề giải quyết:** Tối ưu hóa xử lý các công việc nặng (image/video processing), giảm tải cho backend, tăng trải nghiệm người dùng và khả năng mở rộng hệ thống.