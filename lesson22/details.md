
Bài học này nói về **Chuẩn hóa dữ liệu số (Numerical Data Normalization)** trong Machine Learning. Đây là một bước xử lý dữ liệu cực kỳ quan trọng để giúp mô hình của bạn học hiệu quả hơn.

Dưới đây là những nội dung cốt lõi bạn cần nắm:

## 1. Tại sao phải chuẩn hóa dữ liệu?

Hãy tưởng tượng bạn có hai đặc trưng: Tuổi tác (từ **0** đến **100**) và Thu nhập (từ **5,000** đến **1,000,000,000**). Sự chênh lệch quá lớn này sẽ khiến mô hình lầm tưởng Thu nhập quan trọng hơn Tuổi tác hàng triệu lần. Việc chuẩn hóa giúp đưa mọi thứ về cùng một hệ quy chiếu, mang lại các lợi ích sau:

* Giúp mô hình hội tụ nhanh hơn trong quá trình huấn luyện.
* Tránh hiện tượng mô hình dự đoán kém do chênh lệch tỷ lệ.
* Tránh "bẫy NaN" (khi các giá trị quá lớn vượt qua giới hạn lưu trữ số thực của máy tính).
* Giúp mô hình học được trọng số (weights) công bằng cho từng đặc trưng.

*Lưu ý quan trọng:* Nếu bạn chuẩn hóa một đặc trưng trong lúc huấn luyện (training), bạn bắt buộc phải áp dụng chuẩn hóa tương tự khi đưa ra dự đoán (prediction).

---

## 2. Các phương pháp chuẩn hóa phổ biến

### Tỷ lệ tuyến tính (Linear Scaling)

Phương pháp này nén các giá trị về một dải chuẩn xác định, thường là từ **0** đến **1** hoặc **-1** đến **1**.

Công thức toán học:


$$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$

**Khi nào nên dùng:**

* Biên độ dữ liệu (min và max) ổn định, không thay đổi theo thời gian.
* Dữ liệu phân bố khá đồng đều (dạng phẳng).
* Có rất ít hoặc không có giá trị ngoại lai (outliers).

### Tỷ lệ điểm Z (Z-score Scaling)

Điểm Z thể hiện một giá trị nằm cách giá trị trung bình bao nhiêu độ lệch chuẩn.

Công thức toán học:


$$z = \frac{x - \mu}{\sigma}$$

**Khi nào nên dùng:** Phù hợp nhất khi dữ liệu tuân theo phân phối chuẩn (hình quả chuông) hoặc gần giống phân phối chuẩn.

### Tỷ lệ Logarit (Log Scaling)

Phương pháp này tính logarit (thường là logarit tự nhiên) của các giá trị thô ban đầu.

**Khi nào nên dùng:** Rất hữu ích khi dữ liệu tuân theo phân phối hàm mũ (Power law distribution). Ví dụ điển hình là doanh số bán sách: phần lớn sách chỉ bán được vài trăm cuốn, trong khi một vài cuốn best-seller bán được hàng triệu cuốn. Việc lấy Logarit sẽ giúp kéo gần khoảng cách giữa **100** và **1,000,000** lại với nhau.

### Cắt xén (Clipping)

Kỹ thuật này thiết lập một mức trần (hoặc sàn) để giới hạn các giá trị ngoại lai. Ví dụ, nếu bạn đặt ngưỡng cắt là **4.0**, mọi giá trị lớn hơn **4.0** sẽ bị ép thành **4.0**.

**Khi nào nên dùng:** Khi bộ dữ liệu của bạn nhìn chung khá bình thường nhưng thỉnh thoảng lại xuất hiện những giá trị ngoại lai cực kỳ vô lý (extreme outliers).

---

## 3. Bảng đối chiếu nhanh

| Phương pháp | Hình dạng phân phối phù hợp | Dấu hiệu nhận biết |
| --- | --- | --- |
| **Linear scaling** | Phẳng (Flat-shaped) | Phân bố đồng đều khắp các dải giá trị. |
| **Z-score scaling** | Quả chuông (Bell-shaped) | Phân phối chuẩn, tập trung nhiều ở mức trung bình. |
| **Log scaling** | Đuôi dài (Heavy Tail-shaped) | Dữ liệu lệch hẳn, có một số ít giá trị cực lớn so với mặt bằng chung. |
| **Clipping** | Đa dạng | Chứa các giá trị ngoại lai đột biến làm hỏng dữ liệu chung. |