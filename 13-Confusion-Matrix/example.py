from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix

# Giả sử đây là đáp án thực tế của 5 giao dịch (1 là lừa đảo, 0 là bình thường)
y_that = [0, 0, 1, 1, 0]

# Đây là kết quả con AI đoán (Nó bỏ lọt 1 vụ lừa đảo, và báo động giả 1 vụ bình thường)
y_doan = [0, 1, 1, 0, 0]
ma_tran = confusion_matrix(y_that, y_doan)
print(ma_tran)
