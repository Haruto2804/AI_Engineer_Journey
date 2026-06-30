### Tình huống thực tế:

Bạn nhận được một file dữ liệu khách hàng từ bộ phận Marketing gửi sang để chuẩn bị cho AI học. Nhưng ôi thôi, nhân viên nhập liệu đã làm ăn rất cẩu thả: có người bị lặp tên 2 lần, có người quên nhập tuổi, có người quên nhập lương. AI mà nhìn thấy dữ liệu khuyết thiếu (`NaN` - Not a Number) là nó sẽ báo lỗi và "đình công" ngay lập tức.

Nhiệm vụ của bạn là phải dọn sạch cái bảng này.

### Bảng dữ liệu "Rác":

Bạn hãy copy đoạn code tạo dữ liệu này vào IDE của bạn:

```python
import pandas as pd
import numpy as np # Import numpy để tạo ra các giá trị NaN (rỗng)

data_rac = {
    "Khach_Hang": ["Gia Bảo", "Huấn", "Haruto", "Gia Bảo", "Thầy Ông Nội"],
    "Tuoi": [25, np.nan, 22, 25, 85],       # Huấn bị quên nhập tuổi (NaN)
    "Luong_Trieu": [15, 40, np.nan, 15, 5]  # Haruto bị quên nhập lương (NaN)
}

df = pd.DataFrame(data_rac)
print("--- DỮ LIỆU GỐC TRƯỚC KHI DỌN ---")
print(df)

```

Khi in ra, nó sẽ trông gớm ghiếc như thế này:

```text
  Khach_Hang  Tuoi  Luong_Trieu
0    Gia Bảo  25.0         15.0
1       Huấn   NaN         40.0
2     Haruto  22.0          NaN
3    Gia Bảo  25.0         15.0  <-- Bị trùng lặp hoàn toàn với dòng 0
4 Thầy Ông Nội  85.0          5.0

```

---

### Yêu cầu Thử thách:

Bạn hãy tự tìm hiểu hoặc suy luận cú pháp Pandas để thực hiện **3 bước dọn dẹp** sau đây:

1. **Loại bỏ kẻ mạo danh:** Dòng số 0 và dòng số 3 giống hệt nhau ("Gia Bảo"). Hãy tìm cách xóa các dòng bị trùng lặp (Duplicate) trong bảng `df`. *(Gợi ý: Tìm hiểu hàm `.drop_duplicates()`)*
2. **Xử lý hố đen dữ liệu (Missing Data):** AI không biết tính toán với chữ `NaN`. Hãy tìm cách điền số `0` vào TẤT CẢ những chỗ nào đang bị `NaN` trong bảng. *(Gợi ý: Tìm hiểu hàm `.fillna(...)`)*
3. **Trích xuất dữ liệu sạch:** Sau khi dọn xong, hãy tạo một dòng code để chỉ in ra những khách hàng có `Tuoi` lớn hơn 0 (để loại bỏ những người vừa bị điền tuổi bằng 0 ở bước trên).

Bạn cứ thoải mái Google cách dùng các hàm gợi ý trên nhé. Kỹ năng Google Document của thư viện chính là "bài học ẩn" trong thử thách này.

