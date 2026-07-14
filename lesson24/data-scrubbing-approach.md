Để xử lý triệt để các lỗi dữ liệu này, chúng ta cần áp dụng các chiến lược từ cơ bản (xóa bỏ) đến nâng cao (biến đổi hoặc dùng thuật toán bù đắp). Dưới đây là các phương hướng giải quyết cụ thể cho từng trường hợp:

## 1. Xử lý Dữ liệu bị thiếu (Omitted values)

Khi một bản ghi bị thiếu dữ liệu (tương đương với các giá trị `null` hoặc `NaN`), bạn có hai hướng tiếp cận chính:

* **Xóa bỏ (Deletion):**
* **Xóa dòng (Drop Rows):** Nếu tập dữ liệu của bạn rất lớn nhưng số dòng bị thiếu dữ liệu chỉ chiếm 1-2%, cách nhanh nhất là xóa hẳn các dòng đó (tương tự như việc bạn query bỏ qua các record `null` trong database).
* **Xóa cột (Drop Columns):** Nếu một cột (feature) có đến 60-80% giá trị bị trống và không mang nhiều ý nghĩa quyết định, tốt nhất là loại bỏ hoàn toàn cột đó khỏi mô hình.


* **Điền bù (Imputation):**
* **Dùng giá trị thống kê:** Điền vào chỗ trống bằng giá trị Trung bình (Mean) hoặc Trung vị (Median) của toàn bộ dữ liệu trong cột đó. Trung vị thường an toàn hơn nếu cột có chứa các giá trị quá lớn hoặc quá nhỏ.
* **Dùng giá trị mặc định:** Thay thế khoảng trống bằng một giá trị hằng số (ví dụ: gán `-1` hoặc chữ `"Unknown"`) để mô hình tự nhận diện rằng đây là một nhóm "dữ liệu không xác định".
* **Dự đoán điểm khuyết (Advanced):** Dùng một thuật toán Machine Learning khác để dự đoán và điền vào chỗ trống dựa trên sự liên kết với các cột dữ liệu đã có.



## 2. Khử Dữ liệu trùng lặp (Duplicate examples)

Dữ liệu lặp lại nhiều lần sẽ làm sai lệch trọng số của mô hình.

* **Deduplication (Lọc trùng tuyệt đối):** Loại bỏ các dòng giống nhau hoàn toàn 100% ở tất cả các cột. Việc này giống hệt như dùng lệnh `SELECT DISTINCT` trong SQL để chỉ giữ lại các bản ghi duy nhất.
* **Xử lý trùng lặp bán phần:** Đôi khi dữ liệu có cùng ID nhưng khác nhau ở thời gian cập nhật (timestamp). Bạn cần thiết lập logic gom nhóm (group by) và chỉ giữ lại bản ghi mới nhất hoặc bản ghi có chất lượng tốt nhất.

## 3. Quản lý Giá trị vượt ngoài giới hạn (Out-of-range / Outliers)

Những điểm dữ liệu dị biệt này làm xô lệch nghiêm trọng các thuật toán tính toán.

* **Cắt xén (Clipping / Winsorizing):** Thiết lập một "trần" (cap) và "sàn" (floor). Bất kỳ giá trị nào vượt ngưỡng sẽ bị ép về ngưỡng đó. Ví dụ: Nếu độ tuổi bị nhập lỗi thành `250`, bạn có thể thiết lập quy tắc "bất cứ giá trị nào > 100 đều được gán bằng 100".
* **Biến đổi toán học (Log Transformation):** Áp dụng hàm logarit để "thu nhỏ" khoảng cách của các con số siêu lớn, giúp phân phối dữ liệu trở nên mượt mà và tập trung hơn.
* **Chia thùng (Binning):** Thay vì để dữ liệu dạng số thực (ví dụ tuổi từ 1 đến 100), bạn gộp chúng thành các danh mục rời rạc (ví dụ: Nhóm `0-18`, `19-35`, `36-60`, `60+`). Việc này giúp mô hình giảm bớt độ nhạy cảm với các con số cực đoan.

## 4. Khắc phục Gán nhãn sai (Bad labels)

Nhãn sai nguy hiểm nhất vì nó trực tiếp dạy mô hình học những điều vô lý.

* **Bỏ phiếu đa số (Majority Vote):** Nếu sử dụng con người để dán nhãn, hãy cho 3-5 người độc lập đánh giá cùng một dữ liệu. Nhãn cuối cùng được chọn là nhãn được nhiều người đồng thuận nhất.
* **Đánh dấu để kiểm tra lại (Flagging):** Chạy thử một mô hình sơ bộ. Nếu mô hình dự đoán xác suất một nhãn là 99% nhưng nhãn thực tế ghi trong dữ liệu lại hoàn toàn ngược lại, hãy viết script trích xuất riêng các dòng đó ra để con người review lại thủ công (vì rất có khả năng dữ liệu ban đầu đã bị nhập sai).