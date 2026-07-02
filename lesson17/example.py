import joblib
from sklearn.ensemble import RandomForestRegressor

# =========================================================
# PHẦN 1: KỸ SƯ AI HUẤN LUYỆN VÀ ĐÓNG GÓI
# =========================================================
# 1. Dữ liệu gốc
X_o_to = [
    [2020, 5],
    [2018, 8],
    [2023, 1],
    [2015, 12],
    [2021, 3],
    [2017, 10],
    [2022, 2],
    [2019, 7],
]
Y_gia_xe = [500, 350, 800, 200, 650, 300, 750, 420]

# 2. Khởi tạo và Dạy AI (Học trên toàn bộ dữ liệu để AI thông minh nhất)
print("⏳ Đang huấn luyện AI...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_o_to, Y_gia_xe)

# 3. Xuất xưởng: Lưu bộ não ra file cứng
ten_file = "ai_dinh_gia_xe.pkl"
joblib.dump(model, ten_file)
print(f"✅ Đã lưu thành công file '{ten_file}' vào máy tính!\n")


# =========================================================
# PHẦN 2: TÍCH HỢP LÊN WEBSITE (Kỹ sư phần mềm làm)
# (Từ giờ trở đi, bạn KHÔNG cần chạy lại Phần 1 nữa)
# =========================================================
print("--- ỨNG DỤNG ĐỊNH GIÁ XE TỰ ĐỘNG ---")

# 1. Load bộ não từ ổ cứng lên
ai_web = joblib.load(ten_file)

# 2. Giả lập một khách hàng mới vừa nhập thông tin lên Website
nam_san_xuat_khach_nhap = 2019
so_vạn_km_khach_nhap = 4

xe_moi = [[nam_san_xuat_khach_nhap, so_vạn_km_khach_nhap]]

# 3. AI dự đoán ngay lập tức
gia_du_doan = ai_web.predict(xe_moi)

print(
    f"Khách hàng báo bán xe đời {nam_san_xuat_khach_nhap}, đã đi {so_vạn_km_khach_nhap} vạn km."
)
print(f"💰 AI chốt giá thu mua: {gia_du_doan[0]:.2f} Triệu VNĐ")
