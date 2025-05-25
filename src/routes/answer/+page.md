# Ôn luyện thi cuối kì

## 1. Hệ thống phân tán, tập trung, phi tập trung khác nhau như thế nào, nêu ví dụ về mỗi loại, làm thế nào để xác định sự khác biệt chính?

**Hệ thống tập trung:**  
Mọi dữ liệu và xử lý đều được quản lý bởi một máy chủ trung tâm duy nhất. Các nút khác (thường là client) hoàn toàn phụ thuộc vào trung tâm này. Một số ví dụ điển hình bao gồm các hệ thống web truyền thống (client-server), hệ thống quản lý ngân hàng nội bộ, hay mạng xã hội như Facebook.

**Hệ thống phân tán:**  
Ở đây, các quyết định có thể được đưa ra bởi một nút trung tâm hoặc một nhóm các nút lớn, nhưng quá trình xử lý và hoạt động lại được phân bổ trên nhiều nút khác nhau. Ví dụ: Google Search, các mạng phân phối nội dung (CDN), hoặc hệ thống máy tính đa lõi.

**Hệ thống phi tập trung:**  
Không tồn tại bất kỳ điểm trung tâm kiểm soát nào. Tất cả các nút đều có quyền tham gia vào quá trình ra quyết định thông qua sự đồng thuận. Điều này tăng cường khả năng chống kiểm duyệt, ví dụ như blockchain (Bitcoin, Ethereum), BitTorrent, hay IPFS.

**Tiêu chí so sánh:**

| Tiêu chí | Tập trung | Phân tán | Phi tập trung |
|---|---|---|---|
| Trung tâm điều khiển | Có | Có thể có | Không có |
| Phân bổ xử lý | Không | Có | Có |
| Quyết định toàn cục | Trung tâm | Trung tâm hoặc nhóm lớn | Các nút cùng tham gia |
| Độ tin cậy | Dễ bị lỗi toàn hệ thống | Một phần còn hoạt động | Hệ thống vẫn tiếp tục nhờ các nút khác |

---

## 2. Các đặc tính của hệ phân tán là gì? giải thích cho từng đặc điểm thật kỹ

- Chia sẻ tài nguyên:
    - Kết nối tài nguyên
    - Giảm chi phí
    - Tăng tính sẵn sàng
    - Hỗ trợ làm việc nhóm
    - Tăng rủi ro về an toàn thông tin

- Tính trong suốt (**Transparency**):
    - Hệ thống là duy nhất với **NSD**:
        - Giao diện giống nhau
        - Cách thức truy cập giống nhau
    - Trong suốt về qui mô và vị trí
    - Che giấu tính phân tán của hệ phân tán
    - Mức độ trong suốt:
        - Cân bằng giữa hiệu năng và độ trong suốt

- Tính mở:
    - Cho phép các thành phần có thể được sản xuất bơi các NSX khác nhau
    - Hệ phân tán mở cung cấp các dịch vụ theo các đặc tả về cú pháp và ngữ nghiã của các dịch vụ, gọi là `Giao diện`
    - Thường được mô tả bằng ngôn ngữ tương tác dữ liệu (**IDL**)
    - Tính đầy đủ của đặc tả:
        - Quá chi tiết: phụ thuộc vào cài đặt cụ thể của dịch vụ
        - Không đủ chi tiết: Khi cài đặt phải bổ sung thêm, phục thuộc vào cài đặt cụ thể của dịch vụ
    - Khả năng phối hợp (**Interoperability**)
    - Tính khả chuyển (**Portability**)
    - Tính mềm dẻo + mở rộng được (**Flexibility**, **Extensibility**)
    - Thực hiện: Tách biệt chính sách và cơ chế

- Tính co giãn:
    - Quy mô:
        - Số lượng **NSD** và tài nguyên thay đổi
    - Không gian địa lý:
        - Quy mô vùng địa lý có tài nguyên và **NSD** thay đổi
    - Tổ chucswL
        - Quy mô tổ chức thay đối => tổ chức hệ thống thành các domain

    - Co giãn theo số lượng:
        - Mô hình tập trung:
            - Dịch vụ: cổ chai
            - Dữ liệu: lưu trữ, xử lý
            - Giải thuật: thông tin vào ra, xử lý
        - Mô hình không tập trung:
            - Phức tạp, gặp các vấn đề về bảo mật và riêng tư
            - Quyết định cục bộ
            - Khó phát hiện được lỗi
    - Co giãn theo không gian địa lý
        - Gần: Mạng cục bộ
            - Quảng bá, tốc độ cao, tin cậy, độ trễ cố định
        - Xa: Mạng diện rộng
            - Điểm điểm, tốc độ thấp, không tin cậy, độ trễ thay đổi
        - Khác nhau:
            - Tốc độ truyền tin, độ trễ,..
            - Đồng bộ/Không đồng bộ
            - Các thao tác quảng bá

---

## 3. Mục đích của nút chủ trong một hệ phân tán là để làm gì? Điều gì sẽ xảy ra nếu nút chủ gặp sự cố?

