
---

## BÀI 20: ROC_CURVE - AUC 

* **Ẩn dụ thực tế:** Hãy tưởng tượng bạn là một cảnh sát trưởng đang cài đặt độ nhạy cho **máy quét kim loại** ở sân bay.
* Nếu bạn chỉnh máy **quá nhạy** (Ngưỡng thấp): Máy sẽ bắt được *tất cả* súng dao (True Positive), nhưng bù lại, chìa khóa, thắt lưng hay cúc áo cũng làm máy kêu tít tít (False Positive - Bắt nhầm người tốt).
* Nếu bạn chỉnh máy **quá lỏng lẻo** (Ngưỡng cao): Máy sẽ không bao giờ báo động nhầm khi gặp thắt lưng, nhưng bạn lại bỏ sót tội phạm mang vũ khí thật (Lọt lưới).


* **Dưới góc nhìn AI Engineer:** Mô hình phân loại (ví dụ: đoán xem email có phải là Rác không) thường trả về một con số xác suất từ 0% đến 100%. Nhiệm vụ của bạn là chọn ra một **Ngưỡng (Threshold)** (ví dụ: trên 50% là rác).
* **ROC Curve** là một biểu đồ vẽ lại kịch bản: Chuyện gì sẽ xảy ra với tỷ lệ "Bắt trúng" và tỷ lệ "Bắt nhầm" khi bạn **thay đổi cái ngưỡng này từ 0% đến 100%**.


* **AUC (Area Under the Curve):** Là phần diện tích nằm dưới đường cong ROC đó. Diện tích này càng lớn (gần bằng 1), chứng tỏ mô hình của bạn càng thông minh (vừa bắt trúng nhiều, vừa ít bắt nhầm).

---

### PHẦN 2: THỰC HÀNH (Xem ROC hoạt động bằng Code)

Trong thực tế, AI Engineer dùng thư viện `scikit-learn` để tính toán đường cong này chỉ trong vài dòng lệnh. Hãy xem thử nhé:

```python
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score

# Y_that: Kết quả thực tế (1: Bị bệnh, 0: Khỏe mạnh)
y_that = np.array([0, 0, 1, 1])

# Y_doan: Xác suất mà mô hình AI dự đoán (từ 0 đến 1)
y_doan = np.array([0.1, 0.4, 0.35, 0.8])

# 1. Tính điểm AUC (Diện tích dưới đường cong)
auc = roc_auc_score(y_that, y_doan)
print(int("Điểm AUC của mô hình là:", auc))

# 2. Lấy các giá trị để vẽ đường ROC (Tỷ lệ bắt nhầm, Tỷ lệ bắt đúng, và các Ngưỡng)
fpr, tpr, thresholds = roc_curve(y_that, y_doan)

print("\nCác ngưỡng (Thresholds) AI đã thử:", thresholds)
print("Tỷ lệ bắt nhầm (False Positive Rate):", fpr)
print("Tỷ lệ bắt đúng (True Positive Rate):", tpr)

```

---

### PHẦN 3: THỬ THÁCH NHỎ

Nhìn vào kết quả đoạn code trên hoặc logic của máy quét sân bay:

**Câu hỏi dành cho bạn:** Nếu bạn đặt Ngưỡng (Threshold) cực kỳ khắt khe là `1.0` (tức là mô hình phải chắc chắn 100% mới dám kết luận là Bệnh/Rác), thì theo bạn:

1. Tỷ lệ bắt đúng (True Positive Rate) sẽ cao hay thấp?
2. Tỷ lệ bắt nhầm (False Positive Rate) sẽ là bao nhiêu?

*Hãy thử suy luận theo logic thực tế của người vận hành máy quét và trả lời cho tôi biết nhé!*