# Process And Flow

## **1.** Dựa vào bài học, check CPU, GPU, RAM, giải thích về hiệu năng của máy tính mà em đang dùng?

### 🧠 CPU:
- **Lõi (Core)**:
  - Mỗi lõi là một đơn vị xử lý độc lập có thể thực hiện các tác vụ riêng biệt.
  - Nhiều lõi giúp thực hiện song song nhiều tác vụ (đa nhiệm tốt hơn).

- **Luồng (Thread)**:
  - Luồng là đơn vị nhỏ hơn lõi, được tạo ra nhờ công nghệ siêu phân luồng (Hyper-Threading) của Intel hoặc SMT của AMD.
  - Mỗi lõi vật lý có thể xử lý 2 luồng, giúp tận dụng tài nguyên lõi hiệu quả hơn.

- **Xung nhịp (Clock Speed)**:
  - Xung nhịp càng cao → xử lý đơn luồng càng nhanh.
  - Ảnh hưởng lớn đến game, ứng dụng phản hồi thời gian thực, và các tác vụ đơn luồng.

---

### 🎮 GPU:
- **Nhân xử lý đồ họa (CUDA Cores / Stream Processors)**:
  - Giúp GPU xử lý dữ liệu hình ảnh và các tác vụ song song như game, đồ họa, AI.

- **Xung nhịp GPU (GPU Clock)**:
  - Tốc độ xử lý của GPU, ảnh hưởng đến hiệu năng khi chơi game hoặc dựng video.

- **VRAM (Video RAM)**:
  - Bộ nhớ đồ họa chuyên dụng để lưu hình ảnh, texture, mô hình 3D,...
  - Dung lượng lớn hơn giúp chạy tốt các phần mềm thiết kế hoặc game nặng.

- **Hỗ trợ công nghệ**:
  - Ray Tracing, DLSS (NVIDIA), FidelityFX (AMD), CUDA (AI), v.v. giúp tăng chất lượng hình ảnh và hiệu suất.

---

### 💾 RAM:
- **Dung lượng**:
  - RAM càng nhiều → càng tốt cho đa nhiệm, mở nhiều ứng dụng cùng lúc.
  - 8GB: tạm đủ cho văn phòng; 16GB: tốt cho học tập, game; 32GB+: cho đồ họa, lập trình, mô phỏng.

- **Tốc độ (MHz)**:
  - RAM nhanh hơn giúp tăng tốc độ truy xuất dữ liệu, cải thiện hiệu năng hệ thống.

- **Loại RAM**:
  - DDR3 (cũ), DDR4 (phổ biến), DDR5 (mới, nhanh hơn).

---

### 🔍 Đánh giá hiệu năng tổng thể:

