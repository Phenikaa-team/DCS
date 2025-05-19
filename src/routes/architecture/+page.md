# Báo cáo Bài Tập: Giao Thức Mạng và OpenMPI

## 1. Tìm hiểu các giao thức HTTP, TCP/IP, UDP, REST, GraphQL, SOAP, AJAX, RPC, gRPC

### Mục đích sử dụng và đặc điểm chính:

| Giao thức | Mục đích sử dụng | Đặc điểm nổi bật |
|----------|------------------|------------------|
| **HTTP** | Truyền tải dữ liệu qua web | Dựa trên mô hình request/response, dùng nhiều cho ứng dụng web |
| **TCP/IP** | Giao tiếp mạng cơ bản | TCP đảm bảo truyền dữ liệu đáng tin cậy, IP định tuyến gói tin |
| **UDP** | Giao tiếp mạng không đảm bảo | Nhanh, không đảm bảo độ tin cậy, phù hợp cho video/voice streaming |
| **REST** | Thiết kế API theo nguyên lý HTTP | Dễ hiểu, dựa trên URL, sử dụng phương thức HTTP (GET, POST, PUT, DELETE) |
| **GraphQL** | API truy vấn linh hoạt | Cho phép client chỉ định dữ liệu cần lấy, hiệu quả hơn REST trong nhiều trường hợp |
| **SOAP** | Giao thức web service chuẩn | Dựa trên XML, mạnh mẽ nhưng nặng nề, thường dùng trong môi trường doanh nghiệp |
| **AJAX** | Tương tác web không tải lại trang | Sử dụng JavaScript để gửi/nhận dữ liệu bất đồng bộ từ server |
| **RPC** | Gọi hàm từ xa | Cho phép client gọi hàm trên server như gọi local function |
| **gRPC** | RPC sử dụng HTTP/2 và protobuf | Nhanh, nhẹ, hỗ trợ đa ngôn ngữ, phù hợp cho microservices |

### Mối liên quan:

- **HTTP** là nền tảng cho **REST**, **GraphQL**, **SOAP**, **AJAX** và **gRPC**.
- **TCP/IP** là tầng thấp hơn, làm nền tảng cho HTTP, UDP, gRPC, RPC,...
- **REST**, **GraphQL**, **SOAP** là kiến trúc thiết kế API chạy trên HTTP.
- **RPC** và **gRPC** đều là cơ chế gọi hàm từ xa, gRPC hiện đại hơn và sử dụng protobuf.
- **AJAX** sử dụng HTTP để giao tiếp bất đồng bộ trên trình duyệt.
- **UDP** khác với TCP ở chỗ không đảm bảo độ tin cậy nhưng có tốc độ cao hơn.

---

## 2. Nghiên cứu thư viện OpenMPI

### Tính năng chính:

- Thư viện mã nguồn mở dùng để lập trình song song phân tán.
- Hỗ trợ giao tiếp giữa các tiến trình trên nhiều máy tính trong một mạng.
- Tuân theo chuẩn MPI (Message Passing Interface).
- Tương thích với nhiều hệ điều hành và trình biên dịch.

### Một số hàm cơ bản:

| Hàm | Chức năng |
|-----|-----------|
| `MPI_Init` | Khởi tạo môi trường MPI |
| `MPI_Comm_size` | Lấy số tiến trình đang chạy |
| `MPI_Comm_rank` | Lấy ID của tiến trình hiện tại |
| `MPI_Send` | Gửi dữ liệu đến tiến trình khác |
| `MPI_Recv` | Nhận dữ liệu từ tiến trình khác |
| `MPI_Finalize` | Kết thúc chương trình MPI |

---

## 3. Giải pháp tính 10,000,000 số nguyên tố đầu tiên bằng OpenMPI

### Mô tả bài toán:
- Tìm 10 triệu số nguyên tố đầu tiên.
- Hệ thống gồm **16 máy**, mỗi máy **2 core** → tổng cộng **32 core**.

### Phương pháp đề xuất:

1. **Phân tích số lượng cần tính**:
   - Không cần kiểm tra toàn bộ các số đến một giới hạn nào đó, có thể dùng **sàng Eratosthenes** (Sieve of Eratosthenes).

2. **Phân chia công việc đều**:
   - Chia khoảng số cần kiểm tra cho các tiến trình.
   - Mỗi tiến trình kiểm tra số nguyên tố độc lập trong khoảng được phân công.

3. **Sử dụng MPI để giao tiếp**:
   - Một tiến trình **master** sẽ phân công công việc và thu kết quả.
   - Các tiến trình **worker** tính số nguyên tố và gửi kết quả về.

4. **Linh hoạt theo số core**:
   - Thay vì cố định số tiến trình, nên thiết kế chương trình theo **số tiến trình đầu vào (dynamic)** để chạy được với 8, 10, 12, 32,... core tùy cấu hình.
   - Có thể sử dụng `mpirun -np <số tiến trình>` để điều chỉnh.

### Sơ đồ luồng hoạt động:

```text
[Master]
    |
    | gửi phân đoạn
    ↓
[Worker 1] → tính toán → gửi kết quả
[Worker 2] → tính toán → gửi kết quả
[...]
[Worker N] → tính toán → gửi kết quả
    ↑
    | tổng hợp kết quả
    |
[Master]
```

### Tham khảo thuật toán:

- Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- Triển khai có thể dùng **segmented sieve** để giảm bộ nhớ và tăng hiệu quả.

---

## Kết luận:

- Việc hiểu rõ các giao thức mạng giúp thiết kế hệ thống phù hợp mục đích: truyền dữ liệu, tạo API, xử lý bất đồng bộ.
- OpenMPI là giải pháp mạnh để xử lý phân tán song song.
- Bài toán tính số nguyên tố với OpenMPI cần chia nhỏ bài toán, tận dụng tối đa tài nguyên, và có thể mở rộng/linh hoạt theo số core.