# Lộ Trình Trở Thành AI Engineer (9-12 Tháng)

## Bài 2: Biến (Variables) và Kiểu dữ liệu (Data Types) – "Gạch cát" xây thuật toán

Để chuẩn bị cho các bài toán AI phức tạp hơn sau này (như xử lý hình ảnh, phân tích văn bản), hôm nay chúng ta sẽ làm quen với các loại "vật liệu cơ bản" nhất trong Python. Trong thế giới AI, dữ liệu không chỉ đơn thuần là những con số, mà nó có thể là một ma trận, một đoạn văn bản, hoặc các quyết định Đúng/Sai.

---

### 1. Ý nghĩa & Bản chất

* **Biến (Variable):** Hãy tưởng tượng biến như một **chiếc hộp có dán nhãn**. Bạn ném dữ liệu vào trong hộp và dán lên đó một cái tên để lần sau muốn tái sử dụng thì chỉ cần gọi tên cái nhãn đó ra.
* **Kiểu dữ liệu (Data Type):** Là "tính chất" hoặc "chủng loại" của dữ liệu nằm trong hộp. Python cần biết trong hộp chứa gì để xử lý cho đúng (ví dụ: bạn không thể lấy một câu văn đi thực hiện phép cộng với một con số được).

Trong AI, chúng ta sẽ liên tục làm việc với 4 kiểu dữ liệu cốt lõi sau:

| Kiểu dữ liệu | Tên trong Python | Ví dụ thực tế trong cấu trúc AI |
| :--- | :--- | :--- |
| **Số nguyên** | `int` (Integer) | Số lượng ảnh đầu vào để huấn luyện mô hình (vd: `1000`) |
| **Số thực (thập phân)** | `float` | Độ chính xác (Accuracy) của model (vd: `0.95` ~ 95%) |
| **Chuỗi chữ (Văn bản)** | `str` (String) | Câu text để AI dịch hoặc phân tích cảm xúc (vd: `"Tôi yêu AI"`) |
| **Đúng / Sai** | `bool` (Boolean) | Trạng thái mô hình dự đoán đúng hay sai? (`True` hoặc `False`) |

---

### 2. Thực hành ngay: Khởi tạo dữ liệu cho một Chatbot

Hãy xem cách chúng ta định nghĩa thông tin nền tảng cho một con Bot AI bằng Python bằng đoạn code cực kỳ tường minh dưới đây:

```python
# 1. Tên của Chatbot (Kiểu String - phải bọc trong dấu nháy)
bot_name = "MindBot"

# 2. Phiên bản hiện tại của mô hình (Kiểu Float)
version = 2.5

# 3. Số lượng người dùng đang phục vụ trực tuyến (Kiểu Int)
active_users = 1500

# 4. Trạng thái hệ thống có ổn định không? (Kiểu Boolean - lưu ý viết hoa chữ đầu True/False)
is_stable = True

# --- Kiểm tra "bản chất" dữ liệu ---
# Thử in ra kiểm tra xem Python hiểu đúng kiểu dữ liệu không nhé:
print(type(bot_name))     # Output: <class 'str'>
print(type(version))      # Output: <class 'float'>
print(type(active_users)) # Output: <class 'int'>
print(type(is_stable))    # Output: <class 'bool'>