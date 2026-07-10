from sklearn.tree import DecisionTreeClassifier

# 1. CHUẨN BỊ DỮ LIỆU
# Mỗi danh sách con là [Số giờ online, Số tin nhắn] của 4 người dùng cũ
X_train = [
    [2, 10],  # Người 1: Ít online, ít nhắn tin
    [20, 150],  # Người 2: Online nhiều, nhắn tin nhiều
    [5, 20],  # Người 3: Ít online, ít nhắn
    [18, 120],  # Người 4: Online nhiều, nhắn nhiều
]
# Nhãn tương ứng: 0 là Free, 1 là Premium
y_train = [0, 1, 0, 1]
# 2. KHỞI TẠO VÀ DẠY (TRAIN) MODEL
model = DecisionTreeClassifier()
# Gọi thuật toán Cây Quyết Định
model.fit(X_train, y_train)
# Hàm fit() chính là lúc AI học quy luật
# 3. AI DỰ ĐOÁN NGƯỜI DÙNG MỚI
# Có một người dùng mới: Online 19 giờ, gửi 130 tin nhắn
new_user = [[19, 130]]
prediction = model.predict(new_user)
print(f"AI dự đoán khách hàng này thuộc nhóm (0: Free, 1: Premium): {prediction}")
