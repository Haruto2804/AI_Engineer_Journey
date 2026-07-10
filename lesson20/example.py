import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score

# Y_that: Kết quả thực tế (1: Bị bệnh, 0: Khỏe mạnh)
y_that = np.array([0, 0, 1, 1])

# Y_doan: Xác suất mà mô hình AI dự đoán (từ 0 đến 1)
y_doan = np.array([0.1, 0.4, 0.35, 0.8])

# 1. Tính điểm AUC (Diện tích dưới đường cong)
auc = roc_auc_score(y_that, y_doan)
print("Điểm AUC của mô hình là:", auc)

# 2. Lấy các giá trị để vẽ đường ROC (Tỷ lệ bắt nhầm, Tỷ lệ bắt đúng, và các Ngưỡng)
fpr, tpr, thresholds = roc_curve(y_that, y_doan)

print("\nCác ngưỡng (Thresholds) AI đã thử:", thresholds)
print("Tỷ lệ bắt nhầm (False Positive Rate):", fpr)
print("Tỷ lệ bắt đúng (True Positive Rate):", tpr)
