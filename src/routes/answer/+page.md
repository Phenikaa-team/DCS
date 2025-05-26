# **Ôn luyện thi cuối kì**

## **Câu 1. Hệ thống phân tán, tập trung, phi tập trung khác nhau như thế nào, nêu ví dụ về mỗi loại, làm thế nào để xác định sự khác biệt chính?**

- **Hệ thống tập trung:**  
Mọi dữ liệu và xử lý đều được quản lý bởi một máy chủ trung tâm duy nhất. Các nút khác (thường là client) hoàn toàn phụ thuộc vào trung tâm này. Một số ví dụ điển hình bao gồm các hệ thống web truyền thống (client-server), hệ thống quản lý ngân hàng nội bộ, hay mạng xã hội như Facebook.

- **Hệ thống phân tán:**  
Ở đây, các quyết định có thể được đưa ra bởi một nút trung tâm hoặc một nhóm các nút lớn, nhưng quá trình xử lý và hoạt động lại được phân bổ trên nhiều nút khác nhau. Ví dụ: Google Search, các mạng phân phối nội dung (CDN), hoặc hệ thống máy tính đa lõi.

- **Hệ thống phi tập trung:**  
Không tồn tại bất kỳ điểm trung tâm kiểm soát nào. Tất cả các nút đều có quyền tham gia vào quá trình ra quyết định thông qua sự đồng thuận. Điều này tăng cường khả năng chống kiểm duyệt, ví dụ như blockchain (Bitcoin, Ethereum), BitTorrent, hay IPFS.

**Tiêu chí so sánh:**

| Tiêu chí | Tập trung | Phân tán | Phi tập trung |
|---|---|---|---|
| Trung tâm điều khiển | Có | Có thể có | Không có |
| Phân bổ xử lý | Không | Có | Có |
| Quyết định toàn cục | Trung tâm | Trung tâm hoặc nhóm lớn | Các nút cùng tham gia |
| Độ tin cậy | Dễ bị lỗi toàn hệ thống | Một phần còn hoạt động | Hệ thống vẫn tiếp tục nhờ các nút khác |

---

## **Câu 2. Các đặc tính của hệ phân tán là gì? giải thích cho từng đặc điểm thật kỹ**

- **Chia sẻ tài nguyên**:
    - Kết nối tài nguyên
    - Giảm chi phí
    - Tăng tính sẵn sàng
    - Hỗ trợ làm việc nhóm
    - Tăng rủi ro về an toàn thông tin

- **Tính trong suốt** (Transparency):
    - Hệ thống là duy nhất với **NSD**:
        - Giao diện giống nhau
        - Cách thức truy cập giống nhau
    - Trong suốt về qui mô và vị trí
    - Che giấu tính phân tán của hệ phân tán
    - Mức độ trong suốt:
        - Cân bằng giữa hiệu năng và độ trong suốt

- **Tính mở**:
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

- **Tính co giãn**:
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

## **Câu 3. Mục đích của nút chủ trong một hệ phân tán là để làm gì? Điều gì sẽ xảy ra nếu nút chủ gặp sự cố?**

- **Vai trò:**  
Nút chủ (master node) đảm nhiệm việc điều phối hoạt động, duy trì tính nhất quán dữ liệu và quản lý trạng thái toàn hệ thống.

- **Nếu xảy ra sự cố:**  
Khi nút chủ gặp lỗi, hệ thống có thể ngừng hoạt động, dữ liệu mất đồng bộ, thậm chí có thể xuất hiện tình trạng chia rẽ hệ thống (split-brain).

- **Giải pháp:**  
Các cơ chế như bầu chọn leader mới (Paxos, Raft), dự phòng nóng (hot standby), hoặc sử dụng kiến trúc không có master (Cassandra, DynamoDB) được áp dụng để đảm bảo tính liên tục và ổn định của hệ thống.

→ **Kết luận**: Nút chủ là yếu tố trọng yếu, nhưng cũng là điểm dễ gây ra sự cố nghiêm trọng nếu không có cơ chế dự phòng phù hợp.

---

## **Câu 4. Trong một mạng không gian, tại sao các máy thường giao tiếp với nhau qua gossip protocol mà không gửi thông tin đến tất cả các máy khác hoặc gửi về một nút trung tâm?**

- Phương pháp phát tán thông tin đến tất cả các máy hoặc tập trung gửi về một nút trung tâm sẽ gây ra tắc nghẽn mạng, tạo ra điểm nghẽn hoặc thậm chí là rủi ro “đơn điểm thất bại”. **Gossip protocol** cho phép các nút trao đổi thông tin theo cách “truyền miệng”: mỗi nút chỉ chia sẻ với một vài nút khác, thông tin dần lan tỏa khắp hệ thống. Cách này giúp giảm tải mạng, tăng hiệu quả truyền thông tin, đồng thời tránh tình trạng quá tải hoặc phụ thuộc vào một điểm duy nhất.

---

## **Câu 5. Các yếu tố cốt lõi của một hệ phân tán là gì?**

Để xây dựng một hệ phân tán hiệu quả, cần chú trọng các yếu tố then chốt sau:

---

- **1. Phân tán (Distribution)**
  - Không tồn tại điểm tập trung duy nhất; hệ thống không phụ thuộc vào bất kỳ máy chủ hay nút riêng lẻ nào.
  - Các nút có thể đặt tại nhiều vị trí địa lý khác nhau, bao gồm trung tâm dữ liệu, nền tảng đám mây hoặc thiết bị biên.

