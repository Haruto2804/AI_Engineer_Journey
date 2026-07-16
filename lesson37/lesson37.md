## Bài 37: Model Complexity
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/model-complexity)

### 1. Triết lý "Dao cạo Ockham" (Occam's Razor)

Trong khoa học nói chung và Machine Learning nói riêng, có một nguyên tắc gọi là *Occam's Razor*: **Nếu có nhiều cách giải thích cho một vấn đề, cách đơn giản nhất thường là cách đúng nhất.**

* **Mô hình phức tạp:** Giống như việc vẽ những đường cong ngoằn ngoèo, méo mó để cố gắng khoanh vùng chính xác 100% từng điểm dữ liệu trong tập Training. Kết quả là nó bị Overfitting. Nó thi điểm tuyệt đối ở phòng thí nghiệm nhưng lại trượt vỏ chuối khi ra thực tế.
* **Mô hình đơn giản:** Thay vì vẽ đường cong phức tạp, bạn chỉ dùng một **đường thẳng** để chia cắt dữ liệu. Mặc dù đường thẳng này có thể đoán sai một vài điểm trong tập Training, nhưng nó nắm bắt được xu hướng chung rất tốt và hoạt động cực kỳ ổn định trên tập Test (dữ liệu mới).

> **Quy tắc ngầm:** Mô hình phức tạp thường cho kết quả tốt hơn trên tập Train, nhưng mô hình đơn giản lại chiến thắng trên tập Test (vốn là thước đo quan trọng nhất). Do đó, khi chọn tính năng (features) cho AI, hãy ưu tiên chọn một số ít các tính năng có sức mạnh dự đoán cao nhất thay vì "nhét" mọi thứ vào.

### 2. Sự xung đột giữa Độ lỗi (Loss) và Độ phức tạp (Complexity)

Từ đầu khóa học, chúng ta luôn mặc định mục tiêu duy nhất của AI là làm sao để điểm lỗi (Loss) càng thấp càng tốt:


$$Minimize(Loss)$$

Nhưng nếu chỉ chăm chăm giảm Loss, mô hình sẽ tự động trở nên khổng lồ và phức tạp để học thuộc lòng dữ liệu, dẫn đến Overfitting. Sự thật là Loss và Độ phức tạp tỷ lệ nghịch với nhau:

* Độ phức tạp tăng $\rightarrow$ Loss (trên tập Train) giảm.
* Độ phức tạp giảm $\rightarrow$ Loss (trên tập Train) tăng.

Do đó, thuật toán tối ưu thực sự trong Machine Learning phải cân bằng được cả hai yếu tố này. Mục tiêu huấn luyện chuẩn xác phải là:


$$Minimize(Loss + Complexity)$$


Nghĩa là: Mô hình phải đoán đúng nhất có thể, nhưng bằng cách **đơn giản nhất có thể**.

### 3. Regularization: Kỹ thuật ép mô hình "sống tối giản"

Làm sao để bắt một cỗ máy AI phức tạp tự động trở nên đơn giản hơn? Các kỹ sư sử dụng một khái niệm gọi là **Regularization** (Điều chuẩn/Chuẩn hóa).

Tài liệu đưa ra một ví dụ ẩn dụ rất hay:
Hãy tưởng tượng AI là một ông giáo sư thích giảng bài bằng những thuật ngữ toán học siêu phức tạp. Bạn (người huấn luyện) phát cho mỗi sinh viên một cái còi. Cứ khi nào giáo sư giảng quá lằng nhằng, sinh viên sẽ thổi còi báo lỗi. Để không bị thổi còi, giáo sư buộc phải **tự phạt mình** bằng cách dùng từ ngữ bình dân hơn, giải thích ngắn gọn hơn.

Trong Machine Learning, Regularization chính là "tiếng còi" đó. Nó là một hình phạt (penalty) được cộng thẳng vào hàm Loss mỗi khi mô hình có dấu hiệu phình to và trở nên quá phức tạp. Nhờ bị phạt liên tục trong lúc huấn luyện, AI sẽ tự động cắt tỉa bớt những liên kết không cần thiết và giữ lại một bộ khung đơn giản, gọn gàng nhất để giải bài toán.