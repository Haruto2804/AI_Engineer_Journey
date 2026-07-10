
## Bài 3: Cấu trúc điều kiện (If - Else) – "Bộ não" đưa ra quyết định của AI

Dù AI có dùng các thuật toán học máy phức tạp đến đâu, thì ở tầng ứng dụng (Application Layer), chúng ta vẫn phải dùng các câu lệnh điều kiện để đưa ra quyết định cuối cùng: *Có mở cửa không? Có chặn tài khoản này vì nghi ngờ spam không? Có gửi cảnh báo về điện thoại không?*

### 1. Bản chất của If - Else trong Python

Trong Python, cấu trúc điều kiện cực kỳ dễ đọc, nhưng có **2 quy tắc "bất di bất dịch"** mà bạn cần lưu ý để tránh lỗi cú pháp:

1. **Dấu hai chấm (`:`):** Phải có ở cuối câu lệnh `if`, `elif`, hoặc `else`. Nó báo hiệu cho Python biết: "Chuẩn bị vào khối lệnh thực thi đây!".
2. **Thụt lề (Indentation):** Các dòng code nằm trong khối `if` hoặc `else` bắt buộc phải thụt lề vào trong (thường là dùng 1 phím **Tab** hoặc 4 dấu cách). Python dùng thụt lề để hiểu code nào thuộc về khối lệnh nào, thay vì dùng dấu ngoặc nhọn `{}` như C++ hay Java.

---

### 2. Mở rộng thực tế: Khi hệ thống có nhiều hơn 2 lựa chọn

Trong thực tế, hệ thống nhận diện khuôn mặt của bạn không chỉ có 2 trạng thái "Cho vào" hay "Đuổi ra". Nó sẽ có vùng "xám" – ví dụ: AI nhìn hơi giống nhưng chưa chắc chắn lắm, cần yêu cầu quét lại.

Lúc này, chúng ta dùng thêm từ khóa `elif` (viết tắt của Else If).

```python
confidence_score = 0.75

if confidence_score >= 0.9:
    print("Mở cửa: Xác thực thành công!")
elif confidence_score >= 0.7:
    print("Cảnh báo: Vui lòng đứng im và nhìn thẳng vào camera để quét lại!")
else:
    print("Cửa đóng: Không tìm thấy người dùng trong hệ thống!")

```

---

### 3. Thử thách thực chiến số 3: Bộ lọc kiểm duyệt nội dung của AI (Content Moderation)

Hãy tưởng tượng bạn đang làm tính năng chặn các bình luận tiêu cực/toxic cho một mạng xã hội bằng AI. Model AI của bạn sẽ trả về một điểm số gọi là `toxic_score` từ `0.0` đến `1.0` (Điểm càng cao thì câu bình luận càng độc hại).

**Yêu cầu:** Bạn hãy viết một đoạn code Python để phân loại hành động dựa trên biến `toxic_score = 0.85`:

* Nếu `toxic_score >= 0.8`: In ra `"Xóa bình luận và khóa tài khoản!"`
* Nếu `toxic_score >= 0.5` (nhưng nhỏ hơn 0.8): In ra `"Ẩn bình luận và gửi cảnh cáo cho người dùng."`
* Các trường hợp còn lại (nhỏ hơn 0.5): In ra `"Bình luận hợp lệ. Cho phép hiển thị."`

Bạn hãy viết đoạn code xử lý logic này nhé!