- **2. Song song hóa (Parallelism)**
  - Nhiều tác vụ được xử lý đồng thời trên các nút khác nhau, tăng hiệu suất thực thi.
  - Cơ chế cân bằng tải giúp phân bố công việc tối ưu giữa các nút.

- **3. Nhất quán (Consistency)**
  - Dữ liệu được đồng bộ hóa giữa các nút, đảm bảo mọi thành phần đều quan sát cùng một trạng thái dữ liệu (dựa vào mô hình nhất quán mạnh hoặc nhất quán cuối cùng).
  - Áp dụng các thuật toán đồng thuận như Paxos, Raft nhằm đạt sự nhất trí giữa các nút.

- **4. Khả năng chịu lỗi (Fault Tolerance)**
  - Hệ thống có khả năng tự phục hồi khi một số nút gặp sự cố, đảm bảo hoạt động liên tục.
  - Dữ liệu được sao lưu trên nhiều nút để tăng tính dự phòng.

- **5. Minh bạch (Transparency)**
  - Người dùng không cần biết dữ liệu lưu trữ hay xử lý tại đâu; mọi phức tạp được ẩn phía sau.
  - Giao diện truy cập thống nhất, bất kể dữ liệu phân tán.

- **6. Khả năng mở rộng (Scalability)**
  - Có thể mở rộng hệ thống bằng cách bổ sung thêm nút mà không cần nâng cấp phần cứng hiện tại.
  - Kiến trúc tránh các điểm nghẽn tài nguyên tập trung.

- **7. Bảo mật (Security)**
  - Dữ liệu được mã hóa khi truyền giữa các nút.
  - Cơ chế xác thực và phân quyền đảm bảo chỉ các thành phần hợp lệ được tham gia hệ thống.

- **8. Giao tiếp không đồng bộ (Asynchronous Communication)**
  - Các nút có thể trao đổi thông tin mà không cần phản hồi tức thì, cho phép xử lý độc lập dựa trên thông điệp.

---

### Có thể thấy:

Những yếu tố trên đảm bảo hệ thống phân tán đạt được độ tin cậy cao, hiệu suất tốt và khả năng mở rộng linh hoạt trong môi trường phức tạp. Các hệ thống thực tế như Google Spanner (đảm bảo nhất quán mạnh và phân tán địa lý), Bitcoin (đồng thuận phi tập trung và khả năng chịu lỗi), Kubernetes (quản lý mở rộng ngang và tự phục hồi) đều minh chứng cho tầm quan trọng của các yếu tố này.

→ Thiếu một trong những yếu tố nêu trên sẽ khiến hệ thống gặp các vấn đề như nghẽn cổ chai, mất dữ liệu hoặc giảm tính ổn định.

---

## **Câu 6. Nêu những lí do sử dụng hệ phân tán.**

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

## **Câu 7. Nêu định nghĩa hệ phân tán.**

- Hệ phân tán là tập hợp các máy tính độc lập, nhưng đối với người dùng, hệ thống này vận hành như một thể thống nhất. `(Theo Andrew Tannenbaum)`

---

## **Câu 8. Thuật toán Cristian, Berkeley, RBS, Lamport, Bully, Ring.**

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

## **Câu 9. Kỹ thuật phân tán nào hỗ trợ lập trình thủ tục, lập trình web, hướng đối tượng, liệt kê.**

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

## **Câu 10. Tiến trình nhẹ, tiến trình, luồng có những ưu điểm và nhược điểm gì, liệt kê. Khi một lời gọi hệ thống dừng thì đối với 3 loại như thế nào. Tiến trình nhẹ, tiến trình và luồng có mối quan hệ như thế nào với nhau và với chính nó?**

| **Loại**            | **Ưu điểm**                                                                 | **Nhược điểm**                                                                 |
|----------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Tiến trình (Process)** | - Cách ly tốt, an toàn (lỗi một tiến trình không ảnh hưởng tiến trình khác).<br>- Tận dụng đa CPU hiệu quả.<br>- Quản lý tài nguyên độc lập (bộ nhớ, file, CPU). | - Tốn nhiều tài nguyên (bộ nhớ, thời gian khởi tạo).<br>- Chuyển đổi ngữ cảnh (context switch) chậm.<br>- Giao tiếp khó khăn (IPC phức tạp). |
| **Tiến trình nhẹ (LWP)** | - Kết hợp ưu điểm của luồng và tiến trình.<br>- Chia sẻ tài nguyên nhưng có không gian địa chỉ riêng.<br>- Đa luồng trong một tiến trình. | - Phức tạp hơn luồng thông thường.<br>- Vẫn tốn nhiều tài nguyên hơn luồng thuần túy. |
| **Luồng (Thread)**   | - Nhẹ, tạo và chuyển đổi nhanh.<br>- Chia sẻ tài nguyên dễ dàng (bộ nhớ, file).<br>- Hiệu suất cao khi xử lý đồng thời. | - Không cách ly (lỗi một luồng có thể làm crash cả tiến trình).<br>- Đồng bộ hóa phức tạp (race condition, deadlock). |

---

### **Khi một lời gọi hệ thống (system call) bị dừng (block)**
1. **Tiến trình (Process)**:  
   - Toàn bộ tiến trình bị dừng, kể cả các luồng bên trong (nếu có).  
   - Hệ điều hành chuyển sang chạy tiến trình khác.  

2. **Tiến trình nhẹ (LWP)**:  
   - Chỉ LWP gọi system call bị dừng, các LWP khác trong cùng tiến trình vẫn chạy.  
   - Có thể ánh xạ đến các kernel thread để tận dụng đa CPU.  

