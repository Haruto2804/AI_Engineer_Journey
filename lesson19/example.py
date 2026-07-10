from sklearn.metrics import log_loss

# Thực tế (Sự thật bệnh án): 1 là Sốt, 0 là Khỏe
y_thuc_te = [1, 0]

# Tình huống 1: AI dự đoán rất sát sự thật (90% sốt, 10% sốt - tức là 90% khỏe)
AI_du_doan_tot = [0.90, 0.10]
diem_phat_1 = log_loss(y_thuc_te, AI_du_doan_tot)
print(f"Điểm phạt khi AI đoán giỏi: {diem_phat_1:.4f}")
# Kết quả ra rất thấp (khoảng 0.1)

# Tình huống 2: AI "tự tin mù quáng" (Bệnh nhân 1 đoán có 10% sốt, Bệnh nhân 2 đoán 99% sốt)
AI_du_doan_te = [0.10, 0.99]
diem_phat_2 = log_loss(y_thuc_te, AI_du_doan_te)
print(f"Điểm phạt khi AI tự tin mù quáng: {diem_phat_2:.4f}")
# Kết quả phạt cực kỳ nặng (hơn 3.0, cao gấp mấy chục lần!)
