Tuyệt vời! Chúng ta sẽ đi sâu vào "mổ xẻ" từng phương pháp một. Đầu tiên và cơ bản nhất chính là **Tỷ lệ tuyến tính (Linear Scaling)**, hay còn gọi là **Min-Max Scaling**.

### 1. Tỷ lệ tuyến tính (Linear Scaling)

Mục tiêu của phương pháp này là bóp (hoặc kéo giãn) toàn bộ tập dữ liệu của bạn để chúng nằm gọn trong một dải chuẩn cố định, phổ biến nhất là từ **0 đến 1**. Ưu điểm của nó là giữ nguyên vẹn khoảng cách tương đối (tỷ lệ) giữa các điểm dữ liệu với nhau.

**Công thức toán học:**

$$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$

*Trong đó:*

* $x$: Giá trị thô ban đầu cần chuyển đổi.
* $x'$: Giá trị mới sau khi đã chuẩn hóa.
* $x_{min}$ và $x_{max}$: Giá trị nhỏ nhất và lớn nhất trong toàn bộ tập dữ liệu đó.

---

#### Ví dụ thực tế

Hãy tưởng tượng bạn đang phân tích bộ chỉ số Tốc độ (Sprint Speed) của các cầu thủ, với dải chỉ số thực tế dao động từ 40 (chậm nhất) đến 130 (nhanh nhất).

* $x_{min} = 40$
* $x_{max} = 130$

Nếu một tiền vệ có tốc độ là 85, chúng ta sẽ đưa vào mô hình giá trị nào? Áp dụng công thức:

$$x' = \frac{85 - 40}{130 - 40} = \frac{45}{90} = 0.5$$

Vậy, chỉ số tốc độ 85 sẽ được quy đổi thành **0.5** trên thang điểm từ 0 đến 1. Bằng cách này, dù bạn có so sánh Tốc độ với Giá trị chuyển nhượng (lên tới hàng chục triệu), cả hai đều nằm trong dải [0, 1] và mô hình học máy sẽ không bị thiên vị.

---

#### Điểm yếu chí mạng: Outlier (Giá trị ngoại lai)

Linear Scaling hoạt động hoàn hảo khi dữ liệu phân bố đều đặn. Nhưng nếu bất ngờ xuất hiện một giá trị ngoại lai cực lớn (ví dụ do lỗi nhập liệu, tốc độ bị gõ nhầm thành 1000), thì $x_{max}$ sẽ trở thành 1000.

Hậu quả là mẫu số trong công thức trở nên quá lớn, khiến toàn bộ các cầu thủ có tốc độ bình thường (40 - 130) bị "đè bẹp", dồn cục lại thành một nhúm rất nhỏ sát vạch số 0. Lúc này, mô hình sẽ không thể phân biệt được cầu thủ chạy nhanh hay chạy chậm nữa.