3. **Luồng (Thread)**:  
   - Nếu là **user-level thread**: Toàn bộ tiến trình bị dừng vì kernel không nhận biết các luồng.  
   - Nếu là **kernel-level thread**: Chỉ luồng gọi system call bị dừng, các luồng khác vẫn chạy.  

---

### **Mối quan hệ giữa Tiến trình, Tiến trình nhẹ và Luồng**
1. **Với nhau**:  
   - Một **tiến trình** có thể chứa nhiều **luồng** hoặc nhiều **tiến trình nhẹ (LWP)**.  
   - **LWP** là cầu nối giữa tiến trình và luồng:  
     - Mỗi LWP được kernel quản lý như một tiến trình ảo, nhưng chia sẻ không gian địa chỉ với các LWP khác trong cùng tiến trình.  
     - Các **user thread** có thể ánh xạ đến LWP để chạy song song trên đa CPU.  

2. **Với chính nó**:  
   - **Tiến trình**: Độc lập với các tiến trình khác (có PID riêng, không gian bộ nhớ riêng).  
   - **Luồng**: Các luồng trong cùng tiến trình chia sẻ tài nguyên (heap, file) nhưng có stack riêng.  
   - **LWP**: Có thể chạy song song nhờ ánh xạ đến kernel thread, nhưng vẫn chia sẻ bộ nhớ với các LWP cùng tiến trình.  

---

### **Ngắn gọn hơn thì**
- **1 Tiến trình = 1 hoặc nhiều Luồng/LWP**.  
- **LWP giống tiến trình** (được kernel quản lý) nhưng **chia sẻ tài nguyên như luồng**.  
- **Luồng user-level** cần LWP để chạy song song thật sự trên đa CPU.  

---

## **Câu 11. Mô hình client server là gì, vai trò của máy chủ, máy khách là gì?**

- Khái niệm:
  - Máy chủ(**Server**): Cung cấp tại nguyên, dịch vụ(ví dụ: web, database, file, ...).
  - Máy khách(**Client**): Gửi yêu cầu(request) và sử dụng dịch vụ từ máy chủ.
  - Giao tiếp qua mạng: Client và server trao đổi thông qua các giao thức (HTTP, TCP/IP, RPC...).

- Vai trò:
  - Máy chủ(**Server**): 
    - Lưu trữ và quản lý tài nguyên (dữ liệu, ứng dụng, dịch vụ).
    - Xử lý yêu cầu từ client (ví dụ: trả về webpage, kết quả truy vấn DB).
    - Đảm bảo tính sẵn sàng, bảo mật (phục vụ nhiều client đồng thời).
  -Máy khách(**Client**):
    - Gửi yêu cầu (request) đến server.
    - Hiển thị kết quả nhận được từ server (ví dụ: hiển thị web, ứng dụng).
    - Tương tác với người dùng (nhập liệu, gửi form).

---

## **Câu 12. Quá trình gọi thủ tục từ xa là gì?**

- Quá trình gọi thủ tục từ xa (**Remote Procedure Call - RPC**) là cơ chế cho phép một chương trình trên máy tính này gọi hàm/thủ tục(procedure) thực thi trên máy tính khác trong hệ phân tán, như thể nó đang trên cùng một máy

---

## **Câu 13. Nêu mục đích và lợi ích của mô hình phân tầng giao thức, hướng thông điệp bền vững.**

**Mục đích và Lợi ích của Mô hình Phân Tầng Giao Thức và Hướng Thông Điệp Bền Vững trong Hệ Phân Tán**

---

## **1. Mô hình Phân Tầng Giao Thức (Protocol Layering)**
### **Mục đích**
- **Chia nhỏ độ phức tạp**: Phân tách hệ thống mạng thành các tầng (layer) độc lập, mỗi tầng giải quyết một nhiệm vụ cụ thể (ví dụ: định tuyến, truyền dữ liệu, mã hóa).  
- **Chuẩn hóa**: Đảm bảo các hệ thống khác nhau có thể giao tiếp được với nhau thông qua các giao thức chuẩn (TCP/IP, HTTP, FTP...).  
- **Dễ bảo trì & nâng cấp**: Thay đổi một tầng không ảnh hưởng đến các tầng khác.  

### **Lợi ích**
| **Lợi ích**               | **Giải thích**                                                                 |
|---------------------------|-------------------------------------------------------------------------------|
| **Tính module hóa**       | Mỗi tầng có chức năng riêng, dễ dàng thay thế (ví dụ: thay TCP bằng UDP).      |
| **Khả năng tương thích**  | Các thiết bị từ nhiều nhà sản xuất có thể hoạt động cùng nhau (nhờ chuẩn chung như OSI/TCP-IP). |
| **Hiệu suất cao**         | Tối ưu hóa từng tầng (ví dụ: tầng vật lý xử lý tín hiệu, tầng ứng dụng xử lý dữ liệu). |
| **Dễ dàng debug**         | Lỗi có thể được xác định và sửa chữa trong từng tầng cụ thể.                   |

**Ví dụ**:  
- **Mô hình TCP/IP** gồm 4 tầng:  
  1. **Tầng ứng dụng (HTTP, FTP)**  
  2. **Tầng giao vận (TCP/UDP)**  
  3. **Tầng mạng (IP)**  
  4. **Tầng vật lý (Ethernet, WiFi)**  

---

## **2. Hướng Thông Điệp Bền Vững (Persistent Messaging)**
### **Mục đích**
- **Đảm bảo tin cậy**: Thông điệp không bị mất ngay cả khi hệ thống gặp sự cố (server crash, mạng gián đoạn).  
- **Hỗ trợ giao tiếp bất đồng bộ**: Client và server không cần kết nối đồng thời (phù hợp cho hệ thống phân tán có độ trễ cao).  

