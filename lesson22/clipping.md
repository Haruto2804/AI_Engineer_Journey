Chào mừng bạn đến với trùm cuối của các phương pháp chuẩn hóa: **Cắt xén (Clipping)**.

Phương pháp này có một cách tiếp cận cực kỳ "cứng rắn" và trực diện. Thay vì dùng các công thức toán học phức tạp để biến đổi toàn bộ dữ liệu như 3 cách trước, Clipping chỉ đơn giản là đặt ra các **giới hạn (ngưỡng trần và ngưỡng sàn)**.

### 4. Cắt xén (Clipping)

Ý tưởng của Clipping là: Nếu bộ dữ liệu của bạn có 99% là rất đẹp và chuẩn mực, nhưng tự nhiên lòi ra 1% là những con số vô lý (extreme outliers), thì chúng ta không cần phải thay đổi 99% kia làm gì cho mệt. Chúng ta chỉ "xử lý" 1% đó thôi.

**Cách hoạt động:**

* Bạn chọn một **giá trị trần (Max)** và/hoặc một **giá trị sàn (Min)**.
* Nếu một điểm dữ liệu **vượt quá trần**, nó sẽ bị ép gán bằng đúng giá trị trần.
* Nếu một điểm dữ liệu **thấp hơn sàn**, nó sẽ bị kéo lên bằng đúng giá trị sàn.
* Các điểm nằm giữa trần và sàn được **giữ nguyên không đổi**.

**Công thức:**


$$x' = \max(min\_value, \min(x, max\_value))$$

---

#### Ví dụ thực tế

Giả sử bạn thu thập dữ liệu "Số phòng trung bình mỗi người" của các căn nhà.

* 99% dữ liệu loanh quanh từ **1 đến 3 phòng/người**.
* Đột nhiên, có vài biệt thự siêu lớn báo cáo là **20 phòng/người** hoặc **50 phòng/người**.

Nếu không xử lý, mô hình sẽ bị phân tâm bởi những biệt thự 50 phòng này. Tuy nhiên, nếu bạn cắt xén (clip) giới hạn trần ở mức **4.0**, điều gì sẽ xảy ra?
Mọi căn nhà có trên 4 phòng/người (dù là 5, 20 hay 50) đều sẽ được ghi nhận vào dữ liệu với con số là **4.0**. Trên biểu đồ, bạn sẽ thấy một "ngọn đồi" nhỏ nhô lên ngay tại mốc 4.0, tập hợp tất cả các giá trị bị cắt gọt.

