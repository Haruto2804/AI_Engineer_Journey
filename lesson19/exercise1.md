

---

### PHẦN 1: Ý NGHĨA (Bài toán: Dự đoán khách hàng mua xe hơi)

* **Tình huống:** Bạn đang làm việc cho một Showroom ô tô. Giám đốc Marketing đưa cho bạn một tập dữ liệu lịch sử khách hàng gồm 2 thông tin chính: **Tuổi** và **Lương tháng (triệu VNĐ)**.
* **Nhiệm vụ của AI Engineer:** Xây dựng một con AI Hồi quy Logistic. Khi có một khách hàng mới bước vào hoặc đăng ký thông tin trên web, AI phải dự đoán ngay xem người này có khả năng **Mua xe (1)** hay **Không mua (0)**.
* **Lợi ích thực tế:** Nếu AI đoán khách này tiềm năng (xác suất mua cao), đội sale sẽ dồn lực chăm sóc tận răng. Nếu AI báo không tiềm năng, sale sẽ bỏ qua để đỡ tốn thời gian. Đây là bài toán *Lead Scoring* (chấm điểm khách hàng tiềm năng) ra tiền thật ở mọi công ty!

---

### PHẦN 2: THỰC HÀNH (Chạy ngay kịch bản thực tế)

Lần này chúng ta sẽ dùng thêm `Pandas` - một thư viện mà AI Engineer nào cũng phải xài hàng ngày để tạo bảng dữ liệu (như Excel). Bạn hãy copy đoạn code này và chạy nhé:

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression

# 1. Tạo tập dữ liệu lịch sử khách hàng (Giả lập)
data = {
    'Tuoi': [22, 25, 47, 52, 46, 27, 33, 40],
    'Luong_trieu_VND': [10, 15, 60, 80, 55, 20, 25, 45],
    'Mua_xe': [0, 0, 1, 1, 1, 0, 0, 1]  # 0: Không mua, 1: Có mua
}
df = pd.DataFrame(data)

print("--- BẢNG DỮ LIỆU LỊCH SỬ ---")
print(df)
print("-" * 30)

# Chia tính năng (X) và nhãn (y)
X_train = df[['Tuoi', 'Luong_trieu_VND']]
y_train = df['Mua_xe']

# 2. Khởi tạo và Huấn luyện AI
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Ứng dụng thực tế: Dự đoán khách hàng mới
# Khách A: Sinh viên mới ra trường
# Khách B: Quản lý cấp trung
khach_hang_moi = pd.DataFrame({
    'Tuoi': [23, 42], 
    'Luong_trieu_VND': [12, 50]
})

du_doan = model.predict(khach_hang_moi)
xac_suat = model.predict_proba(khach_hang_moi)

print("--- KẾT QUẢ AI DỰ ĐOÁN ---")
print(f"Khách A (23 tuổi, 12tr): Dự đoán = {du_doan[0]} | Tỉ lệ mua = {xac_suat[0][1]*100:.1f}%")
print(f"Khách B (42 tuổi, 50tr): Dự đoán = {du_doan[1]} | Tỉ lệ mua = {xac_suat[1][1]*100:.1f}%")

```

---

### PHẦN 3: THỬ THÁCH NHỎ CHO BẠN

Bây giờ bạn đã có một cỗ máy AI kiếm tiền thực thụ có thể dự đoán dựa trên Tuổi và Lương. Dựa vào đoạn code trên, hãy giúp tôi giải quyết tình huống sau từ Giám đốc Marketing:

> **Nhiệm vụ:** Hôm nay có một anh lập trình viên đến xem xe. Anh này mới **28 tuổi** nhưng lương khá cao: **35 triệu/tháng**.
> Bạn hãy sửa code ở `Phần 3 (Khách hàng mới)` để AI dự đoán xem anh lập trình viên này có khả năng mua xe hay không? Tỉ lệ phần trăm mua xe cụ thể là bao nhiêu? Hãy chạy thử và báo lại kết quả cho tôi nhé!