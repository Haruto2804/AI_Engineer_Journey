

## Bài 8: NumPy – Sức mạnh tính toán tối thượng của AI

### 1. Ý nghĩa: Tại sao Python thuần là chưa đủ cho AI?

Hãy tưởng tượng bạn có một bức ảnh kỹ thuật số. Bản chất của bức ảnh đó trong máy tính là một cái lưới khổng lồ chứa hàng triệu ô số (mỗi ô là một điểm ảnh - pixel). Để AI nhận diện được khuôn mặt của bạn trong bức ảnh, nó phải lấy hàng triệu ô số đó đi nhân với hàng triệu con số khác của thuật toán.

Nếu dùng vòng lặp `for` của Python thuần mà đi duyệt qua từng ô một, máy tính sẽ chạy chậm như rùa bò và bị treo ngay lập tức.

**NumPy xuất hiện để giải quyết việc này.** Nó gom toàn bộ hàng triệu con số đó lại thành một khối (gọi là **Mảng - Array** hoặc **Ma trận**). Thay vì bắt máy tính tính từng con số, NumPy dùng một lệnh duy nhất để ép toàn bộ khối số đó tính toán cùng một lúc (gọi là Vector hóa - Vectorization). Tốc độ của NumPy nhanh hơn Python thuần gấp **gần 100 lần**!

---

### 2. Chuẩn bị: Hướng dẫn cài đặt NumPy

Vì NumPy là một thư viện bên thứ ba (không có sẵn khi vừa cài Python), bạn cần cài đặt nó vào máy tính của mình trước khi sử dụng.

#### Cách 1: Cài đặt trên máy tính cá nhân (Windows / Mac / Linux)

Bạn hãy mở **Terminal** (trên Mac/Linux) hoặc **Command Prompt / PowerShell** (trên Windows) và gõ lệnh sau rồi nhấn Enter:

```bash
pip install numpy

```

*Hệ thống sẽ tự động tải và cài đặt NumPy chỉ trong vài giây.*

#### Cách 2: Nếu bạn dùng Google Colab hoặc Anaconda

* **Tin vui:** Nếu bạn đang học Python trên **Google Colab** hoặc dùng bộ công cụ **Anaconda**, NumPy đã được cài đặt sẵn 100%. Bạn không cần gõ lệnh cài đặt nào cả, chỉ việc vào code và sử dụng thôi!

---

### 3. Thực hành: Biến danh sách số thành Mảng NumPy

Để dùng NumPy, việc đầu tiên là chúng ta phải nạp (import) nó vào code:

```python
import numpy as np  # Viết tắt là np cho ngắn gọn

# Có một danh sách Python thuần chứa độ sáng của 3 pixel ảnh
pixel_list = [120, 255, 80]

# Biến nó thành Mảng NumPy siêu tốc độ bằng hàm np.array()
pixel_array = np.array(pixel_list)

# Thử tăng độ sáng của TẤT CẢ các pixel lên gấp đôi
# Với Python thuần bạn phải dùng vòng lặp for. Với NumPy, bạn chỉ cần gõ:
new_pixels = pixel_array * 2

print(new_pixels)
# Output: [240 510 160] -> Từng phần tử tự động nhân 2 trong chớp mắt!

```

---

### 4. Thử thách nhỏ dành cho bạn

Giả sử bạn đang làm hệ thống AI xử lý âm thanh. Bạn thu được một mảng NumPy chứa biên độ âm thanh của một đoạn voice như sau:
`audio_signals = np.array([0.5, 0.8, 1.2, 0.2])`

**Yêu cầu:** Hãy viết đoạn code (gồm cả bước import) để **giảm một nửa (chia cho 2)** giá trị của tất cả các tín hiệu âm thanh trong mảng `audio_signals` trên và in kết quả ra màn hình.

Bạn hãy gõ thử đoạn code đó ngay dưới đây nhé!