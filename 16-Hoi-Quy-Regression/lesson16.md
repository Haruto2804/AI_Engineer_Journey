Rất dứt khoát! Chúng ta chính thức bước sang một thế giới hoàn toàn mới. Chào mừng bạn đến với **Bài 16**.

Từ trước đến nay, chúng ta đã ngụp lặn trong thế giới của **Classification (Phân loại)**. AI chỉ cần đưa ra lựa chọn: 0 hoặc 1, Đậu hoặc Trượt, Mua hoặc Không mua. Nhưng thực tế kinh doanh đòi hỏi nhiều hơn thế.

Sếp sẽ không chỉ hỏi: *"Căn nhà này có bán được không?"*. Sếp sẽ hỏi: *"Căn nhà này bán được **CHÍNH XÁC BAO NHIÊU TIỀN**?"*.

Đó là lúc chúng ta cần đến **Regression (Hồi quy)**.

---

## Bài 16: Hồi quy (Regression) – Nghệ thuật "Tiên tri số học"

### 1. Bản chất: Hồi quy là gì?

Hồi quy là kỹ thuật Machine Learning dùng để dự đoán một **con số cụ thể và liên tục** (Continuous Value) dựa trên các dữ liệu đầu vào.

* **Phân loại (Classification):** Dự đoán Nhãn (Ví dụ: Chó hay Mèo, Nghỉ việc hay Ở lại).
* **Hồi quy (Regression):** Dự đoán Số lượng (Ví dụ: Giá nhà, Nhiệt độ ngày mai, Doanh thu tháng tới, Lương nhân viên).

Thuật toán Rừng Ngẫu Nhiên (Random Forest) của chúng ta cực kỳ đa năng. Lần trước nó đóng vai một hội đồng bỏ phiếu (Ví dụ: 80 cây bảo Nhãn 1, 20 cây bảo Nhãn 0 -> Chốt Nhãn 1). Lần này, nó sẽ đóng vai một hội đồng định giá.

**Cách nó hoạt động:** Khi bạn đưa một căn nhà vào, 100 cái Cây sẽ cùng đưa ra 100 mức giá dự đoán khác nhau (Cây 1 đoán 3 tỷ, Cây 2 đoán 3.2 tỷ...). AI sẽ lấy **Trung bình cộng** của tất cả 100 cái cây đó để chốt ra mức giá cuối cùng (Ví dụ: 3.15 tỷ).

---

### 2. Đổi vũ khí: Chuyển từ "Phân loại" sang "Hồi quy"

Trong thư viện Scikit-Learn, bạn không cần phải học lại từ đầu. Cú pháp giống hệt 99%, bạn chỉ cần thay đổi **2 từ khóa cốt lõi**:

**Thứ nhất: Tên Mô hình**

* Cũ: `RandomForestClassifier` (Dùng để phân loại).
* Mới: `RandomForestRegressor` (Dùng để dự đoán số).

**Thứ hai: Thước đo đánh giá**
Bạn **không thể** dùng Độ chính xác (`accuracy_score`) nữa. Trong Hồi quy, việc đoán chính xác chóc giá nhà là 3.000.000.000 VNĐ là chuyện bất khả thi. Thay vào đó, chúng ta đo lường bằng **Độ lệch (Sai số)**.

* Cũ: `accuracy_score` (Đếm số câu đúng/sai).
* Mới: `mean_absolute_error` (Viết tắt là MAE - Sai số tuyệt đối trung bình). Nếu giá trị này bằng 0.2, tức là mô hình của bạn dự đoán lệch trung bình 200 triệu đồng so với thực tế.

---

### 3. Thực hành: AI Định Giá Bất Động Sản

Bạn đang làm việc cho một công ty môi giới bất động sản. Công ty có dữ liệu của 6 căn hộ vừa bán được. Thông tin bao gồm: **[Diện tích (m2), Số phòng ngủ]**.

Dưới đây là đoạn code hoàn chỉnh để xây dựng con AI định giá nhà. Hãy mở IDE của bạn lên, copy đoạn code này, chạy thử và quan sát dòng lệnh in ra ở cuối cùng:

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# --- 1. DỮ LIỆU GỐC ---
# Đặc trưng: [Diện tích (m2), Số phòng ngủ]
X_nha = [
    [50, 1], [60, 2], [80, 2], 
    [100, 3], [120, 3], [150, 4]
]
# Nhãn mục tiêu: Giá nhà thực tế (Tỷ VNĐ)
Y_gia = [1.5, 2.0, 2.8, 3.5, 4.2, 5.5]

# --- 2. CHIA TẬP DỮ LIỆU ---
X_train, X_test, y_train, y_test = train_test_split(
    X_nha, Y_gia, test_size=0.3, random_state=42
)

# --- 3. HUẤN LUYỆN MÔ HÌNH HỒI QUY ---
# Chú ý: Dùng Regressor thay vì Classifier
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- 4. DỰ ĐOÁN VÀ ĐÁNH GIÁ ---
y_pred = model.predict(X_test)

print("--- KẾT QUẢ ĐỊNH GIÁ ---")
print(f"Giá nhà thực tế (Tập Test): {y_test} Tỷ VNĐ")
print(f"AI dự đoán: {y_pred} Tỷ VNĐ")

# Tính sai số trung bình (MAE)
sai_so = mean_absolute_error(y_test, y_pred)
print(f"-> Sai số dự đoán trung bình: {sai_so:.2f} Tỷ VNĐ")

