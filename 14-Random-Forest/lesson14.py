from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Thời gian lướt web (Phút), Số trang đã xem]
X_hanh_vi = [
    [5, 2],
    [15, 5],
    [2, 1],
    [20, 7],
    [8, 3],
    [30, 10],
    [1, 1],
    [25, 8],
    [10, 4],
    [18, 6],
    [12, 3],
    [22, 9],
]
# Nhãn: 1 = Chốt đơn (Tự mua), 0 = Thoát trang (Không mua)
Y_mua_hang = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X_hanh_vi, Y_mua_hang, test_size=0.3, random_state=42
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của model là {accuracy*100}%")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# Output:
# [3 0]
# [0 1]
# Phân tíchL
# TN = 3 --> N: AI dự đoán thoát trang (không mua ), T: AI dự đoán đúng với thực tế -> AI đoán đúng
# TP = 1 --> P: AI dự đoán khách sẽ chốt đơn, T: AI dự đoán đúng với thực tế --> AI dự đoán đúng
# FP = 0 --> P: AI dự đoán khách sẽ chốt đơn,
# T: Thực tế đây là khách vãng lai --> AI tưởng khách chốt đơn
# nên không gửi mã giảm giá --> Khách hàng mất tiêu, biết đâu khi gửi
# mã giảm giá thì khách hàng sẽ chốt đơn? --> Bỏ lỡ khách hàng tiềm năng
# FN = 0 --> N: AI dự đoán khách sẽ thoát trang (không mua),
# T: Thực tế điều này sai khách sẽ chốt đơn --> Khiến công ty bị lỗ nặng
# và được hời cho người mua