### **Lợi ích**
| **Lợi ích**               | **Giải thích**                                                                 |
|---------------------------|-------------------------------------------------------------------------------|
| **Tính tin cậy cao**      | Thông điệp được lưu trữ đến khi xử lý thành công (dùng **message queue** như Kafka, RabbitMQ). |
| **Chịu lỗi (Fault Tolerance)** | Nếu server sập, thông điệp vẫn tồn tại và được xử lý khi server khôi phục.    |
| **Giảm tải cho hệ thống** | Xử lý theo hàng đợi, tránh quá tải đột ngột.                                  |
| **Hỗ trợ kiến trúc Event-Driven** | Phù hợp với microservices, IoT, hệ thống real-time.                          |

**Ví dụ**:  
- **Kafka**: Lưu trữ thông điệp trên disk, đảm bảo không mất dữ liệu ngay cả khi broker gặp sự cố.  
- **RabbitMQ**: Hỗ trợ **acknowledgment** để xác nhận thông điệp đã được xử lý.  

---

## **Câu 14. Sharding là gì**

- **Sharding** là một kỹ thuật phân tán dữ liệu trong các hệ thống phân tán (distributed systems) hoặc cơ sở dữ liệu phân tán (distributed databases), nhằm **chia nhỏ dữ liệu thành các phần độc lập** gọi là **shard** và phân tán chúng trên nhiều máy chủ (node) khác nhau để cải thiện hiệu suất, khả năng mở rộng (scalability) và độ tin cậy.

---

## **Câu 15. Các gói luồng có thế làm những nhiệm vụ gì?**

- Trong hệ phân tán, **các gói luồng (thread pools)** đóng vai trò quan trọng trong việc quản lý tài nguyên và tối ưu hiệu suất. Chúng giúp kiểm soát số lượng luồng **(threads)** đồng thời, tránh tạo/quá tải luồng quá mức. Dưới đây là các nhiệm vụ chính của gói luồng trong hệ phân tán:

  - 1. **Xử lý yêu cầu song song (Parallel Request Handling)**:
    - **Nhận và phân phối tác vụ**: Gói luồng quản lý một nhóm luồng được tạo sẵn để xử lý các yêu cầu từ client hoặc các node khác trong hệ thống phân tán.

  - 2. **Quản lý tài nguyên hiệu quả (Resource Management)**:
    - **Giới hạn số luồng đồng thời**: Tránh tạo quá nhiều luồng dẫn đến tốn bộ nhớ hoặc tranh chấp CPU.

    - **Tái sử dụng luồng**: Thay vì tạo/xóa luồng liên tục (tốn chi phí), thread pool duy trì sẵn các luồng để tái sử dụng.

  - 3. **Hỗ trợ xử lý sự kiện (Event-Driven Processing)**:
    - **Xử lý sự kiện mạng**: Trong hệ phân tán, các node thường giao tiếp qua mạng (RPC, message queue). Thread pool giúp xử lý các sự kiện như nhận/gửi dữ liệu mà không chặn luồng chính.

  - 4. **Điều phối tác vụ nền (Background Task Scheduling)**
    - **Thực hiện tác vụ định kỳ**: Như đồng bộ dữ liệu giữa các node, dọn dẹp bộ nhớ đệm, kiểm tra node sống/chết (heartbeat).

  - 5. **Xử lý giao dịch phân tán (Distributed Transactions)**:
    - **Phối hợp giữa các node**: Khi thực hiện giao dịch đa node (như 2PC – Two-Phase Commit), thread pool giúp quản lý các luồng phụ trách giao tiếp và xác nhận giữa các node.

  - 5. **Cân bằng tải (Load Balancing)**:
    - **Phân phối tác vụ đều giữa các luồng**: Tránh tình trạng một số luồng quá tải trong khi số khác nhàn rỗi.

  - 7. **Xử lý lỗi và phục hồi (Fault Tolerance)**
    - **Giám sát và khôi phục luồng**: Nếu một luồng bị lỗi, thread pool có thể tạo luồng mới thay thế mà không ảnh hưởng đến hệ thống.

---

## **Câu 16. Phân loại sự khác nhau giữa luồng kiểu người dùng và luồng kiểu nhân**

  | Tiêu chí                              | **Luồng kiểu người dùng (User-Level Threads)** | **Luồng kiểu nhân (Kernel-Level Threads)** |
  | ------------------------------------- | ---------------------------------------------- | ------------------------------------------ |
  | **Quản lý bởi**                       | Thư viện trong không gian người dùng           | Kernel (nhân hệ điều hành)                 |
  | **Tạo luồng**                         | Nhanh, không cần gọi hệ thống (`syscall`)      | Chậm hơn, cần tương tác với nhân           |
  | **Chuyển đổi giữa luồng**             | Rất nhanh (không qua nhân)                     | Chậm hơn (cần vào nhân)                    |
  | **Lập lịch (scheduling)**             | Do người dùng quản lý                          | Do kernel quản lý                          |
  | **Khả năng chạy song song (đa nhân)** | Không thể (nếu kernel không hỗ trợ)            | Có thể chạy song song trên nhiều CPU       |
  | **Khi 1 luồng bị block (I/O, v.v.)**  | Cả tiến trình bị block                         | Chỉ luồng đó bị block                      |
  | **Tính linh hoạt**                    | Cao, lập lịch tùy biến                         | Thấp hơn, phụ thuộc vào kernel             |
  | **Khả năng gỡ lỗi (debug)**           | Khó hơn, do kernel không "nhìn thấy"           | Dễ hơn, vì kernel kiểm soát trực tiếp      |
  | **Chi phí ngữ cảnh (context switch)** | Rất thấp                                       | Cao hơn do phải chuyển vào kernel          |

