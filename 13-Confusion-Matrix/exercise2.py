from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Tuổi, Huyết áp]
X_benh_nhan = [
    [45, 120],
    [60, 150],
    [50, 110],
    [65, 160],
    [35, 115],
    [70, 140],
    [40, 125],
    [55, 145],
    [48, 130],
    [80, 170],
]

# Nhãn: 1 = Có bệnh tim (Cấp cứu), 0 = Khỏe mạnh (Cho về)
Y_benh_an = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X_benh_nhan, Y_benh_an, test_size=0.4, random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")
cm = confusion_matrix(y_test, y_pred)
print("Ma trận nhầm lẫn:")
print(cm)
# [[TN, FP],
# [FN, TP]]
# TN = 0: N: AI đoán không có bệnh, T: Đúng với thực tế. --> Ngon luôn AI đoán k có bệnh
# FP = 1: P: AI doán có bệnh, F: Thực tế không có bệnh. --> Báo động giả
# FN = 0: N: AI đoán không có bệnh, F: Thực tế có bệnh. --> Bỏ lọt --> Người bệnh về nhà tưởng mình khỏe mạnh --> Nguy hiểm
# TP = 1: P: AI đoán có bệnh, T: Thực tế có bệnh. --> Ngon luôn AI đoán có bệnh
