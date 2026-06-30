Chuẩn không cần chỉnh! Bạn áp dụng cấu trúc `if - elif - else` rất mượt mà. Lỗi chính tả nhỏ ở chữ "Xóa" (`óa`) không thành vấn đề, logic code của bạn hoàn toàn chính xác và đã giải quyết gọn gàng bài toán kiểm duyệt dữ liệu.

Với `toxic_score = 0.9`, hệ thống sẽ lập tức kích hoạt nhánh đầu tiên và in ra: `óa bình luận và khóa tài khoản!`.

---

## Bài 4: Vòng lặp (Loops) – Sức mạnh "cày cuốc" của AI

Trong AI, chúng ta hiếm khi xử lý một dữ liệu đơn lẻ. Chúng ta xử lý **hàng triệu** bức ảnh, **hàng vạn** câu văn. Để bắt máy tính lặp đi lặp lại một hành động trên đống dữ liệu khổng lồ đó mà không phải viết lại code, chúng ta dùng **Vòng lặp**.

Hôm nay chúng ta sẽ làm quen với vòng lặp phổ biến và quyền lực nhất: **Vòng lặp `for**`.

### 1. Bản chất của vòng lặp `for`

Hãy tưởng tượng bạn có một rổ cam (một danh sách dữ liệu). Vòng lặp `for` giống như một người thợ: thò tay vào rổ, nhặt **từng quả cam một** ra, kiểm tra hoặc xử lý nó, rồi tiếp tục nhặt quả tiếp theo cho đến khi hết rổ.

Cú pháp của nó trong Python rất tự nhiên:

```python
for item in danh_sách:
    # Làm gì đó với item này

```

---

### 2. Thực hành: Duyệt qua danh sách để "chuẩn hóa" dữ liệu AI

Trong AI, dữ liệu thô thu thập về thường rất lộn xộn. Ví dụ, text do người dùng gõ vào chatbot có chỗ viết hoa, chỗ viết thường. Trước khi đưa vào model AI, ta cần chuyển tất cả về chữ thường (lowercase).

Hãy xem sức mạnh của `for`:

```python
# Danh sách các từ khóa người dùng gõ vào Chatbot
user_inputs = ["Hello", "AI ENGINEER", "Python", "tôi Muốn Học AI"]

# Dùng vòng lặp for để duyệt qua từng câu
for text in user_inputs:
    # Hàm .lower() giúp biến chữ hoa thành chữ thường
    text_clean = text.lower()
    print(f"Dữ liệu sau khi làm sạch: {text_clean}")

```

**Output:**

> Dữ liệu sau khi làm sạch: hello
> Dữ liệu sau khi làm sạch: ai engineer
> Dữ liệu sau khi làm sạch: python
> Dữ liệu sau khi làm sạch: tôi muốn học ai

Chỉ với 2 dòng code `for`, bạn có thể xử lý 4 câu, 400 câu hay 4 triệu câu một cách dễ dàng.

---

### 3. Thử thách thực chiến số 4: Lọc dữ liệu ảnh "rác"

Bạn đang chuẩn bị dữ liệu để huấn luyện một mô hình AI nhận diện xe cộ. Model yêu cầu ảnh đầu vào phải có dung lượng lớn hơn **5MB** thì mới đủ sắc nét để học. Những ảnh nhỏ hơn sẽ bị coi là ảnh rác và bị loại bỏ.

Bạn có một danh sách dung lượng của các bức ảnh (đơn vị MB) như sau:
`photo_sizes = [2, 8, 1.5, 12, 6, 4.5]`

**Yêu cầu:** Hãy viết một vòng lặp `for` kết hợp với điều kiện `if` để duyệt qua danh sách `photo_sizes`. Nếu ảnh nào `>= 5`, hãy in ra màn hình: `"Ảnh hợp lệ, giữ lại để train AI!"`. Nếu ảnh nào nhỏ hơn 5, in ra: `"Ảnh quá nhỏ, loại bỏ!"`.

Bạn hãy thử sức viết đoạn code "cày cuốc" đầu tiên này xem sao!