---

## **Câu 17. Nêu các hàm chính ở trong RPC và giải thích chức năng của nó.**

  - 1. **Client Stub (Client Proxy)**
    - Đây là hàm (hoặc module) mà phía client sử dụng để gọi hàm từ xa. Client stub đóng vai trò như một đại diện (proxy) cho hàm thực trên server. Nó chịu trách nhiệm:

      - Gói (marshal) các tham số đầu vào của hàm thành một định dạng chuẩn để truyền qua mạng.
      - Gửi yêu cầu gọi hàm đến server.
      - Nhận kết quả trả về từ server.
      - Giải gói (unmarshal) kết quả để client có thể sử dụng như bình thường.

  - 2. **Server Stub (Server Proxy)**
    - Server stub nằm trên server, chịu trách nhiệm:

      - Nhận các yêu cầu gọi hàm từ client qua mạng.
      - Giải gói (unmarshal) các tham số truyền tới.
      - Gọi hàm thật trên server với các tham số đó.
      - Gói kết quả trả về để gửi lại cho client.

  - 3. **RPC Runtime (Runtime Library)**
    - Thư viện hỗ trợ RPC trên cả client và server để:

      - Quản lý kết nối mạng, gửi nhận gói tin.
      - Xử lý việc gọi hàm qua mạng.
      - Xử lý các lỗi mạng, lỗi timeout, tái truyền dữ liệu.
      - Đồng bộ và bất đồng bộ khi gọi hàm từ xa.

  - 4. **Binding**
    - Binding giúp client biết được địa chỉ của server (ví dụ IP, port) và các thông tin cần thiết để gọi hàm từ xa.

      - Tĩnh: được cấu hình sẵn.
      - Động: client tìm kiếm server qua dịch vụ đăng ký (naming service).

  - 5. **Marshall/Unmarshall Functions**
    - **Marshalling**: Chuyển đổi tham số của hàm từ dạng nội bộ (cấu trúc dữ liệu trong bộ nhớ) sang dạng chuẩn, có thể truyền qua mạng (ví dụ: chuỗi bytes).

    - **Unmarshalling**: Chuyển đổi dữ liệu nhận được từ mạng trở lại dạng cấu trúc dữ liệu ban đầu để hàm thực thi.

  - 6. **Communication Functions (Gửi/nhận thông điệp)**
    - Gửi các gói tin yêu cầu (request) từ client đến server và nhận gói tin phản hồi (response) từ server về client. Đây có thể là các hàm xử lý socket hoặc giao thức truyền thông khác.

---

## **Câu 18. Định nghĩa tiến trình, thread, multithread client, multithread server.**

  | Khái niệm                | Định nghĩa                                                   | Đặc điểm chính                                      | Lợi ích / Ứng dụng chính                            |
| ------------------------ | ------------------------------------------------------------ | --------------------------------------------------- | --------------------------------------------------- |
| **Tiến trình (Process)** | Chương trình đang chạy, có không gian bộ nhớ riêng           | Không gian bộ nhớ riêng biệt, độc lập               | Quản lý tài nguyên, thực thi chương trình           |
| **Thread (Luồng)**       | Đơn vị thực thi nhỏ nhất trong tiến trình, chia sẻ bộ nhớ    | Chia sẻ bộ nhớ tiến trình, nhẹ hơn tiến trình       | Thực thi song song, tăng hiệu năng trong tiến trình |
| **Multithread Client**   | Client sử dụng nhiều thread để xử lý nhiều tác vụ đồng thời  | Nhiều thread xử lý gửi/nhận hoặc tác vụ song song   | Tăng tốc độ phản hồi, xử lý đa nhiệm client         |
| **Multithread Server**   | Server sử dụng nhiều thread để phục vụ nhiều client cùng lúc | Mỗi kết nối hoặc yêu cầu xử lý bởi một thread riêng | Phục vụ nhiều client đồng thời, tối ưu CPU đa lõi   |

---

## **Câu 19. Review lại kiến thức căn bản của Map, Reduce và mục đích trong một hệ phân tán.**

| Khái niệm    | Định nghĩa và chức năng                                                                                                                                    | Mục đích trong hệ phân tán                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Map**      | Hàm Map nhận một tập dữ liệu đầu vào, chuyển đổi và phân tách thành các cặp (key, value) trung gian. Mỗi phần dữ liệu được xử lý độc lập (song song).      | Phân tán và xử lý dữ liệu lớn đồng thời trên nhiều node khác nhau, giúp tăng tốc xử lý.        |
| **Reduce**   | Hàm Reduce nhận các cặp (key, list\_of\_values) từ Map, gộp và xử lý để tạo ra kết quả cuối cùng.                                                          | Tổng hợp, hợp nhất kết quả từ nhiều node sau khi Map xử lý song song, để thu về kết quả chung. |
| **Mục đích** | Tách bài toán lớn thành các bài toán nhỏ, xử lý song song trên nhiều máy tính trong hệ phân tán, rồi kết hợp kết quả để xử lý dữ liệu quy mô lớn hiệu quả. | Giúp xử lý Big Data, tăng khả năng mở rộng, độ bền, và hiệu suất trong hệ thống phân tán.      |


---

