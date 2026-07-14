
Cũng giống như việc thiết lập các ràng buộc (constraints) chặt chẽ trong database, sử dụng các kiểu dữ liệu an toàn để kiểm soát luồng thông tin, hoặc validate payload từ client gửi lên server, các mô hình Machine Learning cũng cần một luồng dữ liệu đầu vào thật "sạch". Nếu đưa dữ liệu rác vào, mô hình sẽ học sai và đưa ra dự đoán lệch lạc ("Garbage in, Garbage out").

[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/numerical-data/scrubbing)

Dưới đây là tóm tắt các vấn đề cốt lõi mà tài liệu đề cập, được giải thích theo góc nhìn xử lý logic hệ thống:

### 1. Omitted values (Dữ liệu bị thiếu)

* **Vấn đề:** Các trường dữ liệu bị bỏ trống (tương đương với các giá trị `null` hoặc `undefined`). Ví dụ: Khảo sát viên quên ghi lại tuổi của một người.
* **Giải pháp:** Bạn có thể loại bỏ (drop) hoàn toàn dòng dữ liệu đó, hoặc sử dụng kỹ thuật **Imputation** (điền bù) – ví dụ như tự động điền bằng giá trị trung bình (mean) hoặc trung vị (median) của toàn bộ dữ liệu hợp lệ trong cột đó.

### 2. Duplicate examples (Dữ liệu trùng lặp)

* **Vấn đề:** Một bản ghi bị đẩy vào hệ thống nhiều lần do lỗi đồng bộ hoặc log lặp.
* **Giải pháp:** Cần chạy các script để lọc bỏ các bản ghi trùng lặp (tương tự như việc đảm bảo tính duy nhất của một Primary Key). Nếu không lọc, mô hình có thể bị "thiên vị" (bias) bởi các dữ liệu xuất hiện quá nhiều lần.

### 3. Out-of-range feature values (Giá trị vượt ngoài giới hạn)

* **Vấn đề:** Lỗi nhập liệu khiến thông số trở nên vô lý (outliers). Ví dụ: Nhiệt độ môi trường thực tế chỉ từ 10 đến 30 độ, nhưng do lỗi cảm biến lại ghi nhận thành 200 độ.
* **Giải pháp:** Viết các logic kiểm tra giới hạn (range validation) để bắt và loại bỏ các giá trị dị biệt này trước khi đưa vào mô hình phân tích.

### 4. Bad labels (Gán nhãn sai)

* **Vấn đề:** Dữ liệu mục tiêu bị con người phân loại sai (ví dụ: gán nhãn ảnh cây sồi thành cây phong).
* **Giải pháp:** Sử dụng các phương pháp thống kê để đánh giá mức độ đồng thuận giữa những người dán nhãn (raters), từ đó loại bỏ các nhãn có độ tin cậy thấp.

---
