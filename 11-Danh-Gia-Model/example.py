from sklearn.metrics import accuracy_score

# 1. Đáp án thực tế (Sự thật mà chúng ta đã biết)
# Ví dụ: Thực tế 3 khách hàng này có mua Premium hay không?
y_true = [1, 0, 1]
# 2. Đáp án do AI dự đoán ra
y_pred = [1, 1, 1]  # AI đoán sai người thứ 2
diem_so = accuracy_score(y_true, y_pred)
print(f"Độ chính xác của mô hình là: {diem_so * 100}%")
# Output: Độ chính xác của mô hình là: 66.66666666666666%
