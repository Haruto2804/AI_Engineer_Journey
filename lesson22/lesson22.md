

---
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/numerical-data/normalization)
### NUMBERIC DATA - BÀI 22: CHUẨN HÓA DỮ LIỆU (DATA NORMALIZATION / SCALING)

#### Phần 1: Ý nghĩa (Nó là gì? Tại sao phải dùng?)

**Ẩn dụ:** Tưởng tượng bạn đang làm giám khảo cho 2 cuộc thi cùng lúc:

* Cuộc thi thi ăn xúc xích: Ai ăn được 50 cái là vô địch.
* Cuộc thi chạy 100m: Ai chạy dưới 10 giây là vô địch.

Nếu bạn mang con số "50" (cái xúc xích) đi so sánh với "10" (giây), mọi thứ sẽ rất khập khiễng. Để chấm điểm công bằng cho danh hiệu "Siêu nhân toàn năng", bạn phải quy đổi điểm của cả 2 môn về cùng một thang điểm (ví dụ: từ 0 đến 10).

**Trong AI cũng y hệt như vậy.** Nếu bạn đưa cho AI một bảng dữ liệu có cột **Tuổi** (giá trị từ 18 - 60) và cột **Lương** (giá trị từ 10.000.000 - 50.000.000 VNĐ). AI thực chất là những cỗ máy tính toán bằng số học, nó sẽ thấy cột "Lương" có số bự quá, và tự động hiểu lầm rằng: *"À, cái cột Lương này to hơn hẳn, chắc chắn nó quan trọng hơn cột Tuổi"*.

Điều này dẫn đến AI dự đoán sai bét! Để tránh việc AI bị "ảo tưởng" bởi những con số to, ta phải **Chuẩn hóa (Scale)** ép tất cả các cột về cùng một thước đo (thường là từ `0` đến `1`). Cách phổ biến nhất gọi là **Min-Max Scaling** (hay Chia độ tuyến tính như tài liệu bạn vừa đọc).

#### Phần 2: Thực hành (Code chạy ngay)

Bạn không cần phải tự giải phương trình Toán học. Python và thư viện `scikit-learn` sẽ làm điều đó trong 3 dòng code.

*(Bạn có thể copy đoạn code này dán vào Google Colab hoặc IDE để chạy thử nhé)*

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Dữ liệu gốc: Tuổi thì nhỏ, Lương thì số rất to
data = {
    'Tuổi': [25, 30, 50], 
    'Lương': [10000000, 20000000, 50000000]
}
df = pd.DataFrame(data)
print("--- DỮ LIỆU GỐC ---")
print(df)

# 2. Gọi công cụ chuẩn hóa Min-Max (Ép về 0 đến 1)
scaler = MinMaxScaler()

# 3. Tiến hành ép kiểu và xem kết quả
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\n--- DỮ LIỆU SAU KHI CHUẨN HÓA ---")
print(df_scaled)

```

*Kết quả bạn sẽ thấy:* Người 25 tuổi (thấp nhất) sẽ bị biến thành số `0.0`, người 50 tuổi (cao nhất) biến thành `1.0`. Cột lương cũng tương tự! Lúc này, AI học sẽ rất mượt và nhanh.

#### Phần 3: Thử thách nhỏ dành cho bạn

Dựa vào logic của kỹ thuật Min-Max Scaling (ép từ thấp nhất là 0 đến cao nhất là 1) ở trên, hãy trả lời câu hỏi logic này:

Giả sử bạn có một cột dữ liệu là **"Chiều cao"** của một nhóm người. Người thấp nhất nhóm cao 150cm, người cao nhất nhóm cao 190cm.
**Hỏi:** Sau khi dùng code chuẩn hóa Min-Max, chiều cao của người thấp nhất (150cm) sẽ bị biến thành con số mấy? Và chiều cao của người cao nhất (190cm) sẽ bị biến thành con số mấy?

👉 *Hãy trả lời câu hỏi này dưới góc nhìn logic của bạn. Trả lời xong, tôi sẽ dạy bạn bước tiếp theo!*