## **Câu 20. Ảo hóa (Virtulization) là gì, mục đích của ảo hóa trong một hệ phân tán dùng để làm gì?**

  - **Định nghĩa**:
    Là kỹ thuật tạo ra một phiên bản ảo của tài nguyên phần cứng hoặc phần mềm (như máy chủ, hệ điều hành, bộ nhớ, mạng) trên một nền tảng vật lý duy nhất.
  
  - **Mục đích**:
    - **Tối ưu sử dụng tài nguyên**: Thay vì dùng nhiều máy vật lý riêng biệt, có thể chạy nhiều máy ảo trên cùng một máy, tận dụng tối đa CPU, RAM, ổ đĩa.

    - **Dễ dàng triển khai, mở rộng**: Có thể nhanh chóng tạo, sao chép hoặc di chuyển máy ảo giữa các máy chủ trong hệ phân tán mà không ảnh hưởng đến hoạt động.

    - **Cách ly và bảo mật**: Mỗi máy ảo hoạt động độc lập, giúp cô lập lỗi hoặc tấn công, tránh ảnh hưởng lan rộng.

    - **Tiết kiệm chi phí**: Giảm số lượng phần cứng cần thiết, tiết kiệm điện năng, không gian và chi phí vận hành.

    - **Hỗ trợ tính linh hoạt và khả năng phục hồi**: Trong hệ phân tán, khi một node gặp sự cố, máy ảo có thể được nhanh chóng chuyển sang node khác.

---

## **Câu 21. Review lại các kiến trúc của server đa luồng.**

| Kiến trúc      | Mô tả chính            | Ưu điểm              | Nhược điểm       | Thích hợp cho                    |
| -------------- | ---------------------- | -------------------- | ---------------- | -------------------------------- |
| **1. Thread per Connection (Luồng trên mỗi kết nối)**              | Mỗi khi có client kết nối, server tạo một thread riêng để xử lý kết nối đó.                                                         | - Đơn giản, dễ lập trình. <br> - Tách biệt xử lý từng client.                  | - Tốn nhiều tài nguyên khi có nhiều client.<br> - Quản lý thread phức tạp khi số lượng lớn. | Số client ít đến vừa, không cần tối ưu tài nguyên. |
| **2. Thread Pool (Nhóm luồng cố định)**                            | Server tạo trước một nhóm thread cố định, khi có kết nối đến thì giao việc cho thread trong pool.                                   | - Tiết kiệm chi phí tạo hủy thread.<br> - Kiểm soát được số lượng thread.      | - Giới hạn số thread, có thể gây nghẽn nếu quá nhiều kết nối.                               | Server cần xử lý số lượng lớn client ổn định.      |
| **3. Event-driven (Sự kiện bất đồng bộ, không dùng nhiều thread)** | Server dùng một hoặc vài thread chính quản lý các sự kiện I/O không đồng bộ, xử lý nhiều kết nối qua callback hoặc reactor pattern. | - Tối ưu tài nguyên, dùng ít thread.<br> - Thích hợp cho I/O-bound.            | - Lập trình phức tạp hơn.<br> - Không tốt cho CPU-bound tasks.                              | Server xử lý lượng lớn kết nối I/O nhiều.          |
| **4. Hybrid (Kết hợp Thread Pool + Event-driven)**                 | Kết hợp thread pool và mô hình sự kiện, dùng thread pool để xử lý các tác vụ nặng, còn I/O bất đồng bộ để nhận và phát sự kiện.     | - Cân bằng giữa tài nguyên và hiệu suất.<br> - Linh hoạt xử lý đa dạng tác vụ. | - Phức tạp trong thiết kế và triển khai.                                                    | Server cần xử lý đa dạng và số lượng lớn client.   |

---

## **Câu 22: Review lại các hướng tiếp cận cài đặt luồng**

| Hướng tiếp cận cài đặt luồng                      | Mô tả chính                                                                         | Ưu điểm                                                                | Nhược điểm                                                                     | Thích hợp cho                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------- |
| **1. Luồng riêng biệt (Dedicated Thread)**        | Mỗi tác vụ hoặc kết nối được xử lý bởi một luồng riêng biệt.                        | - Đơn giản, dễ hiểu, dễ lập trình.                                     | - Tốn nhiều tài nguyên khi số luồng lớn.<br>- Khó mở rộng khi nhiều tác vụ.    | Ứng dụng đơn giản, số luồng ít.               |
| **2. Nhóm luồng (Thread Pool)**                   | Tạo sẵn một nhóm luồng cố định để tái sử dụng cho các tác vụ khác nhau.             | - Tiết kiệm chi phí tạo/destroy luồng.<br>- Kiểm soát số luồng tối đa. | - Giới hạn số lượng tác vụ đồng thời.<br>- Cần thiết kế hợp lý để tránh nghẽn. | Hệ thống cần xử lý nhiều tác vụ ngắn hạn.     |
| **3. Luồng không đồng bộ (Asynchronous Threads)** | Sử dụng callback, future, promise để xử lý tác vụ bất đồng bộ, luồng không bị chặn. | - Tăng hiệu suất, tránh chặn luồng.                                    | - Lập trình phức tạp, khó debug.                                               | Ứng dụng I/O-bound hoặc sự kiện lớn.          |
| **4. Luồng theo sự kiện (Event-driven Threads)**  | Một hoặc vài luồng quản lý tất cả sự kiện theo mô hình reactor hoặc proactor.       | - Tối ưu tài nguyên, phù hợp với lượng lớn kết nối.                    | - Phức tạp, không phù hợp CPU-bound tasks.                                     | Server mạng, xử lý I/O nhiều kết nối.         |
| **5. Luồng theo tác vụ (Task-based Threading)**   | Tách tác vụ ra, luồng chỉ nhận và chạy các task được phân phối.                     | - Quản lý linh hoạt, dễ mở rộng.                                       | - Cần có hệ thống quản lý task hiệu quả.                                       | Hệ thống đa tác vụ, xử lý song song phức tạp. |

