

## BÀI 21: WORKING WITH DATA - VISUALIZATION 
---

### PHẦN 1: Ý NGHĨA (Hình ảnh hóa là gì? Tại sao phải vẽ đồ thị?)

Nếu chỉ nhìn vào bảng số liệu `.describe()`, bạn giống như một người mù sờ voi. Bạn chỉ biết cái đuôi, cái tai chứ không thấy được toàn bộ con voi.

Để nhìn thấy "hình thù" của dữ liệu, AI Engineer có 2 vũ khí hạng nặng:

1. **Histogram (Biểu đồ tần suất):** Hãy tưởng tượng bạn gom tất cả những người có cùng chiều cao vào chung một cái xô. Xô nào nhiều người nhất thì cột của xô đó sẽ cao nhất. Nhìn vào Histogram, bạn biết ngay dữ liệu của mình đang "tập trung đông đúc" ở đâu và có ai "bị cô lập" ở vùng xa xôi (chính là Outlier) hay không.
2. **Scatter Plot (Biểu đồ tán xạ):** Tưởng tượng bạn bắn các điểm dữ liệu lên một bức tường phẳng. Nếu các điểm tụ lại thành một cụm bầy đàn, tự nhiên có một điểm bay tít ra rìa ngoài, điểm "đơn độc" đó chính là Outlier.

---

### PHẦN 2: THỰC HÀNH (Code vẽ đồ thị & Trảm Outlier)

Chúng ta sẽ dùng `pandas` kết hợp với thư viện `matplotlib` để vẽ hình. Hãy copy đoạn code ngắn gọn này chạy thử trên môi trường của bạn (như Jupyter Notebook hoặc Google Colab):

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Giả lập dữ liệu giá nhà (9 căn bình dân và 1 căn siêu biệt thự 500 tỷ của đại gia)
gia_nha = [2.1, 2.5, 3.0, 2.8, 3.2, 4.0, 3.5, 2.9, 3.1, 500.0]
df = pd.DataFrame({'gia': gia_nha})

# 2. Vẽ biểu đồ Histogram để xem "hình thù" dữ liệu
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(df['gia'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram: Trước khi xử lý")
plt.xlabel("Giá (Tỷ)")

# 3. Áp dụng kỹ thuật Clipping (Cắt phần): Chặn trần ở mức 5.0 tỷ
# Căn nhà 500 tỷ sẽ bị ép về bằng 5.0 tỷ để không phá bĩnh mô hình
df['gia_sach'] = df['gia'].clip(upper=5.0)

# 4. Vẽ lại Histogram sau khi đã "làm sạch" dữ liệu
plt.subplot(1, 2, 2)
plt.hist(df['gia_sach'], bins=5, color='lightgreen', edgecolor='black')
plt.title("Histogram: Sau khi dùng Clipping")
plt.xlabel("Giá (Tỷ)")

plt.tight_layout()
plt.show()

```

**Hiện tượng bạn sẽ thấy:**

* **Hình 1 (Trước xử lý):** Bạn sẽ thấy một cột đứng chót vót ở gần vạch số 0 (nơi 9 căn nhà bình dân tụ tụ lại), và một dấu chấm nhỏ xíu nằm đơn độc mãi tận vạch số 500. Khoảng trống mênh mông ở giữa chính là bằng chứng tố cáo có Outlier cực đoan!
* **Hình 2 (Sau xử lý):** Toàn bộ dữ liệu giờ đã quy về một mối từ 2 đến 5 tỷ, đồ thị trông cực kỳ "gọn gàng" và đẹp đẽ, sẵn sàng ném vào cho AI học.

---

### PHẦN 3: THỬ THÁCH NHỎ CHO BẠN

Để kiểm tra xem bạn đã thực sự làm chủ được vũ khí trực quan hóa này chưa, hãy trả lời câu hỏi thực tế sau:

**Tình huống:** Bạn được giao một tập dữ liệu về **Tuổi của người dùng** trên một ứng dụng mua sắm. Khi bạn vẽ biểu đồ **Histogram**, bạn thấy đại đa số người dùng nằm trong độ tuổi từ $18 \rightarrow 45$. Tuy nhiên, ở góc xa của đồ thị, xuất hiện một cột nhỏ ghi nhận có một số người dùng mang số tuổi là **-1** và **999**.

1. Hai giá trị **-1** và **999** này thuộc loại Outlier nào (Outlier Lỗi hay Outlier Hợp lệ)?
2. Bạn sẽ dùng cách nào để xử lý 2 giá trị này (Xóa thẳng tay hay dùng Clipping)? Tại sao?

Hãy đưa ra phương án xử lý của một AI Engineer tương lai nhé! Chờ phản hồi từ bạn.