import numpy as np
from sklearn.linear_model import LogisticRegression

# 1. Dữ liệu mẫu: Số lượng từ "nhạy cảm" trong email
# [1 từ], [2 từ], [3 từ] -> Thường là email bình thường (0)
# [7 từ], [8 từ], [9 từ] -> Thường là email Spam (1)
X = np.array([[1], [2], [3], [7], [8], [9]])
y = np.array([0, 0, 0, 1, 1, 1])  # 0: Bình thường, 1: Spam

# 2. Khởi tạo mô hình Hồi quy Logistic và "dạy" nó học từ dữ liệu
model = LogisticRegression()
model.fit(X, y)

# 3. Thử nghiệm xem AI dự đoán email mới thế nào
email_moi_1 = np.array([[1.5]])  # Email chỉ có 1.5 từ nhạy cảm
email_moi_2 = np.array([[8.5]])  # Email có tận 8.5 từ nhạy cảm
email_moi_5 = np.array([[5]])  # Email có tận 5 từ nhạy cảm

print(
    f"Email 1 (1.5 từ) dự đoán là: {model.predict(email_moi_1)[0]} (0: Thường, 1: Spam)"
)
print(
    f"Email 2 (8.5 từ) dự đoán là: {model.predict(email_moi_2)[0]} (0: Thường, 1: Spam)"
)
print(
    f"Email 2 (5 từ) dự đoán là: {model.predict(email_moi_5)[0]} (0: Thường, 1: Spam)"
)

# Xem xác suất phần trăm cụ thể mà AI tính toán
probability = model.predict_proba(email_moi_5)
print(
    f"Xác suất cụ thể của Email 1: {probability[0][0]*100:.2f}% Thường | {probability[0][1]*100:.2f}% Spam"
)
# Như bạn thấy ở kết quả chạy thực tế, xác suất máy tính ra sẽ xấp xỉ 50% Bình thường | 50% Spam (Nếu in số thập phân chi tiết, nó sẽ cỡ 49.9999% Thường và 50.0001% Spam).

# Vì 50.0001% > 50%, AI sẽ chốt luôn kết quả cuối cùng là 1 (Spam). Khái niệm này gọi là Ngưỡng quyết định (Decision Threshold). Máy học mặc định lấy mốc 50% làm ranh giới.
