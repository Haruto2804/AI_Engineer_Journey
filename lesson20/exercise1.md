Được luôn! Mình sẽ đóng vai Trưởng khoa Sản nhi của bệnh viện. Dưới đây là bài toán thực tế lâm sàng cùng toàn bộ dữ liệu mẫu (đã được chuyển thành dạng số) để bạn đưa thẳng vào code.

---

### 📋 Tình huống thực tế: Dự đoán nguy cơ Sinh non (Preterm Birth)

Bạn được giao một bộ dữ liệu gồm **8 sản phụ**. Mô hình AI phân tích dữ liệu siêu âm và xét nghiệm máu để trả về **Xác suất sinh non (từ 0 đến 1)**.

Nhiệm vụ của bạn là chạy code ROC-AUC với dữ liệu này để tìm ra **ngưỡng (threshold)** phù hợp nhất. Mục tiêu trong sản khoa: **Tuyệt đối không được bỏ sót ca sinh non nào** (tức là muốn $TPR = 1.0$), nhưng cũng không được báo động nhầm quá nhiều làm sản phụ hoang mang.

---

### 📊 Dữ liệu đầu vào (Bạn nạp thẳng vào code)

* **Kết quả thực tế từ bác sĩ (`y_that`):** `[0, 0, 1, 0, 1, 1, 0, 1]`
*(Trong đó: 1 = Sinh non, 0 = Sinh đủ tháng)*
* **Xác suất AI dự đoán (`y_doan`):** `[0.15, 0.2, 0.4, 0.55, 0.6, 0.75, 0.3, 0.85]`

---

### 🛠️ Nhiệm vụ của bạn

Bạn hãy chạy đoạn code dưới đây trên máy của mình:

```python
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score

# Nạp dữ liệu thực tế từ bài toán
y_that = np.array([0, 0, 1, 0, 1, 1, 0, 1])
y_doan = np.array([0.15, 0.2, 0.4, 0.55, 0.6, 0.75, 0.3, 0.85])

# Tính toán
auc = roc_auc_score(y_that, y_doan)
fpr, tpr, thresholds = roc_curve(y_that, y_doan)

# In kết quả
print(f"Điểm AUC của mô hình: {auc:.2f}")
print("\nCác ngưỡng (Thresholds) đã thử:", thresholds)
print("Tỷ lệ bắt nhầm (FPR):", fpr)
print("Tỷ lệ bắt đúng (TPR):", tpr)

```

### ❓ Câu hỏi thực tế dành cho bạn:

Sau khi chạy và nhìn thấy các mảng kết quả hiện ra trên màn hình:

1. Bạn thấy điểm **AUC** của mô hình này có cao không? (Mô hình tốt hay tệ?)
2. Dựa trên mảng `thresholds`, `fpr`, và `tpr` kết quả, bạn sẽ khuyên Bệnh viện chọn **Ngưỡng (Threshold) nào** để vừa **bắt được 100% ca sinh non** ($TPR = 1.0$) mà lại có **tỷ lệ báo động nhầm ($FPR$) thấp nhất**?

Bạn chạy code rồi cho mình biết kết quả bạn chọn nhé!