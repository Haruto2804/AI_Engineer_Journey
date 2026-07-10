# BÀI 18: HỒI QUY LOGISTIC - LOGISTIC REGRESSION
[Xem chi tiết nội dung bài học ở đây](https://developers.google.com/machine-learning/crash-course/linear-regression?hl=vi)
### PHẦN 1: Ý NGHĨA (Logistic Regression là gì?)

* **Ẩn dụ thực tế:** Hãy tưởng tượng bạn là một bác sĩ khám bệnh. Nhiệm vụ của bạn là dựa vào nhiệt độ cơ thể của bệnh nhân để quyết định xem họ có bị **Sốt (1)** hay **Khỏe mạnh (0)**.
Nếu dùng một đường thẳng (Hồi quy tuyến tính) để dự đoán, có lúc nó sẽ tính ra kết quả là "bệnh nhân này bị sốt 150%" hoặc "sốt -20%" (điều này thật vô lý!).
Vì vậy, bạn cần một bộ lọc (gọi là hàm **Sigmoid**) để ép mọi kết quả tính toán thô thiển kia phải nằm gọn lỏn trong khoảng từ **0 đến 1** (tương ứng với 0% đến 100% cơ hội bị sốt). Nếu kết quả ra > 50%, bạn phán: "Sốt chắc rồi!".

* **Tại sao AI Engineer cần nó?** Trong thực tế, AI phải đối mặt với hàng tỷ bài toán phân loại nhị phân (chỉ có 2 lựa chọn Đúng/Sai):
* Email này là *Spam* hay *Không Spam*?
* Giao dịch ngân hàng này là *Lừa đảo* hay *Hợp pháp*?
* Khách hàng này sẽ *Gia hạn dịch vụ* hay *Hủy dịch vụ*?
Logistic Regression chính là thuật toán nền tảng, chạy siêu nhanh và cực kỳ hiệu quả để giải quyết các bài toán này trước khi nghĩ tới các mạng Neural phức tạp.



---

### PHẦN 2: THỰC HÀNH (Code chạy ngay xem kết quả)

Chúng ta sẽ dùng thư viện `Scikit-learn` để huấn luyện một AI nhận diện xem một email dựa vào số lượng từ nhạy cảm (như "trúng thưởng", "miễn phí") thì có phải là Spam hay không.

Bạn hãy copy đoạn code Python này vào Google Colab hoặc máy cá nhân để chạy thử:

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

# 1. Dữ liệu mẫu: Số lượng từ "nhạy cảm" trong email
# [1 từ], [2 từ], [3 từ] -> Thường là email bình thường (0)
# [7 từ], [8 từ], [9 từ] -> Thường là email Spam (1)
X = np.array([[1], [2], [3],[7], [8], [9]]) 
y = np.array([0, 0, 0, 1, 1, 1]) # 0: Bình thường, 1: Spam

# 2. Khởi tạo mô hình Hồi quy Logistic và "dạy" nó học từ dữ liệu
model = LogisticRegression()
model.fit(X, y)

# 3. Thử nghiệm xem AI dự đoán email mới thế nào
email_moi_1 = np.array([[1.5]]) # Email chỉ có 1.5 từ nhạy cảm
email_moi_2 = np.array([[8.5]]) # Email có tận 8.5 từ nhạy cảm

print(f"Email 1 (1.5 từ) dự đoán là: {model.predict(email_moi_1)[0]} (0: Thường, 1: Spam)")
print(f"Email 2 (8.5 từ) dự đoán là: {model.predict(email_moi_2)[0]} (0: Thường, 1: Spam)")

# Xem xác suất phần trăm cụ thể mà AI tính toán
probability = model.predict_proba(email_moi_1)
print(f"Xác suất cụ thể của Email 1: {probability[0][0]*100:.2f}% Thường | {probability[0][1]*100:.2f}% Spam")

```

---

### PHẦN 3: THỬ THÁCH NHỎ CHO BẠN

Dựa vào phần ẩn dụ và kết quả code ở trên, bạn hãy trả lời câu hỏi logic sau:

> **Câu hỏi:** Giả sử ta đưa vào một Email mới có chứa **5 từ nhạy cảm** (nằm ngay giữa ranh giới dữ liệu cũ). Nếu AI tính toán ra xác suất Email này là Spam là **51%**, thì theo bạn, mô hình sẽ dán nhãn cuối cùng cho Email này là **0 (Bình thường)** hay **1 (Spam)**? Tại sao?

Bạn hãy đưa ra câu trả lời của mình hoặc gõ đoạn code trên chạy thử rồi phản hồi lại cho tôi nhé. Tôi chờ bạn!