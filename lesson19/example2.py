import pandas as pd
from sklearn.linear_model import LogisticRegression

# 1. Tạo tập dữ liệu lịch sử khách hàng (Giả lập)
data = {
    "Tuoi": [22, 25, 47, 52, 46, 27, 33, 40],
    "Luong_trieu_VND": [10, 15, 60, 80, 55, 20, 25, 45],
    "Mua_xe": [0, 0, 1, 1, 1, 0, 0, 1],  # 0: Không mua, 1: Có mua
}
df = pd.DataFrame(data)

print("--- BẢNG DỮ LIỆU LỊCH SỬ ---")
print(df)
print("-" * 30)

# Chia tính năng (X) và nhãn (y)
X_train = df[["Tuoi", "Luong_trieu_VND"]]
y_train = df["Mua_xe"]

# 2. Khởi tạo và Huấn luyện AI
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Ứng dụng thực tế: Dự đoán khách hàng mới
# Khách A: Sinh viên mới ra trường
# Khách B: Quản lý cấp trung
khach_hang_moi = pd.DataFrame({"Tuoi": [23, 42], "Luong_trieu_VND": [12, 50]})

du_doan = model.predict(khach_hang_moi)
xac_suat = model.predict_proba(khach_hang_moi)

print("--- KẾT QUẢ AI DỰ ĐOÁN ---")
print(
    f"Khách A (23 tuổi, 12tr): Dự đoán = {du_doan[0]} | Tỉ lệ mua = {xac_suat[0][1]*100:.1f}%"
)
print(
    f"Khách B (42 tuổi, 50tr): Dự đoán = {du_doan[1]} | Tỉ lệ mua = {xac_suat[1][1]*100:.1f}%"
)