- **Vai trò:**  
Nút chủ (master node) đảm nhiệm việc điều phối hoạt động, duy trì tính nhất quán dữ liệu và quản lý trạng thái toàn hệ thống.

- **Nếu xảy ra sự cố:**  
Khi nút chủ gặp lỗi, hệ thống có thể ngừng hoạt động, dữ liệu mất đồng bộ, thậm chí có thể xuất hiện tình trạng chia rẽ hệ thống (split-brain).

- **Giải pháp:**  
Các cơ chế như bầu chọn leader mới (Paxos, Raft), dự phòng nóng (hot standby), hoặc sử dụng kiến trúc không có master (Cassandra, DynamoDB) được áp dụng để đảm bảo tính liên tục và ổn định của hệ thống.

→ **Kết luận**: Nút chủ là yếu tố trọng yếu, nhưng cũng là điểm dễ gây ra sự cố nghiêm trọng nếu không có cơ chế dự phòng phù hợp.

---

## 4. Trong một mạng không gian, tại sao các máy thường giao tiếp với nhau qua gossip protocol mà không gửi thông tin đến tất cả các máy khác hoặc gửi về một nút trung tâm?

Phương pháp phát tán thông tin đến tất cả các máy hoặc tập trung gửi về một nút trung tâm sẽ gây ra tắc nghẽn mạng, tạo ra điểm nghẽn hoặc thậm chí là rủi ro “đơn điểm thất bại”. **Gossip protocol** cho phép các nút trao đổi thông tin theo cách “truyền miệng”: mỗi nút chỉ chia sẻ với một vài nút khác, thông tin dần lan tỏa khắp hệ thống. Cách này giúp giảm tải mạng, tăng hiệu quả truyền thông tin, đồng thời tránh tình trạng quá tải hoặc phụ thuộc vào một điểm duy nhất.

---

## 5. Các yếu tố cốt lõi của một hệ phân tán là gì?

Để xây dựng một hệ phân tán hiệu quả, cần chú trọng các yếu tố then chốt sau:

---

### 1. Phân tán (Distribution)
- Không tồn tại điểm tập trung duy nhất; hệ thống không phụ thuộc vào bất kỳ máy chủ hay nút riêng lẻ nào.
- Các nút có thể đặt tại nhiều vị trí địa lý khác nhau, bao gồm trung tâm dữ liệu, nền tảng đám mây hoặc thiết bị biên.

### 2. Song song hóa (Parallelism)
- Nhiều tác vụ được xử lý đồng thời trên các nút khác nhau, tăng hiệu suất thực thi.
- Cơ chế cân bằng tải giúp phân bố công việc tối ưu giữa các nút.

### 3. Nhất quán (Consistency)
- Dữ liệu được đồng bộ hóa giữa các nút, đảm bảo mọi thành phần đều quan sát cùng một trạng thái dữ liệu (dựa vào mô hình nhất quán mạnh hoặc nhất quán cuối cùng).
- Áp dụng các thuật toán đồng thuận như Paxos, Raft nhằm đạt sự nhất trí giữa các nút.

### 4. Khả năng chịu lỗi (Fault Tolerance)
- Hệ thống có khả năng tự phục hồi khi một số nút gặp sự cố, đảm bảo hoạt động liên tục.
- Dữ liệu được sao lưu trên nhiều nút để tăng tính dự phòng.

### 5. Minh bạch (Transparency)
- Người dùng không cần biết dữ liệu lưu trữ hay xử lý tại đâu; mọi phức tạp được ẩn phía sau.
- Giao diện truy cập thống nhất, bất kể dữ liệu phân tán.

### 6. Khả năng mở rộng (Scalability)
- Có thể mở rộng hệ thống bằng cách bổ sung thêm nút mà không cần nâng cấp phần cứng hiện tại.
- Kiến trúc tránh các điểm nghẽn tài nguyên tập trung.

### 7. Bảo mật (Security)
- Dữ liệu được mã hóa khi truyền giữa các nút.
- Cơ chế xác thực và phân quyền đảm bảo chỉ các thành phần hợp lệ được tham gia hệ thống.

### 8. Giao tiếp không đồng bộ (Asynchronous Communication)
- Các nút có thể trao đổi thông tin mà không cần phản hồi tức thì, cho phép xử lý độc lập dựa trên thông điệp.

---

### Ý nghĩa của các yếu tố này

Những yếu tố trên đảm bảo hệ thống phân tán đạt được độ tin cậy cao, hiệu suất tốt và khả năng mở rộng linh hoạt trong môi trường phức tạp. Các hệ thống thực tế như Google Spanner (đảm bảo nhất quán mạnh và phân tán địa lý), Bitcoin (đồng thuận phi tập trung và khả năng chịu lỗi), Kubernetes (quản lý mở rộng ngang và tự phục hồi) đều minh chứng cho tầm quan trọng của các yếu tố này.

