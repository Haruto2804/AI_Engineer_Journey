import numpy as np
from sklearn.model_selection import train_test_split

# 1. TẠO DỮ LIỆU GIẢ LẬP CHO 100 KHÁCH HÀNG
# X: Đặc trưng (ví dụ: [Tuổi, Thu nhập]).
# Tạo 100 dòng dữ liệu, mỗi dòng có 2 cột đặc trưng.
X = np.random.rand(100, 2)

# y: Nhãn (ví dụ: 0 là không mua, 1 là có mua).
# Tạo 100 nhãn tương ứng với 100 khách hàng.
y = np.random.randint(0, 2, 100)
# 2. CHIA DỮ LIỆU
# Cú pháp chia dữ liệu:
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,  # Cắt 20% dữ liệu ra để làm bài Test (80% để Train)
    random_state=42,  # Ghi nhớ cách xáo trộn (để lần sau chạy lại code không bị đổi kết quả)
)

# 3. KIỂM TRA KẾT QUẢ
print(f"Số lượng dữ liệu mang đi dạy (X_train): {len(X_train)}")  # Output: 80
print(f"Số lượng dữ liệu mang đi thi (X_test): {len(X_test)}")  # Output: 20
