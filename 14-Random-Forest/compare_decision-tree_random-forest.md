

## Bài toán 1: Khi Cây Quyết Định (Decision Tree) là Vị Vua độc tôn

### Tình huống: Hệ thống Duyệt/Từ chối Vay Vốn Ngân Hàng

Bạn làm AI cho ngân hàng Techcombank. AI của bạn vừa đánh trượt hồ sơ vay 1 tỷ của một vị khách. Vị khách này làm ầm lên, gọi điện lên tổng đài mắng vốn và dọa kiện ngân hàng: *"Tại sao lương tôi 50 triệu/tháng mà các anh không cho tôi vay? Trả lời ngay!"*

**Nếu bạn dùng Random Forest:**

* Sếp hỏi bạn: *"Tại sao con AI lại từ chối ông này?"*
* Bạn toát mồ hôi: *"Dạ... em không biết. Em có 100 cái Cây (100 bác sĩ). 80 ông bảo từ chối, 20 ông bảo duyệt. Thuật toán tự chốt số đông là từ chối. Còn vì sao 80 ông kia từ chối thì... em chịu, nó rối quá em không dò lại được!"* (Đây gọi là thuật toán **Hộp Đen - Black-box**).
* 👉 **Hậu quả:** Ngân hàng dính phốt, sếp đuổi việc bạn vì không có lý do chính đáng để trả lời khách hàng và Ngân hàng Nhà nước.

**Nếu bạn dùng Decision Tree:**

* Bạn bình tĩnh mở bản đồ Cây quyết định ra (chỉ là 1 cái cây duy nhất). Bạn dò từ rễ xuống lá và chỉ thẳng tay vào màn hình:
* *"Dạ thưa sếp, luật của con AI nhà mình viết rất rõ: Dù lương > 40 triệu, nhưng khách hàng này có **số lần nợ chú ý > 2 lần trong năm ngoái**, nên nó tự động rẽ nhánh sang nút TỪ CHỐI."* (Đây gọi là **Hộp Trắng - White-box**).
* 👉 **Kết quả:** Sếp hài lòng, đem câu này ra cãi thắng khách hàng.

> **CHỐT LẠI THỨ 1:** Hãy dùng **Decision Tree** khi bài toán của bạn yêu cầu **Khả năng giải thích (Interpretability) cao**. Tức là Sếp, Khách hàng, hoặc Pháp luật bắt buộc bạn phải trả lời được câu hỏi: *"Tại sao AI lại quyết định như vậy?"*.

---

## Bài toán 2: Khi Rừng Ngẫu Nhiên (Random Forest) là Kẻ Hủy Diệt

### Tình huống: Bắt Giao dịch Lừa đảo (Fraud Detection) lúc 2h sáng

Vẫn ở ngân hàng đó, nhưng lần này bạn làm AI bảo mật thẻ tín dụng. Một cái thẻ của khách đang ở Việt Nam, tự nhiên quẹt mua iPhone 15 Pro Max trị giá 35 triệu ở tận... Châu Phi lúc 2h sáng.

**Nếu bạn dùng Decision Tree:**

* Con AI Cây Quyết Định này học vẹt (Overfitting) dữ liệu cũ. Nó thấy *"Ủa, khách này trước giờ toàn mua đồ xịn (thỏa mãn nhánh A), số dư thẻ còn nhiều (thỏa nhánh B) -> Bình thường, cho qua!"*.
* 👉 **Hậu quả:** Sáng dậy khách mất 35 triệu. Ngân hàng đền tiền.

**Nếu bạn dùng Random Forest:**

* Bạn tung Hội đồng 100 cái cây ra. Có cây check thói quen mua, có cây check vị trí địa lý, có cây check múi giờ. Dù có vài cây bị "ngu" cho qua, nhưng 90 cây còn lại la làng: *"Sai vị trí địa lý! Lệch múi giờ! Block ngay!"*. Số đông chiến thắng. Thẻ bị khóa ngay lập tức.
* Khách hàng sáng dậy thấy tin nhắn khóa thẻ. Họ gọi lên tổng đài hỏi: *"Tại sao khóa thẻ tôi?"*.
* Tổng đài viên đáp: *"Dạ hệ thống AI phát hiện rủi ro cao nên tạm khóa để bảo vệ tài sản ạ."* (Khách hàng thở phào cảm ơn, **chẳng ai quan tâm hỏi vặn lại xem cái AI đó dùng nhánh If/Else nào ở tầng dưới cả**).

> **CHỐT LẠI THỨ 2:** Hãy dùng **Random Forest** khi bài toán của bạn đặt **Độ chính xác (Accuracy)** lên hàng đầu, và không ai bắt bẻ bạn phải giải thích chi tiết lý do.

---

### Bảng Phong Thần: So sánh Nhanh

| Tiêu chí | Cây Quyết Định (Decision Tree) | Rừng Ngẫu Nhiên (Random Forest) |
| --- | --- | --- |
| **Bản chất** | 1 Chuyên gia duy nhất | Hội đồng 100 Chuyên gia |
| **Độ chính xác** | Trung bình (Dễ bị học vẹt - Overfitting) | **Rất cao** (Cực kỳ ổn định) |
| **Khả năng giải thích** | **Xuất sắc (Hộp Trắng)** - Vẽ được sơ đồ ra giấy | Yếu (Hộp Đen) - Quá nhiều cây, rối tinh rối mù |
| **Tốc độ chạy dự đoán** | **Nhanh như chớp** (Tốn ít RAM) | Chậm hơn một chút (Phải đợi 100 cây cùng tính) |
| **Khi nào dùng?** | Y khoa (Bác sĩ cần lý do chẩn đoán), Duyệt hồ sơ pháp lý, Giải thích cho sếp. | Phân tích Chứng khoán, Đề xuất sản phẩm E-commerce, Nhận diện hình ảnh. |

Về cơ bản, khi mới nhận một tập dữ liệu, kỹ sư AI luôn tuân theo quy tắc: **Chạy thử Decision Tree trước để xem cái khung luật lệ nó ra sao, sau đó mới ốp Random Forest vào để lấy độ chính xác cao nhất mang đi triển khai.**

