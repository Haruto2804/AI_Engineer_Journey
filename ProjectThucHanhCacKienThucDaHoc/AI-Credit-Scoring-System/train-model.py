import os
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. IMPORT HÀM TỪ DATASET
from dataset import load_credit_data, ten_cot_ngan_hang

# 2. ĐỌC DỮ LIỆU TỪ FILE CSV LÊN RAM THÔNG QUA HÀM
# Hàm load_credit_data() từ dataset.py sẽ trả về 2 mảng lấy từ CSV, ta gán vào đây:
X_ngan_hang, Y_phe_duyet = load_credit_data()

# Lấy dữ liệu test và train
X_train, X_test, y_train, y_test = train_test_split(
    X_ngan_hang, Y_phe_duyet, test_size=0.2, random_state=42
)

# Khởi tạo module
danh_sach_tham_so = {"n_estimators": [10, 50, 100], "max_depth": [2, 3, None]}
model = GridSearchCV(
    RandomForestClassifier(random_state=42, class_weight={0: 3, 1: 1}),
    param_grid=danh_sach_tham_so,
    cv=3,
)

# Giai đoạn train AI dựa trên dữ liệu sẵn có lấy từ CSV:
model.fit(X_train, y_train)
print(f"Tham số tối ưu nhất cho model này là {model.best_params_}")

# Thử test model
y_pred = model.predict(X_test)

# Bắt đầu tính điểm accuracy_score.
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của model là {accuracy*100:.2f}%")

# Dùng Confusion Matrix để test thử coi các trường hợp model dự đoán như nào
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix của model là: \n {cm}")

# Bắt đầu đánh giá các yếu tố ảnh hưởng
best_model = model.best_estimator_
cac_cot_anh_huong = best_model.feature_importances_

print("\n------ MỨC ĐỘ ẢNH HƯỞNG CÁC YẾU TỐ -------")
# Dùng mảng tên cột tính năng (4 cột đầu) để map với mức độ ảnh hưởng
for ten, giatri in zip(ten_cot_ngan_hang[:4], cac_cot_anh_huong):
    print(f" - {ten} ảnh hưởng {giatri*100:.2f}%")


# Bước đóng gói mô hình
def save_model(model, folderName, fileName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)
        print("Đã tạo thư mục thành công!")
    full_url = os.path.join(folderName, fileName)
    try:
        joblib.dump(model, full_url)
        print(f"✅ Đã đóng gói mô hình thành công tại: {full_url}")
    except Exception as e:
        print(f"❌ Thất bại khi đóng gói mô hình. Lỗi: {e}")


# Gọi hàm lưu mô hình vào đúng thư mục 'model' của project
save_model(best_model, "model", "credit_scoring_model.pkl")
