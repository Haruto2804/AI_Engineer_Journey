from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# --- DỮ LIỆU GỐC ---
# [Thu nhập (Triệu VNĐ), Điểm tín dụng]
X_khach_hang = [
    [15, 600],
    [8, 400],
    [30, 750],
    [22, 680],
    [10, 500],
    [5, 350],
    [50, 800],
    [40, 720],
    [12, 550],
    [18, 620],
    [25, 710],
    [9, 450],
]
# Nhãn tương ứng: 1 = Duyệt cho vay, 0 = Từ chối (Vì nợ xấu)
Y_quyet_dinh = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
# Chia để trị: Dùng train_test_split để chia X_khach_hang và Y_quyet_dinh với tỷ lệ test là 0.25 (tức là 25% mang đi thi) và random_state=42.
X_train, X_test, y_train, y_test = train_test_split(
    X_khach_hang,
    Y_quyet_dinh,
    test_size=0.25,
    random_state=42,
)
# Huấn luyện: Khởi tạo DecisionTreeClassifier() và dạy nó bằng tập Train.
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
# Dự đoán: Dự đoán trên tập Test và lưu kết quả vào biến y_pred.
y_pred = model.predict(X_test)
# Đánh giá: Tính độ chính xác (accuracy) bằng accuracy_score(y_test, y_pred) và in ra kết quả.
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")
# Tạo ma trận nhầm lẫn (confusion matrix) bằng confusion_matrix(y_test, y_pred) và in ra kết quả.
cm = confusion_matrix(y_test, y_pred)
print("Ma trận nhầm lẫn:")
print(cm)
# [[TN, FP],
# [FN, TP]]
# TN = 0: N: Không duyệt cho vay, T: Thực tế không được duyệt cho vay. (Ngon luôn mô hình dự đoán đúng)
# FP = 1: P: Duyệt cho vay, F: Thực tế không được duyệt cho vay. -> AI dự đoán sai, tin tưởng khách hàng này sẽ trả nợ nhưng thực tế là không. (Báo động giả)
# FN = 0: N: Không duyệt cho vay, F: Thực tế được duyệt cho vay. -> AI dự đoán sai, tin tưởng khách hàng này sẽ không trả nợ nhưng thực tế là có. (Bỏ lọt) -> Mất đi khách hàng tiềm năng
# TP = 2: P: Duyệt cho vay, T: Thực tế được duyệt cho vay. -> AI dự đoán đúng, tin tưởng khách hàng này sẽ trả nợ và thực tế là có. (Ngon luôn mô hình dự đoán đúng)
