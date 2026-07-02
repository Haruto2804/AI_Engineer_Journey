from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import mean_absolute_error

# 1.
# --- DỮ LIỆU GỐC ---
X_cuoc_xe = [
    [2, 0, 0],  # 2km, Giờ bình thường, Trời đẹp
    [2, 1, 1],  # 2km, Giờ cao điểm, Mưa ngập
    [5, 0, 0],  # 5km, Giờ bình thường, Trời đẹp
    [5, 1, 0],  # 5km, Giờ cao điểm, Trời đẹp
    [5, 1, 1],  # 5km, Giờ cao điểm, Mưa ngập
    [10, 0, 0],  # 10km, Giờ bình thường, Trời đẹp
    [10, 1, 0],  # 10km, Giờ cao điểm, Trời đẹp
    [10, 1, 1],  # 10km, Giờ cao điểm, Mưa ngập
]
# Giá tiền tính theo nghìn VNĐ
Y_gia_tien = [25, 70, 60, 95, 150, 120, 180, 280]
ten_cot = ["Khoảng cách", "Giờ cao điểm", "Thời tiết mưa"]
# . Lấy dữ liệu test
X_train, X_test, y_train, y_test = train_test_split(
    X_cuoc_xe, Y_gia_tien, random_state=42, test_size=0.3
)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Tập test", y_test)
print(f"AI dự đoán giá", y_pred)
sai_so = mean_absolute_error(y_test, y_pred)
print(f"Sai số khi AI dự đoán là {sai_so:.2f} VNĐ")
print("----Mức độ ảnh hưởng của các yếu tố----")
for ten, dudoan in zip(ten_cot, model.feature_importances_):
    print(f"- {ten}: {dudoan*100:.2f}%")

# Output:
# - Khoảng cách: 54.27%
# - Giờ cao điểm: 16.43%
# - Thời tiết mưa: 29.30%
# Chào sếp: Dựa trên dữ liện em phân tích, em thấy
# Thời tiết mưa > Giờ cao điểm vì mức độ ảnh hưởng,
# nên lý do chính là do trời mưa ngập nên giá cước xe cao

# 2.
print("Đang đóng gói model AI bằng thư viện joblib....")
ten_file = "lesson17/models/ai_dinh_gia_xride.pkl"
joblib.dump(model, ten_file)
print(f"Đóng gói model thành công tại {ten_file}")

# 3. Bắt đầu dùng thử
ten_file = "lesson17/models/ai_dinh_gia_xride.pkl"
model_dinh_gia_xride = joblib.load(ten_file)
# Du lieu khach hang
khoang_cach = 1090
gio_cao_diem = 1
troi_mua = 1
new_customer = [[khoang_cach, gio_cao_diem, troi_mua]]
cuoc_phi_du_doan = model_dinh_gia_xride.predict(new_customer)
# Đoạn code đã được format lại chuẩn và đẹp
thong_bao = (
    f"💵 Cước phí dự đoán của khách hàng A:\n"
    f"  • Khoảng cách: {khoang_cach} km\n"
    f"  • Thời tiết: {'Trời mưa' if troi_mua == 1 else 'Trời không mưa'}\n"
    f"  • Khung giờ: {'Giờ cao điểm' if gio_cao_diem == 1 else 'Giờ bình thường'}\n"
    f"💰 Tổng chi phí: {cuoc_phi_du_doan[0] * 1000:,.0f} VNĐ"
)
print(thong_bao)
