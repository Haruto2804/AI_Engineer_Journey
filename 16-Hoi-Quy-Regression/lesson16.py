from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Năm sản xuất, Số vạn Km đã đi]
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
# Nhãn: Giá xe (Triệu VNĐ)
Y_gia_xe = [500, 350, 800, 200, 650, 300, 750, 420]

# 1.
X_train, X_test, y_train, y_test = train_test_split(
    X_o_to, Y_gia_xe, test_size=0.3, random_state=42
)
# 2.
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# 3.
y_pred = model.predict(X_test)
print(f"Giá xe thực tế của tập Test: ", y_test)
print(f"Giá xe AI dự đoán {y_pred}")
# 4.
sai_so = mean_absolute_error(y_test, y_pred)
print(f"-> Sai số dự đoán trung bình: {sai_so:.2f} Triệu VNĐ")
# 5.
# Thưa sếp, kết quả sai số MAE là 28.30. Điều này có nghĩa
# là mức giá mà AI đưa ra sẽ lệch (cao hơn hoặc thấp hơn)
# trung bình khoảng 28.3 triệu VNĐ so với giá trị thực tế
# của chiếc xe trên thị trường. Nếu dùng AI này để đi thu
# mua ngay lúc này, công ty có rủi ro mua đắt hoặc báo giá
# hớ khoảng 28 triệu
# cho mỗi chiếc xe

# 6.
diem_r2 = r2_score(y_test, y_pred)
print(f"Độ tin cậy của mô hình (R2 Score): {diem_r2 * 100:.2f}%")