- [Máy 1: Trần Bá Minh Đức](#máy-1)
- [Máy 2: Đồng Đạo Minh	Dũng](#máy-2)

### Máy 1
- **CPU: Intel Core i5-12500H (12 lõi / 16 luồng, 2.50GHz)** → Rất mạnh mẽ cho hầu hết tác vụ
- **GPU: Intel Iris Xe / NVIDIA Geoforce RTX 3050 Laptop GPU** → Dùng tốt cho đồ họa tầm trung, chơi game ở mức cao.
- **RAM: 16GB DDR4** → Phù hợp với đa nhiệm trung, có thể nâng cấp thêm nếu có nhu cầu đa nhiệm cao hơn.

💡 *Kết luận*: Máy của em phù hợp cho học tập và làm việc ở mức trung bình tới cao.

### Máy 2
- **CPU: Intel Core i5-12500H (12 lõi / 16 luồng, 2.50GHz)** → Rất mạnh mẽ cho hầu hết tác vụ
- **GPU: Intel Iris Xe / NVIDIA Geoforce RTX 3050 Laptop GPU** → Dùng tốt cho đồ họa tầm trung, chơi game ở mức cao.
- **RAM: 16GB DDR4** → Phù hợp với đa nhiệm trung, có thể nâng cấp thêm nếu có nhu cầu đa nhiệm cao hơn.

💡 *Kết luận*: Máy của em phù hợp cho học tập và làm việc ở mức trung bình tới cao.

---

 ## **2.** Các bài toán phổ biến và ứng dụng đa luồng / đa tiến trình

 ### 🔄 Phân biệt: 
    > Đa luồng (Multithreading): Tốt cho xử lý song song nhẹ, chia sẻ bộ nhớ, hiệu quả với CPU đa lõi.
 
    > Đa tiến trình (Multiprocessing): Tốt cho xử lý độc lập, tránh lỗi treo toàn bộ chương trình nếu một phần lỗi.

 | **STT** | **Bài toán / Ứng dụng**                              | **Sử dụng đa luồng / đa tiến trình ở đâu?**                                        |
| ------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1     | **Web Server (Xử lý nhiều yêu cầu HTTP)**            | Mỗi kết nối khách hàng có thể dùng 1 luồng hoặc 1 tiến trình riêng.                |
| 2     | **Tìm kiếm văn bản (Text Search Engine)**            | Chia nhỏ tập dữ liệu và tìm song song trên nhiều luồng/tiến trình.                 |
| 3     | **Xử lý ảnh / video (Image/Video Processing)**       | Áp dụng hiệu ứng, chuyển đổi màu, resize từng phần ảnh/video song song.            |
| 4     | **Dự đoán bằng mô hình AI / Machine Learning**       | Training sử dụng đa tiến trình để xử lý batch dữ liệu; inference chia ra đa luồng. |
| 5     | **Nén và giải nén dữ liệu (Compression)**            | Chia file thành các phần nhỏ, xử lý song song.                                     |
| 6     | **Biên dịch mã nguồn (Compilers)**                   | Biên dịch các file độc lập hoặc phân tích mã nguồn song song.                      |
| 7     | **Phân tích dữ liệu lớn (Big Data Analytics)**       | Chạy song song trên Spark / Hadoop bằng đa tiến trình phân tán.                    |
| 8     | **Game Engine (Xử lý vật lý, AI, đồ họa, âm thanh)** | Mỗi thành phần (vật lý, AI, âm thanh, input) có thể chạy trên luồng riêng.         |
| 9     | **Trình duyệt web (Web Browsers)**                   | Mỗi tab hoặc plugin chạy trên tiến trình riêng, rendering và JS xử lý đa luồng.    |
| 10      | **Phát hiện virus / malware (Antivirus Engine)**     | Quét từng file trong hệ thống song song bằng nhiều luồng.                          |
| 11  | **Phần mềm dựng phim, render 3D**                    | Render mỗi khung hình hoặc pixel bằng nhiều luồng hoặc GPU threads.                |
| 12  | **Cơ sở dữ liệu (Database Engines)**                 | Mỗi truy vấn có thể là 1 luồng, xử lý đọc/ghi song song để tăng tốc độ phản hồi.   |

---

## **3.** Viết ra giấy rồi chụp ảnh, liệt kê các trường hợp nào thì nên dùng thread, trường hợp nào nên dùng process, khi nào thì nên dùng cả hai. Viết dưới dạng table và đưa ví dụ các bài toán

![Place Holder1](static/images/b3.jpg)
---

## **4:** Report – Tìm hiểu ChatGPT training tập dữ liệu lớn bằng Distributed System như thế nào

---

### 🧠 Tổng quan

ChatGPT là một mô hình ngôn ngữ lớn (Large Language Model – LLM) được huấn luyện trên tập dữ liệu khổng lồ với hàng trăm tỷ token. Để huấn luyện mô hình có quy mô như vậy, OpenAI sử dụng hệ thống phân tán (distributed system) nhằm:

- Tối ưu hiệu suất tính toán
- Tăng tốc độ huấn luyện
- Quản lý bộ nhớ hiệu quả
- Tận dụng tài nguyên GPU/TPU cao cấp

---

### ⚙️ Các phương pháp hệ thống phân tán trong huấn luyện ChatGPT

#### 1. **Song song dữ liệu (Data Parallelism)**
- Sao chép toàn bộ mô hình trên nhiều GPU.
- Chia nhỏ dữ liệu thành từng lô (batch) cho mỗi GPU xử lý độc lập.
- Kết quả được tổng hợp lại sau mỗi bước huấn luyện.

#### 2. **Song song mô hình (Model Parallelism)**
- Mô hình quá lớn không thể chứa trong một GPU → chia mô hình thành nhiều phần.
- Mỗi phần mô hình chạy trên một GPU khác nhau.
- Giúp tận dụng tối đa bộ nhớ GPU.

#### 3. **Song song pipeline (Pipeline Parallelism)**
- Chia quá trình huấn luyện thành các giai đoạn (stages).
- Mỗi GPU xử lý một giai đoạn khác nhau theo kiểu "dây chuyền".

#### 4. **Kết hợp song song đa tầng (Hybrid Parallelism)**
- Kết hợp data, model, và pipeline parallelism.
- Giúp tối ưu hóa cho các mô hình cực lớn như GPT-3 hoặc GPT-4.

---

### 🧰 Công cụ và nền tảng hỗ trợ

| Công cụ         | Vai trò chính |
|----------------|---------------|
| **DeepSpeed**  | Tối ưu hóa huấn luyện mô hình lớn, hỗ trợ memory-efficient training |
| **Ray**        | Nền tảng tính toán phân tán mạnh mẽ, dùng cho cả training và inference |
| **Horovod**    | Framework phổ biến hỗ trợ song song dữ liệu trong TensorFlow / PyTorch |
| **TPU/GPU clusters** | Hạ tầng phần cứng với mạng tốc độ cao và hàng ngàn GPU |

---

### 🏗️ Hạ tầng phần cứng

- Sử dụng hàng **nghìn GPU A100 / TPUv4** trong các trung tâm dữ liệu.
- Hệ thống **mạng InfiniBand / NVLink** tốc độ cao giữa các GPU.
- **Bộ nhớ đệm phân tán** để giảm độ trễ truyền dữ liệu.

---

### 📚 Nguồn tài liệu tham khảo

1. [How ChatGPT and our foundation models are developed – OpenAI](https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-foundation-models-are-developed)

2. [How Ray, a Distributed AI Framework, Helps Power ChatGPT – The New Stack](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/)

3. [DeepSpeed-Chat: RLHF training of ChatGPT-like models – arXiv](https://arxiv.org/abs/2308.01320)

4. [How ChatGPT System Design Works – Educative.io](https://www.educative.io/blog/how-chatgpt-system-design-works)

---

### ✅ Kết luận

Việc huấn luyện ChatGPT là một quá trình rất phức tạp và đòi hỏi hệ thống phân tán ở cấp độ siêu máy tính. Nhờ sự kết hợp của các kỹ thuật phân tán tiên tiến và hạ tầng mạnh mẽ, OpenAI có thể huấn luyện những mô hình có hàng trăm tỷ tham số một cách hiệu quả và tối ưu.
