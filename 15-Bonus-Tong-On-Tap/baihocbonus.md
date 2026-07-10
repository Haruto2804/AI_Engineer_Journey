Bạn thấy chưa? Chỉ cần 3 "con sâu làm rầu nồi canh" (dữ liệu nhiễu) mà độ chính xác và bảng báo cáo đã thay đổi rõ rệt. Đây chính là thực tế tàn khốc của dữ liệu đời thực!

### Tại sao con số lại "nhảy múa"?

Khi bạn thêm 3 người này vào, con AI bắt đầu bị "bối rối":

1. **Sự mâu thuẫn:** Trước đây, AI đã học được quy luật *"Lương cao + OT thấp = Ở lại"*. Bây giờ, nhân viên nhiễu `[50, 0, 5]` (Lương cao, OT thấp, nhưng lại Nghỉ việc) đã **phá vỡ hoàn toàn logic** mà AI đã dày công học được.
2. **Sự áp đảo của dữ liệu nhiễu:** Trong tập dữ liệu nhỏ (chỉ 15 người), 3 người nhiễu chiếm tới 20% tổng dữ liệu. Nó không còn là "ngoại lệ" nữa mà đã trở thành một phần của quy luật mới. Con AI buộc phải điều chỉnh lại báo cáo để "cố gắng giải thích" cho cả 3 người bất thường này.

### Bài học cho Kỹ sư AI Architect:

Đây là lúc bạn nhận ra tại sao các công ty lớn lại trả lương rất cao cho công đoạn **Data Cleaning (Làm sạch dữ liệu)** trước khi đưa vào mô hình:

* **Không bao giờ tin tưởng mù quáng vào kết quả:** Nếu con số `Feature Importance` nhảy vọt hoặc thay đổi 180 độ chỉ vì vài dòng dữ liệu, có nghĩa là **Mô hình của bạn chưa đủ ổn định** hoặc **Dữ liệu của bạn có quá nhiều "rác"**.
* **Phân tích ngoại lệ (Outliers):** Một Kỹ sư giỏi sẽ không gộp chung 3 người nhiễu đó vào ngay. Họ sẽ tách riêng 3 người đó ra, kiểm tra xem: *"Tại sao lương cao, nhàn hạ mà vẫn nghỉ? Có phải họ bị trầm cảm, hay bị đối thủ săn đầu người với mức lương gấp đôi?"*.
* **Chiến lược xử lý:** Sau khi hiểu lý do, bạn sẽ hoặc là **loại bỏ** họ nếu đó là lỗi nhập liệu, hoặc là **tạo thêm cột dữ liệu mới** (ví dụ: cột "Bị đối thủ chèo kéo") để giải thích cho sự bất thường đó.

---

### Chúc mừng bạn!

Bạn đã hoàn thành khóa "Nhập môn Rừng Ngẫu Nhiên" một cách xuất sắc. Bạn đã biết:

* Cách tạo rừng (`RandomForest`).
* Cách độ xe (`GridSearchCV`).
* Cách bức cung AI (`Feature Importance`).
* Và quan trọng nhất: **Biết nghi ngờ dữ liệu**.

Bạn đã sẵn sàng để chuyển sang **Bài 16: Hồi quy (Regression)** – Nơi chúng ta không còn làm bài toán "Có/Không" nữa, mà bắt đầu **tiên đoán các con số tài chính**? Đây là kỹ năng giúp bạn làm việc trực tiếp với các bộ phận Tài chính, Kinh doanh của doanh nghiệp đấy!

Bạn đã sẵn sàng bước vào thế giới của "Tiên tri số học" chưa?