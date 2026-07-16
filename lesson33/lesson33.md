## Bài 33: Datasets: Dividing the original dataset
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets)

Bài học này nói về một nguyên tắc vô cùng quen thuộc nếu bạn đã từng làm việc với các quy trình kiểm thử phần mềm (software verification) hoặc phân tích test-case (như white-box testing). Cốt lõi của vấn đề là: **Tuyệt đối không dùng chung dữ liệu để vừa dạy vừa kiểm tra AI.**

Dưới đây là nội dung cốt lõi được "dịch" lại theo tư duy của một kỹ sư phát triển phần mềm để bạn dễ nắm bắt nhất:

### 1. Tại sao chia 2 phần (Train & Test) lại không đủ tốt?

Ban đầu, trực giác mách bảo chúng ta chỉ cần chia dữ liệu làm 2:

* Một nửa để dạy AI học (Training).
* Một nửa để kiểm tra xem nó học đúng không (Test).

**Vấn đề:** Trong quá trình phát triển, bạn sẽ liên tục kiểm tra AI trên tập Test, thấy kết quả chưa tốt thì quay lại sửa cấu hình (đổi hyperparameter, thêm/bớt tính năng). Việc lặp đi lặp lại vòng lặp này khiến AI vô tình "học vẹt" luôn cả những đặc điểm riêng biệt của tập Test. Kết quả là điểm test rất cao, nhưng khi triển khai thực tế (Production) thì mô hình lại chạy rất tệ.

### 2. Quy trình chuẩn: Chia 3 phần (Train - Val - Test)

Để giải quyết bài toán trên, các kỹ sư Machine Learning sử dụng cơ chế chia 3, tương đương với quy trình 3 môi trường cơ bản khi làm web (Dev - Staging - Production):

* **Tập huấn luyện (Training set) - Môi trường Dev:**
Đây là khối lượng dữ liệu lớn nhất dùng để trực tiếp dạy cho AI cách nhận diện mẫu (pattern).
* **Tập xác thực (Validation set) - Môi trường Staging/QA:**
Trong lúc huấn luyện, bạn dùng tập này để test thử và điều chỉnh các thông số của mô hình (tweak model). Quá trình tinh chỉnh này cứ lặp đi lặp lại cho đến khi mô hình hoạt động ổn định trên Validation set.
* **Tập kiểm thử (Test set) - Môi trường Production:**
Đây là "bài thi tốt nghiệp" cuối cùng. Dữ liệu này được cất kỹ, hoàn toàn chưa từng được AI hay lập trình viên nhìn thấy trong lúc điều chỉnh mô hình. Nó chỉ được dùng để đánh giá khách quan một lần cuối xem mô hình thực sự mạnh đến đâu trước khi đưa vào ứng dụng thực tế.

> **Lưu ý:** Giống như các test-case sẽ mất dần giá trị nếu bị sử dụng đi sử dụng lại quá nhiều, tập Validation và Test cũng sẽ bị "mòn" (wear out). Cách tốt nhất là liên tục cập nhật thêm dữ liệu mới để làm mới các tập kiểm thử này.

### 3. Cạm bẫy "Trùng lặp dữ liệu" (Data Leakage)

Một bài test công bằng là bài test không có câu hỏi nào bị lộ từ trước. Bài học đưa ra một tình huống cảnh báo cực kỳ quan trọng:

Giả sử bạn làm một AI lọc thư rác (Spam). AI đạt điểm chính xác 99% trên cả tập Train và tập Test. Quá tuyệt vời? Không hề. Khi kiểm tra lại, bạn phát hiện ra trong Database có những email rác bị **lưu trùng lặp (duplicate)**. Một bản nằm ở tập Train, một bản y hệt lọt vào tập Test. AI chẳng hề thông minh, nó chỉ đơn giản là đã "nhớ mặt" cái email đó từ lúc học rồi.

**Tiêu chuẩn của một tập Test/Validation chất lượng:**

* **Đủ lớn:** Để mang ý nghĩa thống kê (không phải đoán bừa mà trúng).
* **Đại diện được cho số đông:** Không mang đặc tính quá khác biệt so với tập Training hay dữ liệu thực tế.
* **KHÔNG CÓ DỮ LIỆU TRÙNG LẶP** với tập Training. Khi bạn xử lý, làm sạch hoặc biến đổi tính năng (transform) ở tập Train thế nào, hãy nhớ áp dụng chung bộ logic đó cho tập Test và Validation.