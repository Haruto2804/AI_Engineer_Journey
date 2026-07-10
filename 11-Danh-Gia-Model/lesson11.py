import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

customer_data = {
    "customer_name": ["Gia Bảo", "Bùi Xuân Huấn", "Haruto", "Khá Bảnh", "Thầy Ông Nội"],
    "online_hours": [1, 100, 20, 70, 50],
    "messages": [100, 40, 70, 150, 90],
}
df_customer = pd.DataFrame(customer_data)
# Đáp án chuẩn
Y_true = [0, 0, 1, 1, 0]
# Lấy kết quả dự đoán:
Y_prec = [0, 1, 1, 1, 1]
# Đo kết quả:
diem_so = accuracy_score(Y_true, Y_prec)
print(f"Kết quả sau khi đo độ chính là: {diem_so*100} %")