→ Thiếu một trong những yếu tố nêu trên sẽ khiến hệ thống gặp các vấn đề như nghẽn cổ chai, mất dữ liệu hoặc giảm tính ổn định.

---

## 6. Nêu những lí do sử dụng hệ phân tán.

| Tiêu chí              | Hệ phân tán                            |  
|-----------------------|----------------------------------------|  
| Khả năng mở rộng      | Dễ dàng (bổ sung thêm nút)             |
| Độ tin cậy            | Cao (không có điểm lỗi duy nhất)       |
| Hiệu suất             | Xử lý song song, giảm độ trễ            |
| Chi phí               | Tận dụng phần cứng phổ thông            |
| Bảo trì               | Linh hoạt, có thể nâng cấp từng phần    |

---

→ **Kết luận**: Hệ phân tán là giải pháp tối ưu cho các bài toán yêu cầu hiệu suất cao, độ tin cậy và khả năng mở rộng mà hệ tập trung khó đáp ứng.

---

## 7. Nêu định nghĩa hệ phân tán.

Hệ phân tán là tập hợp các máy tính độc lập, nhưng đối với người dùng, hệ thống này vận hành như một thể thống nhất. `(Theo Andrew Tannenbaum)`

---

## 8. Thuật toán Cristian, Berkeley, RBS, Lamport, Bully, Ring.

- **Cristian**

![Cristian algorithm](/images/cristian.png)

- **Berkeley**

![Berkeley algorithm](/images/berkeley.png)

- **RBS**

![RBS algorithm](/images/rbs.png)

- **Lamport**

![Lamport algorithm](/images/lamport.png)

- **Bully**

![Bully algorithm](/images/bully.png)

- **Ring**

![Ring algorithm](/images/ring.png)

---

## 9. Kỹ thuật phân tán nào hỗ trợ lập trình thủ tục, lập trình web, hướng đối tượng, liệt kê.

---

### **1. Lập trình thủ tục (Procedural Programming)**
- **Kỹ thuật phân tán phù hợp**:  
  - **Remote Procedure Call (RPC)**: Cho phép gọi hàm từ xa như gọi hàm cục bộ.  
    - **Ví dụ**: gRPC, Apache Thrift.  
  - **Message Passing Interface (MPI)**: Dùng trong tính toán song song (HPC).  

### **2. Lập trình web (Web-Based Programming)**
- **Kỹ thuật phân tán phù hợp**:  
  - **RESTful API/HTTP**: Giao tiếp qua HTTP request/response.  
    - **Ví dụ**: Microservices (Spring Boot, Flask).  
  - **WebSockets**: Giao tiếp hai chiều thời gian thực.  
    - **Ví dụ**: Chat apps, stock trading platforms.  
  - **Serverless Computing**: Chạy hàm phân tán không cần quản lý server.  
    - **Ví dụ**: AWS Lambda, Google Cloud Functions.  

### **3. Lập trình hướng đối tượng (OOP)**
- **Kỹ thuật phân tán phù hợp**:  
  - **Distributed Objects**: Đối tượng phân tán trên nhiều máy.  
    - **Ví dụ**: Java RMI (Remote Method Invocation), CORBA.  
  - **Actor Model**: Mỗi đối tượng (actor) xử lý độc lập.  
    - **Ví dụ**: Akka, Erlang.  

### **4. Lập trình liệt kê/sự kiện (Event-Driven Programming)**
- **Kỹ thuật phân tán phù hợp**:  
  - **Publish-Subscribe (Pub/Sub)**: Các thành phần giao tiếp qua sự kiện.  
    - **Ví dụ**: Apache Kafka, RabbitMQ.  
  - **Event Sourcing**: Lưu trữ trạng thái hệ thống dưới dạng chuỗi sự kiện.  
    - **Ví dụ**: CQRS (Command Query Responsibility Segregation).  

---

1. **RPC (Remote Procedure Call)**  
   - Phù hợp với **lập trình thủ tục** vì mô phỏng cách gọi hàm tuần tự.  
   - **Hạn chế**: Khó debug do phụ thuộc network.  

2. **Microservices (REST/Web)**  
   - Mỗi service là một ứng dụng web độc lập, dễ scale.  
   - **Ưu điểm**: Tương thích với HTTP/JSON, phổ biến trong web hiện đại.  

3. **Actor Model (OOP)**  
   - Mỗi actor là một đối tượng độc lập, xử lý message bất đồng bộ.  
   - **Ưu điểm**: Chịu lỗi cao (Erlang dùng trong viễn thông).  

4. **Pub/Sub (Event-Driven)**  
   - Component giao tiếp gián tiếp qua message broker.  
   - **Ưu điểm**: Decoupling, xử lý sự kiện thời gian thực.  

---

## 10. Tiến trình nhẹ, tiến trình, luồng có những ưu điểm và nhược điểm gì, liệt kê. Khi một lời gọi hệ thống dừng thì đối với 3 loại như thế nào. Tiến trình nhẹ, tiến trình và luồng có mối quan hệ như thế nào với nhau và với chính nó?