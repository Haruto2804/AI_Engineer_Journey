Bài học này đi sâu vào **L2 Regularization** (Điều chuẩn L2) - công thức toán học phổ biến nhất để thực hiện việc "phạt" mô hình mà chúng ta đã bàn ở bài trước.

Dưới đây là những điểm cốt lõi bạn cần nắm bắt để hiểu cách L2 hoạt động:

### 1. Cách L2 Regularization "phạt" mô hình

Độ phức tạp của một mô hình được quyết định bởi các "trọng số" (weights). Trọng số càng lớn, mô hình càng phụ thuộc nhiều vào một tính năng cụ thể nào đó.

Thuật toán L2 tính toán độ phức tạp bằng cách **bình phương tất cả các trọng số rồi cộng lại với nhau**:


$$L_2 = w_1^2 + w_2^2 + ... + w_n^2$$

**Hiệu ứng vô cùng đặc biệt của L2:**

* **Trừng phạt nặng sự cực đoan:** Vì sử dụng phép bình phương, những trọng số lớn sẽ tạo ra điểm phạt khổng lồ. Ví dụ: Trọng số $5.0$ sẽ tạo ra điểm phạt lên tới $25.0$ (chiếm 93% tổng độ phức tạp trong ví dụ của tài liệu).
* **Tha thứ cho sự nhỏ bé:** Những trọng số nhỏ (gần 0) khi bình phương lên sẽ càng nhỏ hơn, gần như không bị phạt.
* **Không bao giờ triệt tiêu:** L2 ép các trọng số tiến sát về $0$ để giảm tầm ảnh hưởng của chúng, nhưng nó **không bao giờ gán thẳng bằng 0**. Điều này có nghĩa là L2 không xóa bỏ hoàn toàn bất kỳ tính năng nào khỏi mô hình.

### 2. Lambda ($\lambda$) - Nút vặn mức độ phạt

Bạn đã biết công thức lý tưởng là:


$$Minimize(Loss + Complexity)$$

Tuy nhiên, trong thực tế, các kỹ sư cần một "nút vặn" để điều chỉnh xem họ muốn ưu tiên giảm Loss hay ưu tiên giảm Complexity. Nút vặn đó chính là **Tỷ lệ điều chuẩn (Regularization rate)**, ký hiệu là $\lambda$ (Lambda):


$$Minimize(Loss + \lambda \times Complexity)$$

* **Lambda CAO (Kỷ luật thép):** Phạt rất nặng độ phức tạp. Các trọng số bị ép chặt về $0$. Đồ thị trọng số sẽ chụm lại thành hình quả chuông hẹp (Normal distribution). Mô hình đơn giản, chống Overfitting rất tốt (nhưng cẩn thận bị Underfitting vì quá đơn giản).
* **Lambda THẤP (Kỷ luật lỏng):** Phạt nhẹ. Các trọng số tự do chạy lung tung và phình to. Đồ thị trọng số trải phẳng lì. Mô hình dễ bị Overfitting.
* **Nếu Lambda = 0:** Tính năng Regularization bị tắt hoàn toàn.

### 3. Giải pháp "Tắt bếp sớm" (Early Stopping)

Nếu việc tìm kiếm nút vặn Lambda quá rắc rối, có một "mẹo" khác để chống Overfitting gọi là **Early Stopping**.

Hãy nhớ lại biểu đồ Generalization Curve ở bài trước. Khi đường Validation bắt đầu ngóc đầu đi lên (dấu hiệu của học vẹt), thay vì dùng toán học để phạt, bạn đơn giản là **ấn nút STOP**, dừng hẳn việc huấn luyện lại ngay tại điểm đó.

* *Ưu điểm:* Nhanh, dễ làm.
* *Nhược điểm:* Ít khi tạo ra một mô hình hoàn hảo bằng cách chịu khó ngồi tinh chỉnh chỉ số Lambda.

### 4. Cuộc kéo co giữa Learning Rate và Lambda

Trong quá trình huấn luyện, hai thông số này luôn kéo mô hình về hai hướng trái ngược nhau:

* **Learning Rate (Tốc độ học):** Có xu hướng kéo các trọng số ra xa số 0 để mô hình học các điểm mới.
* **Lambda ($\lambda$):** Kéo các trọng số về gần số 0 để giữ mô hình đơn giản.

Nhiệm vụ của người kỹ sư là phải tìm ra điểm cân bằng hoàn hảo giữa hai thế lực này. Nếu thay đổi Learning Rate, bạn gần như chắc chắn sẽ phải dò lại giá trị Lambda từ đầu.
---
## Nội dung cốt lỗi cần nắm cho AI Engineer:

### 1. Ý nghĩa thực tế: L2 là "Bộ còng tay" chống thiên vị

* **Không cần nhớ công thức:** Bạn chỉ cần hiểu L2 sinh ra để ngăn mô hình AI trở nên "cuồng" hoặc phụ thuộc quá mức vào 1-2 tính năng cụ thể.
* *Ví dụ:* Khi đánh giá giá nhà, nếu không có L2, AI có thể bị thiên vị và gán trọng số khổng lồ cho số lượng nhà vệ sinh, dẫn đến đoán sai bét. L2 sẽ nhảy vào "còng tay" cái trọng số đó lại, ép AI phải đánh giá cân bằng cả diện tích, vị trí, năm xây dựng...

### 2. Cách xài "Nút vặn" Lambda ($\lambda$) khi code

Sau này khi bạn gọi các thư viện Machine Learning (như `scikit-learn` hay `TensorFlow`), hàm code của nó sẽ luôn bắt bạn điền một con số (thường tên là `lambda`, `alpha` hoặc `C`). Bạn chỉ cần nhớ thần chú:

* **Mô hình đang học vẹt (Test điểm thấp, Train điểm cao):** $\rightarrow$ Bạn **TĂNG** Lambda lên để phạt nó bớt học vẹt lại.
* **Mô hình đang học dốt (Test thấp, Train cũng thấp):** $\rightarrow$ Do bạn phạt nặng quá, hãy **GIẢM** Lambda xuống để cởi trói cho nó thông minh hơn.

### 3. Mẹo thực chiến: Early Stopping (Tắt bếp sớm)

* **Cái này xài cực nhiều:** Khi huấn luyện các mô hình lớn (đặc biệt là Neural Networks), thay vì phải dò dẫm con số Lambda mất thời gian, các lập trình viên thường viết một đoạn code cài tự động: *"Cứ vẽ đồ thị ra, hễ thấy đường Validation ngóc đầu đi lên (chuẩn bị overfit) là ngắt điện, dừng chương trình ngay lập tức!"*.
* Đây là cách "ăn gian" cực kỳ hiệu quả mà bạn sẽ dùng rất nhiều sau này.

**Tóm gọn lại bằng 1 câu:** Khi AI bị Overfitting, hãy bật L2 lên, dò nút vặn Lambda cho đến khi nó hết học vẹt; hoặc lười quá thì cứ viết code cài chế độ "Tắt bếp sớm" (Early Stopping). Chỉ cần nhớ vậy là đủ xài rồi!