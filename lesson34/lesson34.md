## Bài 34: TRANSFORMING DATA
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/transforming-data)
### 1. Biến chữ thành số (Categorical Data)

Mọi dữ liệu dạng chuỗi (string) đều vô nghĩa với AI.

* **Ví dụ:** Dữ liệu của bạn có cột "Tên đường" với các giá trị như "Broadway" hay "Nguyễn Huệ". Bạn không thể đưa thẳng chữ "Broadway" vào mô hình.
* **Giải pháp:** Bạn bắt buộc phải dùng các thuật toán biến đổi để ánh xạ các chữ cái này thành các con số thực (ví dụ: Broadway = 1.0, Nguyễn Huệ = 2.0).

### 2. Ép khuôn các con số (Normalization - Chuẩn hóa)

Ngay cả khi dữ liệu của bạn đã là con số (ví dụ: Giá nhà là 5.000.000.000 VNĐ, số phòng ngủ là 3), bạn vẫn phải biến đổi chúng.

* **Vấn đề:** Sự chênh lệch quá lớn giữa các con số (5 tỷ và 3) sẽ khiến thuật toán bị nhiễu và học rất chậm.
* **Giải pháp:** Sử dụng kỹ thuật Chuẩn hóa (Normalization) để "ép" tất cả các giá trị khổng lồ này về một thang đo nhỏ và đồng nhất (thường là từ 0 đến 1, hoặc từ -1 đến 1). Điều này giúp AI tiêu hóa dữ liệu trơn tru hơn rất nhiều.

### 3. Lấy mẫu khi có quá nhiều dữ liệu (Sampling)

Nếu hệ thống của bạn có hàng tỷ dòng dữ liệu, việc ôm đồm nhét tất cả vào huấn luyện sẽ làm sập máy hoặc tốn chi phí máy chủ khổng lồ.

* **Giải pháp:** Hãy chọn ra một tập con (subset) mang tính đại diện và liên quan nhất đến mục tiêu dự đoán của bạn để huấn luyện. Không phải cứ nhiều dữ liệu là tốt, dữ liệu phải "chất lượng".

### 4. Lọc bỏ thông tin cá nhân (PII - Personally Identifiable Information)

Đây là quy tắc sống còn về đạo đức và pháp lý.

* **Nguyên tắc:** Một bộ dữ liệu tốt là bộ dữ liệu đã được xóa sạch các thông tin định danh cá nhân (như Tên thật, số điện thoại, CCCD, địa chỉ nhà...). Việc này vừa bảo vệ quyền riêng tư của người dùng, vừa tránh cho AI bị học những định kiến (bias) không đáng có từ dữ liệu cá nhân.