---

## **Câu 23. Tại sao chúng ta sử dụng bảng băm phân tán (review slides), mục đích của bảng băm phân tán là gì, Consitent Hashing là gì, Finger table để làm gì, tại sao sử dụng finger table**

| Khái niệm                              | Định nghĩa / Chức năng                                                                                                                                                         | Mục đích / Lợi ích chính                                                                                               |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Bảng băm phân tán (DHT)**            | Là một cấu trúc dữ liệu phân tán dùng để lưu trữ và truy xuất dữ liệu dựa trên khóa (key) trong mạng phân tán, không phụ thuộc vào máy chủ trung tâm.                          | - Cho phép tìm kiếm, lưu trữ dữ liệu hiệu quả trên hệ thống phân tán. <br> - Tăng tính mở rộng và độ bền của hệ thống. |
| **Mục đích của bảng băm phân tán**     | Phân phối đều dữ liệu và trách nhiệm lưu trữ trên các node trong hệ thống, cho phép tra cứu dữ liệu với độ trễ thấp và khả năng mở rộng cao.                                   | - Giảm tải và tránh điểm nghẽn tập trung.<br> - Đảm bảo tính sẵn sàng và khả năng chịu lỗi.                            |
| **Consistent Hashing (Băm nhất quán)** | Thuật toán băm giúp phân phối khóa và node lên một vòng băm ảo, giảm thiểu tối đa việc di chuyển dữ liệu khi node thay đổi (thêm hoặc bớt).                                    | - Giúp cân bằng tải động.<br> - Giảm thiểu số lượng dữ liệu phải di chuyển khi hệ thống mở rộng hoặc thu nhỏ.          |
| **Finger Table**                       | Bảng chỉ mục trên mỗi node trong DHT, lưu thông tin các node ở khoảng cách quyền lực 2 để tăng tốc tra cứu (lookup) các khóa.                                                  | - Giúp giảm độ phức tạp tra cứu từ O(N) xuống O(log N).<br> - Tăng tốc độ định vị node chứa khóa.                      |
| **Tại sao sử dụng Finger Table?**      | Vì mạng phân tán có thể rất lớn, việc tìm kiếm node chứa khóa theo tuyến tính rất chậm. Finger table giúp nhảy nhanh đến các node xa hơn, cải thiện hiệu suất tra cứu đáng kể. | - Tăng tốc độ tra cứu khóa trong mạng phân tán lớn.<br> - Giúp DHT mở rộng tốt và hiệu quả.                            |


---

## **Câu 24. Không gian phẳng là gì, định danh là gì, liệt kê các đặc điểm của không gian phẳng**

  - **1. Không gian phẳng là gì?**
    ![KGP](/images/kgp.png)

  - **2. Định danh (Identifier) là gì?**
    ![Identifier](/images/identifier.png)

  - **3. Đặc điểm chính của không gian phẳng trong hệ phân tán**
  
  | Đặc điểm                                | Giải thích ngắn gọn                                                                       |
| --------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Không có cấu trúc phân cấp**        | Mỗi thực thể có ID riêng biệt, không thuộc nhóm vùng hay lớp nào.                         |
| **Khó xác định vị trí vật lý**        | Không thể biết vị trí địa lý hoặc quan hệ mạng của node dựa vào định danh.                |
| **Thường sử dụng DHT**                | DHT như Chord, Kademlia dùng không gian phẳng để ánh xạ khóa tới node chứa dữ liệu.       |
| **Cần cơ chế tra cứu hiệu quả**       | Vì ID không mang thông tin vị trí, cần thuật toán để tìm đúng node (ví dụ: finger table). |
| **Dễ mở rộng hệ thống**               | Việc thêm/bớt node không làm thay đổi cấu trúc không gian, chỉ cập nhật ánh xạ.           |
| **Tăng tính trừu tượng và linh hoạt** | Node có thể ở bất kỳ đâu, dễ dàng thay đổi hoặc thay thế mà không ảnh hưởng toàn hệ.      |


---

## **Câu 25. Tại sao cần đồng bộ hóa đồng hồ logic, tại sao đồng hồ vật lý không đảm bảo. mục đích của đồng bộ hóa và các thuật toán đồng bộ hóa là gì?**

- Tại sao cần đồng bộ hóa đồng hồ logic trong hệ phân tán?
  - Trong hệ phân tán, mỗi tiến trình chạy trên các máy độc lập, mỗi máy có đồng hồ riêng. Vì vậy:

    - Các tiến trình không chia sẻ chung đồng hồ.
    - Không có đồng hồ toàn cục trong hệ thống.
    - Các tiến trình giao tiếp qua mạng có độ trễ không xác định.

    → Nếu không có đồng bộ, sẽ không thể xác định đúng thứ tự các sự kiện `(ví dụ: ai gửi trước, ai nhận sau)`

