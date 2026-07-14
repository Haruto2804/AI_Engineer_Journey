

---

### 1. Feature Cross là cái gì? (Hiểu đơn giản nhất)

> **Feature Cross** là việc "nhân" (hoặc kết hợp) 2 hay nhiều đặc trưng lại với nhau để tạo ra một đặc trưng mới đại diện cho **sự kết hợp đồng thời**.

* **Ví dụ thực tế:**
* Bạn có cột 1: **Loại mép lá** (gồm: nhẵn, răng cưa, thùy).
* Bạn có cột 2: **Cách mọc lá** (gồm: mọc đối, mọc so le).
* Nếu mô hình chỉ nhìn riêng lẻ từng cột, nó rất khó phân biệt loại cây. Nhưng nếu bạn **cross** chúng lại, bạn sẽ có các tổ hợp mới như: `Mép_nhẵn_Mọc_đối`, `Mép_răng_cưa_Mọc_so_le`,...
* Nếu một chiếc lá vừa có *mép thùy* vừa *mọc so le*, thì ô `Mép_thùy_Mọc_so_le` sẽ bằng **1**, tất cả các ô tổ hợp khác bằng **0**.



### 2. Tại sao phải dùng nó?

* **Giải quyết bài toán phi tuyến (Nonlinear):** Mô hình tuyến tính bình thường chỉ vẽ được đường thẳng. Nhưng khi bạn nhân các đặc trưng lại với nhau (giống như $x_1 \times x_2$), bạn đã gián tiếp giúp mô hình tuyến tính học được các đường cong, đường cắt phức tạp để phân loại dữ liệu chính xác hơn.
* **Mã hóa sự tương tác:** Có những thứ đi riêng lẻ thì vô nghĩa, nhưng đi chung với nhau thì cực kỳ chuẩn xác (Ví dụ: `Quận = Quận 1` và `Loại nhà = Biệt thự` $\rightarrow$ giá nhà chắc chắn cực kỳ đắt).

### 3. Điểm yếu chết người cần lưu ý (Be careful!)

* **Bùng nổ dữ liệu thưa (Sparsity):** Nếu bạn lấy một cột có 100 giá trị (như 100 quận/huyện) nhân với một cột có 200 giá trị (200 ngành nghề), đặc trưng mới sau khi cross sẽ có tới **20.000 cột** ($100 \times 200$).
* Hầu hết các ô trong 20.000 cột này sẽ toàn là số `0` (dữ liệu cực kỳ thưa thớt), làm ngốn RAM và khiến mô hình cực kỳ nặng nề.

---

**Chốt lại để nhớ:**

* **Feature Cross** = Nhân các đặc trưng với nhau để tạo ra tổ hợp mới giúp mô hình tuyến tính học tốt hơn.
* **Mặt trái:** Rất dễ làm phình to số lượng cột dữ liệu (gây thưa thớt dữ liệu) nếu lạm dụng bừa bãi.
