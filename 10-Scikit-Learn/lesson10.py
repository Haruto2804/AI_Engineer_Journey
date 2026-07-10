from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import accuracy_score

# Khách hàng A: Online 3 giờ/tuần, gửi 15 tin nhắn.
# Khách hàng B: Online 25 giờ/tuần, gửi 200 tin nhắn.
# Dữ liệu gốc
new_customers = [[3, 15], [25, 200]]
is_premium_train = [0, 1]
# Khởi tạo model
model = DecisionTreeClassifier()
# Huấn luyện dựa trên dữ liệu đã có
model.fit(new_customers, is_premium_train)
# Huấn luyện xong, giờ ta cần dữ liệu sạch để test
customer_data = {
    "customer_name": ["Gia Bảo", "Bùi Xuân Huấn", "Haruto", "Khá Bảnh", "Thầy Ông Nội"],
    "online_hours": [1, 100, 20, 70, 50],
    "messages": [100, 40, 70, 150, 90],
}
df_customer = pd.DataFrame(customer_data)
x_new = df_customer[["online_hours", "messages"]]
df_customer["bought_premium"] = model.predict(x_new)
print(df_customer)
# Lưu ý: customer_data: càng đa dạng càng chính xác thì tỉ lệ dự đoán càng cao! vì customer_data chỉ có dữ liệu của
# 2 khách hàng nên kết quả dự đoán chưa thật sự chính xác
