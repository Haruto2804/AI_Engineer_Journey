from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 3. Thử thách thực chiến số 16: Cứu vãn Người dùng Ứng dụng (Churn Prediction)
# --- DỮ LIỆU ---
# Đặc trưng: [Số ngày đăng nhập, Số lần phàn nàn]
X_khach_hang = [
    [30, 0],
    [2, 5],
    [25, 1],
    [5, 4],
    [28, 0],
    [3, 3],
    [10, 6],
    [29, 2],
    [1, 7],
    [22, 1],
    [4, 4],
    [26, 0],
    [15, 5],
    [20, 2],
    [6, 3],
]
# Nhãn: 1 = Gỡ App, 0 = Vẫn dùng
Y_roi_bo = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X_khach_hang, Y_roi_bo, test_size=0.3, random_state=42
)
danh_sach_thong_so = {"n_estimators": [10, 50, 100], "max_depth": [2, 4, None]}
robot = GridSearchCV(
    RandomForestClassifier(random_state=42), param_grid=danh_sach_thong_so, cv=2
)
robot.fit(X_train, y_train)
print("Cấu hình tốt nhất:", robot.best_params_)
y_pred = robot.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của robot là {accuracy*100}%")
print("Nhãn thực tế (y_test): ", y_test)
print(robot.best_estimator_.feature_importances_)
