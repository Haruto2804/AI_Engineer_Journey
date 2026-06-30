
## Bài 6: Danh sách nâng cao (List) & Từ điển (Dictionary) – "Nhà kho" chứa dữ liệu AI

Khi làm việc với AI, dữ liệu không nằm đơn lẻ mà thường được gom lại thành các cấu trúc để dễ quản lý. Hai cấu trúc dữ liệu quan trọng nhất mà bạn sẽ dùng hàng ngày là **List** (Danh sách) và **Dictionary** (Từ điển).

### 1. Phân biệt nhanh List và Dictionary

* **List (Danh sách):** Giống như một hàng ghế được đánh số thứ tự từ `0, 1, 2, 3...`. Bạn dùng List khi **thứ tự** của dữ liệu là quan trọng (ví dụ: chuỗi các khung hình trong một đoạn video, hoặc danh sách các từ trong một câu).
* **Dictionary (Từ điển):** Giống như một cuốn danh bạ điện thoại, lưu trữ dữ liệu theo cặp **Key - Value (Khóa - Giá trị)**. Thay vì tìm bằng số thứ tự, bạn tìm bằng tên "Khóa". Bạn dùng Dictionary khi muốn lưu trữ các **thuộc tính** của một đối tượng.

---

### 2. Thực hành: Quản lý thông tin một Model AI bằng Dictionary

Hãy xem cách chúng ta lưu thông tin cấu hình và kết quả của một mô hình AI bằng Dictionary:

```python
# Khởi tạo một Dictionary bằng dấu ngoặc nhọn {}
ai_model_profile = {
    "model_name": "YOLOv8",          # Key là 'model_name', Value là 'YOLOv8'
    "task": "Object Detection",      # Nhận diện vật thể
    "accuracy": 0.92,                # Độ chính xác
    "epochs": 50                     # Số chu kỳ huấn luyện
}

# Cách truy xuất dữ liệu: Gọi tên "Key" trong dấu ngoặc vuông
print(f"Tên model: {ai_model_profile['model_name']}") 
# Output: Tên model: YOLOv8

# Cách cập nhật dữ liệu hoặc thêm thuộc tính mới
ai_model_profile["accuracy"] = 0.94   # Cập nhật độ chính xác mới
ai_model_profile["status"] = "Ready"  # Thêm một cặp Key-Value mới

print(ai_model_profile)

```

---

### 3. Thử thách thực chiến số 6: Tổng hợp kết quả đánh giá Model

Hệ thống AI của bạn vừa quét qua một văn bản và trả về thông tin phân tích cảm xúc của câu văn đó dưới dạng một Dictionary.

```python
sentiment_result = {
    "text": "Khóa học AI này thực sự rất thực tế và dễ hiểu!",
    "label": "Positive",
    "confidence": 0.97
}

```

**Yêu cầu:** 1. Hãy viết lệnh in ra màn hình nhãn dự đoán (`label`) của câu văn trên.
2. Hãy viết một câu điều kiện `if`: Nếu độ tự tin (`confidence`) lớn hơn `0.9`, hãy in ra câu: `"Kết quả đáng tin cậy!"`. Ngược lại, in ra: `"Cần kiểm tra lại."`

Bạn hãy viết đoạn code xử lý yêu cầu này nhé!