# Lần này, chúng ta sẽ làm một quy trình chuẩn từ A đến Z, không bỏ sót bước nào.

# Giả sử bạn có dữ liệu của 10 khách hàng (gồm số giờ online và số tin nhắn) cùng với đáp án thực tế xem họ có mua Premium hay không.

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# --- BƯỚC 1: DỮ LIỆU GỐC ---
X_tong = [
    [1, 10],
    [2, 15],
    [20, 100],
    [25, 120],
    [5, 20],
    [18, 90],
    [3, 10],
    [22, 110],
    [6, 30],
    [30, 150],
]
Y_tong = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]
# (Nhìn bằng mắt ta thấy quy luật: Cứ số to là 1, số nhỏ là 0)
# 1. Dùng train_test_split để chia X_tong và Y_tong thành 4 biến (X_train, X_test, y_train, y_test) với tỷ lệ test là 0.3 (30%), và random_state=42.
X_train, X_test, y_train, y_test = train_test_split(
    X_tong, Y_tong, test_size=0.3, random_state=42
)
# Khởi tạo DecisionTreeClassifier() và dạy nó (fit) bằng tập Train (X_train và y_train).
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
# Dự đoán (predict) trên tập Test (X_test) và lưu kết quả vào biến y_pred.
y_pred = model.predict(X_test)
# Tính độ chính xác (accuracy) bằng accuracy_score(y_test, y_pred) và in ra kết quả.
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")
