from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Lương (Triệu), Số giờ OT/tuần, Điểm hài lòng sếp (1-10)]
X_nhan_su = [
    [15, 20, 4],
    [30, 5, 8],
    [12, 25, 3],
    [40, 0, 9],
    [10, 15, 5],
    [25, 10, 7],
    [14, 22, 2],
    [35, 2, 8],
    [18, 18, 5],
    [20, 8, 6],
    [11, 28, 4],
    [50, 0, 10],
]
# Nhãn: 1 = Đã nộp đơn nghỉ việc, 0 = Vẫn đang cống hiến
Y_nghi_viec = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

ten_cac_cot = ["Mức lương", "Số giờ OT", "Điểm hài lòng Sếp"]
X_train, X_test, y_train, y_test = train_test_split(
    X_nhan_su, Y_nghi_viec, test_size=0.3, random_state=42
)
danh_sach_thong_so = {"n_estimators": [10, 50, 100], "max_depth": [2, 3, None]}
robot = GridSearchCV(
    RandomForestClassifier(random_state=42), param_grid=danh_sach_thong_so, cv=2
)
robot.fit(X_train, y_train)
print(f"Cấu hình tốt nhất là: {robot.best_params_}")
diem_quan_trong = robot.best_estimator_.feature_importances_
print("Tỷ lệ sức nặng của các yếu tố ảnh hưởng đến nghỉ việc:")
for ten, diem in zip(ten_cac_cot, diem_quan_trong):
    print(f"- {ten}: {diem * 100:.2f}%")
# Output:
# - Mức lương: 22.22%
# - Số giờ OT: 33.33%
# - Điểm hài lòng Sếp: 44.44%
# Yếu tố hài lòng Sếp ảnh hưởng cốt lõi. Giám đốc cần quyết định đuổi mấy ông Sếp tồi
