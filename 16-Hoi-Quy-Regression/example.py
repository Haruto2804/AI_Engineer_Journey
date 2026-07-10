from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# --- 1. DỮ LIỆU GỐC ---
# Đặc trưng: [Diện tích (m2), Số phòng ngủ]
X_nha = [[50, 1], [60, 2], [80, 2], [100, 3], [120, 3], [150, 4]]
# Nhãn mục tiêu: Giá nhà thực tế (Tỷ VNĐ)
Y_gia = [1.5, 2.0, 2.8, 3.5, 4.2, 5.5]

# --- 2. CHIA TẬP DỮ LIỆU ---
X_train, X_test, y_train, y_test = train_test_split(
    X_nha, Y_gia, test_size=0.3, random_state=42
)

# --- 3. HUẤN LUYỆN MÔ HÌNH HỒI QUY ---
# Chú ý: Dùng Regressor thay vì Classifier
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- 4. DỰ ĐOÁN VÀ ĐÁNH GIÁ ---
y_pred = model.predict(X_test)

print("--- KẾT QUẢ ĐỊNH GIÁ ---")
print(f"Giá nhà thực tế (Tập Test): {y_test} Tỷ VNĐ")
print(f"AI dự đoán: {y_pred} Tỷ VNĐ")

# Tính sai số trung bình (MAE)
sai_so = mean_absolute_error(y_test, y_pred)
print(f"-> Sai số dự đoán trung bình: {sai_so:.2f} Tỷ VNĐ")
