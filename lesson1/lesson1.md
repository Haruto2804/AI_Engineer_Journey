# Lộ Trình Trở Thành AI Engineer (9-12 Tháng)

## Bài 1: Tại sao lại là Python? "Vị vua" của thế giới AI

Chào mừng bạn đến với bài học đầu tiên! Chúng ta sẽ tiếp cận theo phương châm: **Thực dụng, chiến đấu bằng code trước rồi mổ xẻ bản chất sau**. Cứ tự tin lên, chúng ta bắt đầu ngay nhé!

---

### 1. Ý nghĩa: Tại sao AI Engineer bắt buộc phải giỏi Python?

Hãy tưởng tượng bạn là một tổng công trình sư chuẩn bị xây một tòa nhà chọc trời (ở đây là một hệ thống AI). Bạn có hai lựa chọn:

1. **Tự đi nung từng viên gạch, tự chế máy trộn bê tông:** Đây là cách làm của các ngôn ngữ như C++ hay Java. Rất mạnh, rất nhanh, nhưng tốn quá nhiều thời gian vào những việc vặt vãnh.
2. **Có sẵn một siêu thị vật liệu:** Cần móng nhà? Có sẵn khối bê tông đúc sẵn. Cần hệ thống điện? Có sẵn module thông minh. Bạn chỉ việc kết nối chúng lại. **Đó chính là Python!**

Trong AI, chúng ta không cần viết lại thuật toán từ đầu. Các "ông lớn" như Google, Meta đã làm sẵn các thư viện cực mạnh (như NumPy, TensorFlow, PyTorch). Việc của một AI Engineer là hiểu tư duy, dùng Python như một "sợi dây thừng" để buộc các khối thư viện khổng lồ đó lại với nhau thành một ứng dụng hoàn chỉnh. 

> **Cốt lõi:** Python thống trị AI vì nó **dễ đọc như tiếng Anh** và sở hữu **hệ sinh thái thư viện AI mạnh nhất hành tinh**.

---

### 2. Thực hành: Cảm nhận sự "mỳ ăn liền" của Python

Thay vì giải thích lý thuyết dông dài, hãy nhìn cách Python xử lý một danh sách dữ liệu (ví dụ: điểm số của các mô hình AI) chỉ trong nháy mắt.

#### Đoạn code mẫu:
```python
# Có một danh sách độ chính xác của 3 mô hình AI (đơn vị %)
accuracy_scores = [85, 92, 78]

# Tính điểm trung bình của các mô hình
average_score = sum(accuracy_scores) / len(accuracy_scores)

# In kết quả ra màn hình
print(f"Độ chính xác trung bình của hệ thống: {average_score}%")