import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score

# Nạp dữ liệu thực tế từ bài toán
y_that = np.array([0, 0, 1, 0, 1, 1, 0, 1])
y_doan = np.array([0.15, 0.2, 0.4, 0.55, 0.6, 0.75, 0.3, 0.85])

# Tính toán
auc = roc_auc_score(y_that, y_doan)
fpr, tpr, thresholds = roc_curve(y_that, y_doan)

# In kết quả
print(f"Điểm AUC của mô hình: {auc:.2f}")
print("\nCác ngưỡng (Thresholds) đã thử:", thresholds)
print("Tỷ lệ bắt nhầm (FPR):", fpr)
print("Tỷ lệ bắt đúng (TPR):", tpr)

# Trả lời:
# 1. điểm AUC này cao, mô hình này tốt
# Nên chọn ngưỡng 0.4 vì tỷ lệ bắt trúng 100% nhưng tỷ lệ bắt nhầm chỉ 25% chấp nhận được