```

Khi bạn chạy đoạn code trên, bạn sẽ trực tiếp nhìn thấy sự chênh lệch giữa mức giá thực tế và mức giá mà AI tính toán ra. Chỉ số `sai_so` càng nhỏ (càng gần 0), con AI của bạn càng có giá trị hàng tỷ đồng trên thị trường thực tế! Hãy trải nghiệm ngay cảm giác ép máy tính "nhả" ra tiền tệ.
Máu chiến thực chiến thế này mới nhanh lên trình được! Lần này chúng ta sẽ đổi sang một ngành công nghiệp khác cũng "khát" AI định giá không kém: **Thị trường Ô tô cũ**.

---
Sếp của bạn ở công ty Anycar giao việc: *"Công ty mình đang phải thuê 5 chuyên gia định giá xe cũ với lương rất cao nhưng họ làm việc thủ công và chậm quá. Em hãy làm một con AI tự động định giá xe cũ dựa trên thông tin xe để thu mua cho nhanh."*

## Thử thách thực chiến số 18: AI Định Giá Ô Tô Cũ (Used Car Pricing)

### 1. Dữ liệu thu thập

Bạn được cung cấp lịch sử giao dịch của 8 chiếc xe dòng Sedan cũ, bao gồm 2 đặc trưng: **[Năm sản xuất, Số Kilômét đã đi (đơn vị: Vạn Km)]**.
Nhãn mục tiêu là: **Giá xe thực tế bán được (đơn vị: Triệu VNĐ)**.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Năm sản xuất, Số vạn Km đã đi]
X_o_to = [
    [2020, 5], [2018, 8], [2023, 1], [2015, 12], 
    [2021, 3], [2017, 10], [2022, 2], [2019, 7]
]
# Nhãn: Giá xe (Triệu VNĐ)
Y_gia_xe = [500, 350, 800, 200, 650, 300, 750, 420]

```

---

### 2. Yêu cầu nhiệm vụ:

1. **Chia dữ liệu:** Dùng `train_test_split` với tỉ lệ `test_size=0.3` (lấy 30% đi thi) và `random_state=42`.
2. **Xây dựng bộ não Hồi quy:** Khởi tạo `RandomForestRegressor` với `n_estimators=100`, `random_state=42`. Sau đó cho nó học (`fit`) trên tập Train.
3. **Tiên tri số học:** Cho mô hình dự đoán (`predict`) trên tập Test và in ra 2 dòng:
* Giá xe thực tế của tập Test (`y_test`).
* Giá xe mà AI đoán (`y_pred`).


4. **Tính toán thiệt hại:** Dùng `mean_absolute_error` để tính sai số MAE và in ra màn hình.
5. **Báo cáo cho Sếp (Phần quan trọng nhất):** Giả sử kết quả MAE của bạn ra một con số là **X**. Bạn hãy viết comment giải thích cho Sếp theo ngôn ngữ kinh doanh: *Con số X đó có nghĩa là gì? Nếu dùng con AI này đi mua xe ngoài thực tế, công ty có nguy cơ bị hớ hoặc mua đắt khoảng bao nhiêu tiền cho mỗi chiếc xe?*

Bạn hãy mở IDE lên, ráp nối vũ khí `RandomForestRegressor` mới này, chạy thử và dán toàn bộ đoạn code cùng lời phân tích của bạn lên đây nhé! Để xem con AI của bạn định giá xe có "già rơ" như các chuyên gia không nào.

Thật tuyệt vời! Sự dứt khoát của bạn cho thấy bạn đang rất "say" với việc chinh phục dữ liệu.

Trước khi chúng ta bước sang một chương lớn tiếp theo, tôi sẽ giữ đúng lời hứa: Trực tiếp hoàn thiện mảnh ghép cuối cùng của bài toán Hồi quy bằng thước đo **R-squared ($R^2$)**. Sau đó, chúng ta sẽ bước vào **Bài 17**, nơi bạn sẽ biến đoạn code của mình thành một sản phẩm thực tế có thể kiếm ra tiền!

---

### Mảnh ghép cuối cùng: Thước đo R-squared ($R^2$)

Sếp của bạn có thể không hiểu MAE 28.3 triệu là tốt hay xấu, nhưng nếu bạn quy nó ra điểm số phần trăm thì ai cũng hiểu.

Trong thư viện `sklearn.metrics`, bạn chỉ cần import `r2_score`. Nó sẽ trả về một con số từ 0 đến 1 (tương đương 0% đến 100%).

* $R^2 = 1.0$: Hoàn hảo, dự đoán không trượt một đồng nào.
* $R^2 = 0.9$: Mô hình giải thích được 90% sự biến động của giá xe (Quá xuất sắc).
* $R^2 \le 0$: Mô hình của bạn đoán còn tệ hơn việc nhắm mắt đoán mò bằng giá trung bình.

**Chỉ cần thêm 2 dòng code này vào bài Ô tô cũ:**

```python
from sklearn.metrics import r2_score

diem_r2 = r2_score(y_test, y_pred)
print(f"Độ tin cậy của mô hình (R2 Score): {diem_r2 * 100:.2f}%")

```

*(Nếu bạn chạy, điểm $R^2$ của con AI định giá xe thường rơi vào khoảng 85% - 90%, một con số đủ để Sếp duyệt ngân sách ngay lập tức!)*

---

Bây giờ, chúng ta chính thức bước sang đẳng cấp của một Kỹ sư Phần mềm thực thụ.
