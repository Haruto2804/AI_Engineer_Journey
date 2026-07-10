
## Bài 9: Pandas – Quản lý dữ liệu dạng bảng như một Pro

### 1. Ý nghĩa: Tại sao có NumPy rồi vẫn cần Pandas?

Nếu **NumPy** là vua xử lý các mảng số thuần túy (như ma trận điểm ảnh, biên độ âm thanh), thì **Pandas** là chúa tể xử lý dữ liệu cấu trúc hỗn hợp (vừa có tên, có tuổi, có ngày tháng, có số tiền...).

Hãy tưởng tượng bạn có một file Excel chứa thông tin của 1 triệu khách hàng để AI dự đoán xem ai có khả năng rời bỏ dịch vụ. Bạn không thể dùng NumPy để tính toán mượt mà trên đống chữ và số trộn lẫn đó được. Pandas sinh ra để biến file Excel đó thành một cấu trúc gọi là **DataFrame** (phần mềm hiểu như một cái bảng, có hàng và có cột rõ ràng) và xử lý nó với tốc độ của tên lửa.

---

### 2. Chuẩn bị: Hướng dẫn cài đặt Pandas

Tương tự như NumPy, Pandas cũng là một thư viện bên thứ ba và cần được cài đặt vào môi trường Python của bạn trước khi dùng.

#### Cách 1: Cài đặt trên máy tính cá nhân (Windows / Mac / Linux)

Bạn mở **Terminal** hoặc **Command Prompt** lên và gõ lệnh thần chú sau rồi bấm Enter:

```bash
pip install pandas

```

*Mẹo nhỏ: Khi cài đặt Pandas, hệ thống thường sẽ tự động cài luôn NumPy cho bạn vì hai thư viện này là "đôi bạn cùng tiến" trong Data Science.*

#### Cách 2: Nếu bạn dùng Google Colab hoặc Anaconda

* Đống dữ liệu khổng lồ của bạn đã có công cụ lo, vì trên **Google Colab** hoặc **Anaconda** đã tích hợp sẵn thư viện Pandas. Bạn có thể bỏ qua bước cài đặt này và nhảy thẳng vào viết code!

---

### 3. Thực hành: Tạo bảng dữ liệu và xem nhanh bằng Pandas

Giống như NumPy, ta cần nạp thư viện Pandas vào trước (thường viết tắt là `pd`):

```python
import pandas as pd

# Giả sử ta có dữ liệu của 3 mô hình AI dưới dạng Dictionary
data = {
    "Model_Name": ["ChatGPT", "Claude", "Gemini"],
    "Accuracy": [0.95, 0.96, 0.94],
    "Release_Year": [2022, 2023, 2023]
}

# Biến Dictionary thành một bảng DataFrame của Pandas
df = pd.DataFrame(data)

# In cái bảng này ra xem thử
print(df)

```

**Output ra màn hình sẽ đẹp như một góc của file Excel:**

```text
  Model_Name  Accuracy  Release_Year
0    ChatGPT      0.95          2022
1     Claude      0.96          2023
2     Gemini      0.94          2023

```

Bây giờ, nếu bạn chỉ muốn lấy riêng cột `Accuracy` để tính toán? Cực kỳ đơn giản: `df["Accuracy"]`.
Bạn muốn lọc các model ra mắt năm 2023? Chỉ cần: `df[df["Release_Year"] == 2023]`. Không cần vòng lặp `for` phức tạp nào cả!

---

### 4. Thử thách thực chiến số 9

Tôi có một bảng DataFrame tên là `df_users` chứa dữ liệu người dùng của một ứng dụng AI gồm 2 cột: `Username` và `Is_Premium` (Nhận giá trị `True` nếu đã trả phí, `False` nếu dùng miễn phí).

**Yêu cầu:** Bạn hãy đoán hoặc viết cú pháp Python/Pandas để:

1. Lấy ra riêng cột `Username` từ bảng `df_users`.
2. (Nâng cao một chút) Làm sao để lọc ra danh sách những người dùng có `Is_Premium` bằng `True`?

Hãy thử đưa ra phương án của bạn ngay dưới đây, sai đâu tôi sửa đó, không phải lo!