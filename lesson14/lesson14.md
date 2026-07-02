 Từ đầu đến giờ, chúng ta đã dùng thuật toán **Cây quyết định (Decision Tree)**. Nó rất tốt, nhưng có một nhược điểm chí mạng: Nó giống như một vị bác sĩ độc đoán, rất dễ đưa ra quyết định sai lầm nếu gặp một ca bệnh hơi lạ.

Để giải quyết vấn đề này, các nhà khoa học dữ liệu đã tạo ra một thuật toán mạnh mẽ hơn gấp hàng chục lần. 
---

## Bài 14: Random Forest (Rừng ngẫu nhiên) – Sức mạnh của "Trí tuệ tập thể"

### 1. Ý nghĩa: Rừng ngẫu nhiên là gì?

Nguyên lý của Random Forest cực kỳ đơn giản và rất giống với cách con người đưa ra quyết định quan trọng: **Lấy ý kiến số đông (Voting).**

Thay vì chỉ tạo ra **1 Cây quyết định** (1 bác sĩ) để chẩn đoán bệnh, thuật toán Random Forest sẽ tạo ra một **Khu rừng gồm 100 Cây quyết định** (Hội đồng 100 bác sĩ).

* Quá trình huấn luyện: Nó sẽ chia nhỏ dữ liệu ra và dạy cho mỗi Cây một góc nhìn khác nhau về bài toán.
* Quá trình dự đoán: Khi có một bệnh nhân mới bước vào, cả 100 Cây sẽ cùng đưa ra dự đoán. Nếu 80 Cây bảo "Có bệnh", 20 Cây bảo "Khỏe mạnh", hệ thống sẽ chốt kết quả theo số đông: **Có bệnh**.

Nhờ tính chất "trí tuệ tập thể" này, Random Forest cực kỳ ổn định, ít bị học vẹt (Overfitting) và là một trong những thuật toán được sử dụng nhiều nhất trong các công ty công nghệ thực tế.

---

### 2. Thực hành: Thay "Cây" bằng "Rừng" chỉ với 1 dòng code

Điểm tuyệt vời nhất của thư viện **Scikit-Learn** là nó được thiết kế cực kỳ đồng nhất. Bạn không cần phải viết lại toàn bộ quy trình `train_test_split`, `fit`, hay `predict` gì cả. Tất cả những gì bạn cần làm chỉ là **đổi tên bộ não** lúc khởi tạo.

Thay vì gọi Cây Quyết Định:

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

```

Bạn gọi Rừng Ngẫu Nhiên:

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42) 
# n_estimators=100 nghĩa là bạn yêu cầu tạo ra 100 cái cây trong khu rừng này

```

Phần code phía dưới để train (`model.fit()`) và test (`model.predict()`) **hoàn toàn giữ nguyên không sai một chữ!**

---

## Thử Thách Thực Chiến Số 15: AI "Bắt mạch" Khách hàng E-commerce

### Tình huống kinh doanh:

Bạn đang làm việc cho một sàn thương mại điện tử. Phòng Marketing đang lãng phí quá nhiều tiền để rải mã giảm giá (Voucher) cho TẤT CẢ mọi người truy cập. Sếp yêu cầu bạn làm một con AI dự đoán xem một người đang lướt web có khả năng **Chốt đơn (1)** hay **Thoát trang (0)** dựa vào thói quen lướt web của họ.

* Nếu AI dự đoán khách **Chốt đơn (1)** -> Không tặng mã (để tối ưu lợi nhuận vì đằng nào họ cũng mua).
* Nếu AI dự đoán khách **Thoát trang (0)** -> Bắn ngay mã giảm giá để níu chân họ lại.

### Dữ liệu thu thập được:

Dưới đây là lịch sử lướt web của 12 khách hàng, gồm 2 chỉ số: **[Thời gian lướt web (Phút), Số trang sản phẩm đã xem]**.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
# BẠN HÃY TỰ VIẾT DÒNG IMPORT RANDOM FOREST Ở ĐÂY NHÉ!

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Thời gian lướt web (Phút), Số trang đã xem]
X_hanh_vi = [
    [5, 2], [15, 5], [2, 1], [20, 7], 
    [8, 3], [30, 10], [1, 1], [25, 8], 
    [10, 4], [18, 6], [12, 3], [22, 9]
]

# Nhãn: 1 = Chốt đơn (Tự mua), 0 = Thoát trang (Không mua)
Y_mua_hang = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

```

---

### Yêu cầu Thử thách:

1. **Chuẩn bị Vũ khí:** Nhớ import `RandomForestClassifier` từ thư viện `sklearn.ensemble`.
2. **Chia để trị:** Dùng `train_test_split` để chia `X_hanh_vi` và `Y_mua_hang` với tỷ lệ test là **0.3** (lấy 30% dữ liệu đi thi), và dùng `random_state=42`.
3. **Triệu hồi Rừng Ngẫu Nhiên:** Khởi tạo `RandomForestClassifier` với số lượng cây là `n_estimators=100`, nhớ thêm `random_state=42` để kết quả ổn định. Sau đó dạy nó (fit) bằng tập Train và dự đoán (predict) trên tập Test.
4. **Báo cáo kết quả:** In ra `accuracy_score` và `confusion_matrix`.
5. **Phân tích dòng tiền (Nhiệm vụ của Kỹ sư trưởng):** Dựa vào ma trận in ra, bạn hãy comment phân tích 2 rủi ro sau:
* **Báo động giả (FP):** Khách không định mua (0), nhưng AI lại đoán là chắc chắn mua (1) nên KHÔNG phát mã giảm giá. Công ty bị thiệt hại gì ở trường hợp này?
* **Bỏ lọt (FN):** Khách vốn dĩ sẽ tự mua (1), nhưng AI đoán là họ sắp thoát trang (0) nên vội vàng ném cho họ mã giảm giá. Công ty bị thiệt hại gì ở ô này?



Bạn hãy mở IDE lên, xây dựng Khu Rừng Ngẫu Nhiên đầu tiên của mình và dán toàn bộ đoạn code phân tích xuống đây nhé!