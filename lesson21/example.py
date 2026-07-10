import pandas as pd
import matplotlib.pyplot as plt

# 1. Giả lập dữ liệu giá nhà (9 căn bình dân và 1 căn siêu biệt thự 500 tỷ của đại gia)
gia_nha = [2.1, 2.5, 3.0, 2.8, 3.2, 4.0, 3.5, 2.9, 3.1, 500.0]
df = pd.DataFrame({"gia": gia_nha})

# 2. Vẽ biểu đồ Histogram để xem "hình thù" dữ liệu
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(df["gia"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram: Trước khi xử lý")
plt.xlabel("Giá (Tỷ)")

# 3. Áp dụng kỹ thuật Clipping (Cắt phần): Chặn trần ở mức 5.0 tỷ
# Căn nhà 500 tỷ sẽ bị ép về bằng 5.0 tỷ để không phá bĩnh mô hình
df["gia_sach"] = df["gia"].clip(upper=5.0)
# 4. Vẽ lại Histogram sau khi đã "làm sạch" dữ liệu
plt.subplot(1, 2, 2)
plt.hist(df["gia_sach"], bins=5, color="lightgreen", edgecolor="black")
plt.title("Histogram: Sau khi dùng Clipping")
plt.xlabel("Giá (Tỷ)")

plt.tight_layout()
plt.show()

# 1 BT Tình huống
# Với giá trị 999: Nếu bạn dùng Clipping để ép về 100, mô hình AI sẽ hiểu là "À, có một cụ già 100 tuổi đang mua sắm". Nhưng thực tế đây là dữ liệu rác.

# Với giá trị -1: Tương tự, nếu ép về 1, AI sẽ nghĩ "Có đứa bé 1 tuổi đang tự mua hàng".
