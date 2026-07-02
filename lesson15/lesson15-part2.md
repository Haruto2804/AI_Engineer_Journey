

---

## Bài 15 - Part 2: GridSearchCV – Con Robot Thợ Máy Tối Ưu Tự Động

### 1. Ý nghĩa: Tại sao chúng ta cần một "Con Robot"?

Như chúng ta vừa phân tích, để con AI Rừng Ngẫu Nhiên đạt đỉnh cao, bạn phải tìm ra tổ hợp ngon nhất giữa 2 núm vặn:

* `n_estimators` (Số lượng cây): Thử 50, 100, 200...
* `max_depth` (Chiều cao tối đa): Thử 3, 5, 10...

Nếu bạn làm thủ công (vặn tay, chạy code, ghi lại điểm số ra giấy, rồi lại vặn tiếp...), bạn sẽ mất cả thanh xuân. Nếu bạn có 3 núm vặn, mỗi núm có 5 mức, bạn phải chạy code $5 \times 5 \times 5 = 125$ lần!

**Giải pháp:** Thư viện Scikit-Learn đã chế tạo sẵn một "Con Robot" mang tên `GridSearchCV` (Lưới tìm kiếm). Nhiệm vụ của nó là: Bạn chỉ cần quăng cho nó cái xe (Mô hình gốc) và một giỏ phụ tùng (Danh sách thông số), nó sẽ tự động thay lắp, chạy thử tất cả các vòng đua, và cuối cùng báo cáo lại cho bạn đúng một dòng: *"Cấu hình mạnh nhất là cái này!"*

### 2. Thực hành: Cú pháp triệu hồi Robot

Quy trình giao việc cho GridSearchCV chỉ gồm 3 bước cực kỳ thanh lịch:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Bước 1: Liệt kê các phụ tùng muốn Robot thử nghiệm (Viết dưới dạng Dictionary)
danh_sach_thong_so = {
    'n_estimators': [50, 100, 200], # Yêu cầu thử 3 mức số cây
    'max_depth': [3, 5, None]       # Yêu cầu thử 3 mức độ cao
}

# Bước 2: Tạo con Robot
robot = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42), # Đưa cái xe gốc vào
    param_grid=danh_sach_thong_so,                     # Đưa giỏ phụ tùng vào
    cv=3 # Tham số an toàn: Yêu cầu robot test chéo 3 lần cho mỗi tổ hợp để lấy trung bình
)

# Bước 3: Giao dữ liệu và ngồi uống cà phê chờ nó chạy
# robot.fit(X_train, y_train)

# In ra cấu hình ngon nhất sau khi chạy xong
# print("Cấu hình đỉnh nhất:", robot.best_params_)

```

---

### 3. Thử thách thực chiến số 16: Cứu vãn Người dùng Ứng dụng (Churn Prediction)

**Tình huống kinh doanh:** Bạn làm cho một công ty phát hành App Điện thoại. Gần đây, rất nhiều khách hàng VIP đột ngột gỡ cài đặt (Churn). Sếp giao cho bạn dữ liệu của 15 người dùng, gồm 2 chỉ số: **[Số ngày đăng nhập trong tháng, Số lần gọi tổng đài phàn nàn]**.

* Nhãn **1**: Đã gỡ App (Khách bỏ đi).
* Nhãn **0**: Vẫn đang dùng (Khách trung thành).

Sếp yêu cầu bạn xây dựng một con AI Random Forest để phát hiện ra khách sắp gỡ App, nhưng **bắt buộc phải dùng GridSearchCV** để tìm ra thông số tối ưu nhất.

**Dữ liệu gốc (Bạn hãy copy vào IDE):**

```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- DỮ LIỆU ---
# Đặc trưng: [Số ngày đăng nhập, Số lần phàn nàn]
X_khach_hang = [
    [30, 0], [2, 5], [25, 1], [5, 4], [28, 0], 
    [3, 3], [10, 6], [29, 2], [1, 7], [22, 1],
    [4, 4], [26, 0], [15, 5], [20, 2], [6, 3]
]
# Nhãn: 1 = Gỡ App, 0 = Vẫn dùng
Y_roi_bo = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]

```

**Yêu cầu Thử thách:**

1. Dùng `train_test_split` chia dữ liệu ra với `test_size=0.3`, `random_state=42`.
2. Tạo cái giỏ `param_grid` thử nghiệm 2 núm vặn:
* `n_estimators`: Thử `[10, 50, 100]`
* `max_depth`: Thử `[2, 4, None]`


3. Tạo con `robot = GridSearchCV(...)` như cú pháp ở trên và dạy nó bằng tập Train (`robot.fit`).
4. In ra cấu hình xịn nhất bằng lệnh: `print("Cấu hình tốt nhất:", robot.best_params_)`.
5. Bắt con robot đó dự đoán trên tập Test: `y_pred = robot.predict(X_test)` và in ra độ chính xác (`accuracy_score`).

Bạn hãy mở trình soạn thảo, hoàn thiện đoạn code "độ xe" này và dán kết quả lên đây nhé! Chạy xong đoạn code này, bạn chính thức thăng cấp lên Kỹ sư Tối ưu hóa Mô hình rồi đấy!