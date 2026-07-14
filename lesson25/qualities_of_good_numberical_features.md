## NUMBERIC DATA - Bài 25 - THE RULES OF FEATURE'S NAME
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/numerical-data/qualities-of-good-numerical-features)
### 1. Đặt tên tường minh (Cần có đơn vị rõ ràng)

* **Tình huống:** Bạn nhờ người thợ đi chợ và dặn: *"Mua cho tôi 3 thịt"*.
* **Vấn đề:** Người thợ sẽ hoang mang không biết là 3 lạng, 3 ký, hay 3 miếng thịt? Nếu mua nhầm 3 ký thịt thay vì 3 lạng, bữa ăn sẽ hỏng bét.
* **Bài học Machine Learning:** Đừng bao giờ quăng cho mô hình một con số trơ trọi như `thời_gian: 851472000`. Hãy đặt tên là `thời_gian_tính_bằng_giây` hoặc `thời_gian_tính_bằng_năm`. Rõ ràng như việc dặn *"Mua cho tôi 3 ký thịt lợn"* vậy.

### 2. Kiểm tra tính hợp lý (Bắt lỗi sự cố)

* **Tình huống:** Bạn đi ăn bát phở giá 50.000 đồng. Lúc tính tiền, nhân viên đưa hóa đơn ghi **50.000.000 đồng** (do kẹt số 0 trên máy tính tiền).
* **Vấn đề:** Bạn nhìn vào là biết ngay con số này cực kỳ vô lý (outlier) và yêu cầu nhân viên sửa lại ngay chứ không đời nào rút ví ra trả 50 triệu.
* **Bài học Machine Learning:** Đừng bắt mô hình học từ những dữ liệu vô lý (như người dùng thọ 224 tuổi). Trước khi dạy nó, bạn phải làm người kiểm duyệt hóa đơn, nhặt hết những lỗi đánh máy ngớ ngẩn ra để "người thợ" không bị lú lẫn về giá trị thực tế của cuộc sống.

### 3. Xử lý "Giá trị ma thuật" (Không gượng ép thông tin)

* **Tình huống 1 (Số lượng đong đếm được):** Bạn hỏi vay tiền một người bạn, người đó quên mang ví. Thay vì nói thật là "Tôi quên ví", anh ta lại nói: *"Trong túi tôi đang có âm 1 triệu đồng"*. Nghe rất vô lý đúng không? Số âm mang ý nghĩa là anh ta đang mắc nợ bạn, chứ không phải là quên ví.
* **Cách giải quyết:** Giống như Machine Learning, hãy rành mạch 2 thông tin: Số tiền = `0 đồng` **VÀ** Tình trạng = `Quên mang ví` (cờ Boolean).


* **Tình huống 2 (Phân loại đồ đạc):** Bạn đang dọn nhà và có 3 cái tủ: *Tủ quần áo, Tủ sách, Tủ chén bát*. Tự nhiên bạn nhặt được một cái **búa đinh**. Nó không thuộc về tủ nào cả.
* **Sai lầm:** Nhắm mắt nhét đại cái búa vào "Tủ quần áo". Mô hình học máy cũng vậy, nếu bạn ép dữ liệu vào một nhóm sai, nó sẽ học ra quy luật sai.
* **Cách giải quyết:** Lấy một cái thùng carton trống, dán nhãn là **"Đồ linh tinh"** (Missing Category) và vứt cái búa vào đó. Gọn gàng, hợp logic và không làm hỏng quy luật của các tủ khác.
