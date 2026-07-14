[Làm bài tập về Feature Cross ở đây](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-cross-exercises)
Trang này là phần **Bài tập thực hành (Feature cross exercises)** sử dụng công cụ trực quan hóa **Tensorflow Playground** của Google.

Vì đây là các bài tập tương tác trực tiếp trên giao diện kéo thả, mình sẽ giải thích nhanh và đưa cho bạn **đáp án/bí kíp cốt lõi** của cả 2 bài tập này để bạn hiểu bản chất cách mô hình vận hành nhé!

---

## 🎯 Bài tập 1: Feature Cross cơ bản (Phân biệt cây bệnh và cây khỏe)

* **Bối cảnh:** Bạn có các chấm cam (cây bệnh) và chấm xanh (cây khỏe) phân bổ chéo nhau ở 4 góc góc phần tư (giống như bàn cờ vua).
* **Các đặc trưng đầu vào có sẵn:**
* $x_1$ (trục ngang)
* $x_2$ (trục dọc)
* $x_1x_2$ (Tổ hợp chéo - Feature Cross của hai trục)



### 💡 Bí kíp giải Task 2:

Nếu bạn chỉ tăng trọng số (weight) của riêng $x_1$ hoặc $x_2$, mô hình chỉ có thể vẽ các đường thẳng chia dọc hoặc chia ngang màn hình $\rightarrow$ **Đoán sai bét nhè (sai 50%)**.

> **Đáp án:** Để phân loại đúng dạng bàn cờ này, bạn phải **đặt trọng số cho cột Feature Cross $x_1x_2$ là một giá trị lớn (ví dụ: `1.0` hoặc `-1.0`)**, còn hai cột đơn lẻ $x_1$ và $x_2$ thì đặt trọng số bằng `0`.
> Lúc này, mô hình sẽ ngay lập tức vẽ được các vùng màu khớp hoàn hảo với vị trí của các cây bệnh và cây khỏe ở 4 góc!

---

## 🎯 Bài tập 2: Feature Cross nâng cao (Dạng vòng tròn đồng tâm)

* **Bối cảnh:** Các chấm xanh (cây khỏe) nằm tụ lại ở một vòng tròn nhỏ ở tâm, còn các chấm cam (cây bệnh) bao bọc xung quanh thành một vòng tròn lớn bên ngoài.
* **Vấn đề của Task 1:** Nếu bạn chỉ dùng các đặc trưng đường thẳng cơ bản như $x_1, x_2$, dù bạn có huấn luyện (train) đến 1000 epochs thì mô hình vẫn không thể vẽ được một "vòng tròn" để bao bọc các chấm xanh. Giá trị **Test loss** (độ sai lệch) sẽ rất cao.

### 💡 Bí kíp giải Task 2 (Đạt Test loss dưới 0.2):

Để mô hình vẽ được một đường ranh giới hình tròn toán học, nó cần các đặc trưng dạng bình phương hoặc tổ hợp tương đương phương trình đường tròn ($x_1^2 + x_2^2 = R^2$).

> **Đáp án để đạt Test loss < 0.2:**
> 1. **Bật (chọn) hai đặc trưng:** $x_1^2$ và $x_2^2$ (đây là các đặc trưng bậc hai giúp tạo độ cong).
> 2. Ấn nút **Run** (chạy huấn luyện). Chỉ sau vài giây (chưa tới 100 epochs), mô hình sẽ tự động vẽ một vòng tròn màu xanh hoàn hảo ở giữa và bao quanh bởi màu cam. Test loss sẽ giảm cực sâu xuống dưới `0.05`!
> 
> 

---

**Tóm lại bài học rút ra từ bài tập:**
Các đặc trưng ban đầu ($x_1, x_2$) chỉ giúp mô hình vẽ được các đường thẳng. Để vẽ được các đường phân chia phức tạp (như hình bàn cờ hay hình tròn), bắt buộc ta phải tạo ra các đặc trưng tổ hợp như **Feature Cross ($x_1x_2$)** hoặc các đặc trưng bậc cao ($x_1^2, x_2^2$).

Bạn đã nắm được tư duy giải quyết 2 dạng bài tập kinh điển này chưa? Chúng ta đi tiếp sang phần test kiến thức (**Test your knowledge**) luôn nhé!