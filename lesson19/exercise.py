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
lap_trinh_vien = pd.DataFrame({"Tuoi": [28], "Luong_trieu_VND": [35]})
du_doan = model.predict(lap_trinh_vien)
xac_suat = model.predict_proba(lap_trinh_vien)
print("--- KẾT QUẢ AI DỰ ĐOÁN ---")
print(
    f"Kết quả dự đoán anh lập trình viên 28 tuổi lương 35tr/tháng: Chọn mua: {du_doan}, Tỉ lệ mua: {xac_suat[0][1]*100:.2f}%"
)