- Tại sao đồng hồ vật lý không đủ để đảm bảo trật tự sự kiện?

  | Lý do                                | Giải thích                                                                     |
  | ------------------------------------ | ------------------------------------------------------------------------------ |
  | ❌ **Độ lệch thời gian (clock skew)** | Mỗi máy có tốc độ đồng hồ khác nhau → thời gian trôi không đồng đều.           |
  | ❌ **Không thể đồng bộ tuyệt đối**    | Không có cách nào để đồng bộ hoàn hảo tất cả đồng hồ vật lý trong hệ thống.    |
  | ❌ **Độ trễ mạng biến động**          | Mạng không ổn định, độ trễ khác nhau mỗi lần gửi tin nhắn → sai lệch thứ tự.   |
  | ❌ **Không đảm bảo quan sát thứ tự**  | Một tiến trình A gửi trước nhưng đồng hồ của B lại ghi nhận thời gian nhỏ hơn. |

- Mục đích của đồng bộ hóa đồng hồ `(logical clock synchronization)`

  | Mục đích chính                                   | Giải thích                                                  |
  | ------------------------------------------------ | ----------------------------------------------------------- |
  | ✅ **Xác định quan hệ nhân quả (happens-before)** | Biết được sự kiện nào xảy ra trước/sau.                     |
  | ✅ **Đảm bảo thứ tự sự kiện logic**               | Đảm bảo các tiến trình thấy cùng một thứ tự sự kiện hợp lý. |
  | ✅ **Hỗ trợ ghi log, kiểm tra lỗi**               | Dễ dàng xác định nguyên nhân lỗi hoặc xung đột.             |
  | ✅ **Thống nhất thứ tự cập nhật dữ liệu**         | Trong cơ sở dữ liệu phân tán, giúp duy trì tính nhất quán.  |

- Các thuật toán đồng bộ hóa nổi bật

  | Thuật toán                      | Mục đích chính                           | Cách hoạt động                                                                  | Ghi chú                                                              |
  | ------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
  | **Lamport Clock**               | Đồng bộ thứ tự logic                     | Mỗi sự kiện tăng số đếm, gửi kèm theo khi giao tiếp → max đồng hồ giữa hai bên. | Đơn giản, nhưng không phân biệt các sự kiện độc lập.                 |
  | **Vector Clock**                | Phân biệt nhân quả rõ hơn                | Mỗi tiến trình giữ một mảng vector, ghi nhận thời gian từng tiến trình khác.    | So sánh được cả quan hệ xảy ra đồng thời.                            |
  | **Cristian’s Algorithm**        | Gần với thời gian thực                   | Client gửi yêu cầu đồng bộ đến server có đồng hồ chuẩn.                         | Cần giả định độ trễ mạng đối xứng.                                   |
  | **Berkeley Algorithm**          | Đồng bộ nhiều máy                        | Tính trung bình thời gian từ nhiều máy → cập nhật đồng hồ lại.                  | Không cần đồng hồ chuẩn, nhưng bị ảnh hưởng nếu có máy sai nhiều.    |
  | **NTP (Network Time Protocol)** | Đồng bộ hóa đồng hồ vật lý trên Internet | Phân tầng máy chủ đồng hồ chuẩn, điều chỉnh sai lệch qua nhiều bước.            | Dùng trong thực tế, không hoàn toàn chính xác với độ trễ biến thiên. |

---

## **Câu 26. Đồng hồ Lamport giải quyết vấn đề gì, nêu và giải thích các rules của đồng hồ Lamport**

  - 1. Đồng hồ Lamport giải quyết vấn đề gì?
    - Lamport Clock giải quyết vấn đề xác định thứ tự các sự kiện trong hệ thống phân tán, nơi:

      - Không có đồng hồ toàn cục.

      - Mỗi tiến trình có đồng hồ riêng biệt.

      - Đồng hồ vật lý có thể không đồng bộ, gây khó khăn trong việc xác định "sự kiện nào xảy ra trước".

    → Lamport Clock đảm bảo tính nhân quả `(happens-before relation, ký hiệu là →)` giữa các sự kiện:
      - Nếu một sự kiện **A** xảy ra trước sự kiện **B (A → B)**, thì Lamport Clock phải đảm bảo:
        - **L(A) < L(B)**
      -  Nhưng:
        - **L(A) < L(B)** không có nghĩa là **A → B** (không đủ điều kiện để kết luận nhân quả).

  - 2. Các Quy tắc (Rules) của Đồng hồ Lamport
    - Trong hệ phân tán gồm nhiều tiến trình, mỗi tiến trình có đồng hồ logic C (số nguyên, khởi đầu từ 0).
      
    | Rule   | Tên quy tắc                       | Giải thích chi tiết                                                                                                                                        |
    | ------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **R1** | **Nội bộ (Internal Event)**       | Mỗi khi một tiến trình thực hiện **một sự kiện nội bộ** (ví dụ: tính toán), nó **tăng giá trị đồng hồ của mình lên 1**. <br> → `C := C + 1`                |
    | **R2** | **Gửi tin nhắn (Send Event)**     | Khi một tiến trình **gửi một tin nhắn** đi, nó: <br> - **Tăng đồng hồ lên 1** trước khi gửi: `C := C + 1`<br> - **Đính kèm giá trị đồng hồ vào tin nhắn**. |
    | **R3** | **Nhận tin nhắn (Receive Event)** | Khi một tiến trình nhận được tin nhắn có gắn giá trị thời gian `T` từ người gửi:<br> - **Cập nhật đồng hồ của mình**: <br> `C := max(C, T) + 1`            |


---

## **Câu 27. Tham khảo lại các bài tập của đồng hồ logic Lamport trong slides chương 4-5**

---

## **Câu 28. Giao thức đồng bộ NTP là gì, PTP là gì, được tính toán như thế nào?**

---

## **Câu 29. Review lại python cơ bản**

---