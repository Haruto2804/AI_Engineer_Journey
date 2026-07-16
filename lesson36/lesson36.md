
## Bài 36: Overfitting
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting)

Ở Bài học này đưa chúng ta đến thẳng "kẻ thù số 1" của mọi kỹ sư Machine Learning: **Overfitting (Học vẹt hay Quá khớp)**.

Để dễ hình dung nhất, hãy tưởng tượng bạn đang cất công xây dựng một đội hình Chelsea cực kỳ tâm huyết trong FC Online. Bạn thiết lập chiến thuật tạt cánh đánh đầu (cross-and-header) với các chỉ số chiến thuật được tinh chỉnh tỉ mỉ từng li từng tí chỉ để đá thắng... đúng một người bạn duy nhất.

Khi đá giao hữu với người bạn đó, tiền đạo cắm của bạn như Drogba hay Shevchenko luôn chọn đúng điểm rơi, ghi bàn liên tục. Đội hình này đá 10 trận thắng cả 10 (Điểm số trên **Training Set** đạt tuyệt đối).

Tuy nhiên, khi bạn mang nguyên đội hình và chiến thuật đó vào đá Xếp hạng (Rank) gặp vô vàn các đối thủ khác nhau, bạn bị hủy diệt hoàn toàn. Chiến thuật của bạn đã bị **Overfit**. Nó được thiết kế quá mức phức tạp chỉ để "bắt bài" một phong cách duy nhất, dẫn đến việc mất đi tính linh hoạt (Generalization) khi đối đầu với những môi trường mới.

Dưới đây là các khái niệm cốt lõi bạn cần nắm từ bài học này:

### 1. Ba trạng thái của một mô hình AI

Giống như việc tinh chỉnh chiến thuật, mô hình AI sẽ rơi vào 3 trạng thái:

* **Underfitting (Chưa khớp):** Mô hình quá đơn giản hoặc học chưa đủ sâu. Nó đưa ra dự đoán tệ hại ngay cả trên dữ liệu huấn luyện (Đá với bạn cũng thua, mà đá Rank cũng thua).
* **Overfitting (Quá khớp):** Mô hình ghi nhớ chính xác từng chi tiết vụn vặt và nhiễu loạn của dữ liệu huấn luyện, nhưng lại mù tịt với dữ liệu thực tế (Làm vua phòng thí nghiệm, ra đường làm loser).
* **Good Fit (Khái quát hóa tốt):** Mục tiêu tối thượng. Mô hình đủ thông minh để nhận ra quy luật chung và hoạt động ổn định trên cả dữ liệu cũ lẫn mới (Ví dụ: một chiến thuật phòng ngự phản công tốc độ cao được cân bằng tốt, gặp đối thủ nào cũng có thể linh hoạt ứng biến).

### 2. Bắt bệnh Overfitting bằng Đồ thị (Generalization Curve)

Làm sao để biết AI của bạn đang bị "học vẹt" trong lúc huấn luyện? Các kỹ sư sẽ nhìn vào một biểu đồ gọi là **Đường cong khái quát hóa (Generalization Curve)**, bao gồm hai đường Loss (độ lỗi) chạy song song:

* **Giai đoạn đầu:** Cả đường Loss của tập Train và tập Validation đều giảm xuống. Đây là dấu hiệu AI đang học tốt.
* **Điểm bùng phát (Divergence):** Đột nhiên, đường Loss của tập Train tiếp tục cắm đầu đi xuống (AI ngày càng thuộc bài), nhưng đường Loss của tập Validation lại... ngóc đầu đi lên!

Ngay khoảnh khắc hai đường này tách nhau ra và đi ngược chiều, đó là tiếng chuông báo động: AI đã bắt đầu quá trình "học vẹt" và mất đi khả năng xử lý dữ liệu mới.

### 3. Nguyên nhân gây ra Overfitting

Căn bệnh này thường xuất phát từ hai lý do chính:

* **Mô hình quá phức tạp:** Bạn cấp cho AI một bộ não quá khổng lồ để giải quyết một bài toán quá đơn giản, khiến nó tự vẽ ra những quy luật loằng ngoằng không có thật.
* **Dữ liệu không đại diện cho thực tế:** Dữ liệu huấn luyện của bạn bị thiên lệch, không bao quát được những biến động của môi trường thực (giống như việc chỉ luyện tập với một đối thủ duy nhất).

### 4. Các điều kiện để mô hình hoạt động tốt ngoài thực tế

Để AI không bị bỡ ngỡ khi ra khỏi phòng thí nghiệm, dữ liệu của bạn phải tuân thủ 3 nguyên tắc vàng:

* **Độc lập và phân phối đồng nhất (i.i.d):** Các mẫu dữ liệu không được ảnh hưởng lẫn nhau.
* **Tính dừng (Stationarity):** Bản chất của dữ liệu không được thay đổi quá chóng mặt theo thời gian. Nếu bạn dự đoán xu hướng thời trang thập niên 90 và đem áp dụng cho năm 2026, mô hình chắc chắn sụp đổ vì thị hiếu đã thay đổi.
* **Phân phối đồng đều ở các tập (Train/Val/Test):** Đặc điểm thống kê của dữ liệu học phải giống với dữ liệu thi thử và dữ liệu thi thật.