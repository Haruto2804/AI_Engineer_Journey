from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Bước 1: Liệt kê các phụ tùng muốn Robot thử nghiệm (Viết dưới dạng Dictionary)
danh_sach_thong_so = {
    "n_estimators": [50, 100, 200],  # Yêu cầu thử 3 mức số cây
    "max_depth": [3, 5, None],  # Yêu cầu thử 3 mức độ cao
}

# Bước 2: Tạo con Robot
robot = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),  # Đưa cái xe gốc vào
    param_grid=danh_sach_thong_so,  # Đưa giỏ phụ tùng vào
    cv=3,  # Tham số an toàn: Yêu cầu robot test chéo 3 lần cho mỗi tổ hợp để lấy trung bình
)

# Bước 3: Giao dữ liệu và ngồi uống cà phê chờ nó chạy
# robot.fit(X_train, y_train)

# In ra cấu hình ngon nhất sau khi chạy xong
# print("Cấu hình đỉnh nhất:", robot.best_params_)
