# Bài 5: Hàm (Functions) – Đóng gói "vũ khí" để tái sử dụng

Chúc mừng bạn đã đi được một nửa chặng đường của tuần đầu tiên!

Bạn đã biết cách sử dụng:

- Biến (Variables)
- Rẽ nhánh (if/else)
- Vòng lặp (for)

Nhưng hãy tưởng tượng:

Đoạn code lọc ảnh phía trên của bạn cần được sử dụng ở rất nhiều nơi trong dự án AI:

- Khi nhận ảnh từ Camera
- Khi người dùng Upload ảnh
- Khi quét kho ảnh cũ
- Khi xử lý Batch Data
- Khi chạy API

Bạn không thể cứ **copy-paste** đoạn code đó khắp nơi được.

Nếu một ngày sếp nói:

> "Đổi điều kiện từ 5MB thành 7MB nhé."

Bạn sẽ phải sửa ở:

- file A
- file B
- file C
- ...
- file J

Chỉ cần quên sửa một chỗ là hệ thống sẽ chạy sai.

Đó chính là lý do **Function (Hàm)** ra đời.

---

# 1. Hàm (Function) là gì?

Function là một đoạn code được:

- Đặt tên
- Đóng gói
- Có thể gọi lại nhiều lần

Thay vì viết đi viết lại cùng một đoạn code, ta chỉ cần:

- Viết một lần
- Dùng cả đời

---

## Hình dung đơn giản

Giống như bạn có một chiếc máy pha cà phê.

Bạn không cần mỗi sáng tự chế tạo lại chiếc máy.

Chỉ cần:

```
Bỏ hạt cà phê
↓
Bấm nút
↓
Nhận ly cà phê
```

Function cũng hoạt động như vậy.

---

# 2. Function gồm những gì?

Một hàm thường có 3 phần:

```
Input (Arguments)
        ↓
     Function
        ↓
Output (Return)
```

Ví dụ

```
Ảnh 7.2MB
      ↓
check_image_validity()
      ↓
"Hợp lệ"
```

---

# 3. Cú pháp

```python
def ten_ham(tham_so):
    # code
    return ket_qua
```

Ý nghĩa:

- `def` = Define (định nghĩa hàm)
- `ten_ham` = tên hàm
- `tham_so` = dữ liệu đầu vào
- `return` = trả kết quả

---

# 4. Đóng gói bộ lọc ảnh AI

Trước đây bạn phải viết:

```python
if size >= 5:
    print("Hợp lệ")
else:
    print("Loại bỏ")
```

Mỗi lần có ảnh mới lại viết lại.

Giờ chỉ cần đóng gói.

```python
def check_image_validity(size):
    if size >= 5:
        return "Hợp lệ"
    else:
        return "Loại bỏ"
```

Xong.

Từ giờ chỉ việc gọi tên hàm.

---

# 5. Sử dụng Function

Ảnh đầu tiên:

```python
result_1 = check_image_validity(7.2)

print(result_1)
```

Output

```
Hợp lệ
```

---

Ảnh thứ hai

```python
result_2 = check_image_validity(3.0)

print(result_2)
```

Output

```
Loại bỏ
```

---

Ảnh thứ ba

```python
result_3 = check_image_validity(12.5)

print(result_3)
```

Output

```
Hợp lệ
```

---

# 6. Chương trình hoàn chỉnh

```python
def check_image_validity(size):
    if size >= 5:
        return "Hợp lệ"
    else:
        return "Loại bỏ"


result_1 = check_image_validity(7.2)
print(f"Kết quả ảnh 1: {result_1}")

result_2 = check_image_validity(3.0)
print(f"Kết quả ảnh 2: {result_2}")

result_3 = check_image_validity(12.5)
print(f"Kết quả ảnh 3: {result_3}")
```

Output

```
Kết quả ảnh 1: Hợp lệ
Kết quả ảnh 2: Loại bỏ
Kết quả ảnh 3: Hợp lệ
```

---

# 7. Luồng hoạt động

```
                7.2
                 │
                 ▼
      check_image_validity()
                 │
        size >= 5 ?
           │        │
          Có       Không
           │          │
           ▼          ▼
      "Hợp lệ"    "Loại bỏ"
```

---

# 8. Vì sao Function cực kỳ quan trọng trong AI?

Trong các dự án AI thực tế sẽ có hàng trăm tác vụ lặp đi lặp lại như:

- Kiểm tra kích thước ảnh
- Resize ảnh
- Chuẩn hóa dữ liệu
- Đọc file
- Ghi log
- Tiền xử lý văn bản
- Tokenize
- Tính Accuracy
- Tải mô hình
- Dự đoán kết quả

Mỗi tác vụ đều nên được viết thành một Function.

Ví dụ:

```python
resize_image()

normalize_image()

load_dataset()

predict()

save_result()

calculate_accuracy()
```

Nhờ đó:

- Code ngắn hơn
- Dễ đọc hơn
- Dễ bảo trì hơn
- Dễ sửa lỗi hơn
- Dễ tái sử dụng

Đây là phong cách lập trình mà mọi kỹ sư AI chuyên nghiệp đều áp dụng.

---

# 9. Tổng kết

Sau bài này bạn đã biết:

- Cách định nghĩa Function bằng `def`
- Function nhận dữ liệu đầu vào (Arguments)
- Function trả kết quả bằng `return`
- Cách gọi Function nhiều lần
- Lợi ích của việc tái sử dụng code

Bạn vừa học được một trong những nền tảng quan trọng nhất của lập trình Python. Từ những bài sau, gần như mọi chương trình AI đều sẽ được xây dựng bằng cách kết hợp nhiều Function nhỏ lại với nhau.
# Bài tập thực chiến số 5: Trở thành Kỹ sư tính toán hiệu năng Model

Trong Machine Learning và AI, sau khi huấn luyện một mô hình, chúng ta cần đánh giá xem mô hình hoạt động tốt đến đâu.

Một trong những chỉ số quan trọng nhất là **F1-Score**.

F1-Score là sự kết hợp giữa:

- **Precision** (Độ chính xác)
- **Recall** (Độ bao phủ)

Giúp đánh giá mô hình một cách cân bằng hơn.

---

# Công thức tính F1-Score

Cho:

- `P` = Precision
- `R` = Recall

Ta có công thức:

$$
F1 = \frac{2 \times P \times R}{P + R}
$$
```text
F1 = (2 × Precision × Recall) / (Precision + Recall)
```
---

# Yêu cầu

Hãy viết một hàm có tên:

```python
calculate_f1_score()
```

Hàm nhận vào **2 tham số**:

- `precision`
- `recall`

Sau đó:

- Tính F1-Score theo công thức trên.
- `return` kết quả.

Cuối cùng hãy gọi hàm với:

```python
precision = 0.8
recall = 0.9
```

và in kết quả ra màn hình.

---

# Gợi ý

Khung chương trình:

```python
def calculate_f1_score(precision, recall):
    # Viết công thức tính F1-Score ở đây

    return ...
```

Sau đó gọi hàm:

```python
result = calculate_f1_score(0.8, 0.9)

print(f"F1-Score = {result}")
```

---

# Kết quả mong đợi

```
F1-Score = 0.8470588235294118
```

*(Có thể khác một chút ở số chữ số thập phân tùy cách hiển thị.)*

---

# Đáp án tham khảo

```python
def calculate_f1_score(precision, recall):
    f1 = (2 * precision * recall) / (precision + recall)
    return f1


result = calculate_f1_score(0.8, 0.9)

print(f"F1-Score = {result}")
```

Output

```
F1-Score = 0.8470588235294118
```

---

# Giải thích từng bước

Giả sử:

```python
precision = 0.8
recall = 0.9
```

Hàm sẽ tính:

```python
f1 = (2 * 0.8 * 0.9) / (0.8 + 0.9)
```

Tử số:

```python
2 * 0.8 * 0.9 = 1.44
```

Mẫu số:

```python
0.8 + 0.9 = 1.7
```

Kết quả:

```python
1.44 / 1.7
```

≈

```python
0.8470588235294118
```

Giá trị này được `return` về cho biến `result`, sau đó được in ra màn hình.

---

# Kiến thức bạn vừa luyện tập

Sau bài tập này, bạn đã thực hành:

- Khai báo Function bằng `def`
- Truyền nhiều tham số vào Function
- Thực hiện phép tính trong Function
- Sử dụng `return` để trả kết quả
- Gọi Function và lưu kết quả vào biến
- Ứng dụng Function vào một công thức đánh giá mô hình AI thực tế

Đây là cách các kỹ sư AI thường đóng gói các phép tính thành các hàm để có thể tái sử dụng trong nhiều dự án khác nhau.