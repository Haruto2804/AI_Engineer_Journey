Khái niệm "Phân vị" (Quantile) nghe có vẻ sặc mùi toán học, nhưng bản chất của nó lại vô cùng đơn giản và thực tế. Hãy quên đi máy móc và dữ liệu khô khan, chúng ta cùng tưởng tượng về một câu chuyện ở **trường học** nhé.

Tưởng tượng bạn là thầy hiệu trưởng. Trường của bạn có **100 học sinh**, và bạn cần chia các em vào 4 lớp học (Lớp A, B, C, D) dựa trên mức **tiền tiêu vặt** mỗi ngày của các em.

Đây chính là lúc sự khác biệt giữa hai phương pháp lộ diện:

## 1. Cách chia cũ: Khoảng cách đều (Equal Intervals)

Bạn chọn cách chia lấy mức tiền cao nhất (ví dụ 100 ngàn) chia đều cho 4 lớp:

* **Lớp A:** Những em có từ 0 - 25 ngàn
* **Lớp B:** Những em có từ 25 - 50 ngàn
* **Lớp C:** Những em có từ 50 - 75 ngàn
* **Lớp D:** Những em có từ 75 - 100 ngàn

**Thực tế phũ phàng:** Ở lứa tuổi học sinh, đa số các em chỉ có khoảng 10 - 20 ngàn ăn sáng.
Kết quả là **Lớp A bị nhét tận 97 em** ngồi chật cứng! Trong khi đó, **Lớp D chỉ có đúng 1 em** nhà giàu.

Đối với Trí tuệ nhân tạo (AI), học sinh chính là "dữ liệu". Lớp D có quá ít dữ liệu (chỉ 1 người), AI sẽ không thể rút ra được đặc điểm hay quy luật chung gì từ lớp này cả.

---

## 2. Cách chia mới: Phân vị (Quantile Bucketing)

Rút kinh nghiệm, lần này bạn quyết định không chia theo các mốc tiền nữa. Mục tiêu của bạn bây giờ là: **Lớp nào cũng phải có đúng 25 em học sinh** để thầy cô dễ quản lý.

Bạn yêu cầu 100 học sinh xếp thành một hàng dọc, từ người ít tiền nhất đến người nhiều tiền nhất. Sau đó bạn đi dọc hàng và đếm:

* Đếm đủ **25 em đầu tiên** ➔ Cắt ngang! Gom vào **Lớp A**. *(Có thể lớp này chỉ gồm các em có 0 - 10 ngàn).*
* Đếm tiếp **25 em tiếp theo** ➔ Cắt ngang! Gom vào **Lớp B**. *(Gồm các em từ 11 - 15 ngàn).*
* Đếm tiếp **25 em tiếp theo** ➔ Cắt ngang! Gom vào **Lớp C**. *(Gồm các em từ 16 - 30 ngàn).*
* Và **25 em cuối cùng** ➔ Gom hết vào **Lớp D**. *(Nhóm này dao động cực lớn, có em 31 ngàn, có em lên tới 100 ngàn).*

**Điều kỳ diệu xảy ra:**
"Bề rộng" số tiền của mỗi lớp là không hề giống nhau. Lớp A dao động rất hẹp (chênh nhau 10 ngàn), nhưng Lớp D lại dao động rất rộng (chênh nhau gần 70 ngàn). **Nhưng số lượng học sinh trong mỗi lớp lại bằng nhau tăm tắp!**

---

## Tóm lại: Tại sao AI lại "nghiện" Phân vị?

* **Phân vị (Quantile)** thực chất chỉ là việc sắp xếp dữ liệu theo thứ tự, đếm đủ số lượng thì gom vào một "giỏ".
* Việc này đảm bảo **giỏ nào cũng chứa một lượng dữ liệu (examples) như nhau**.
* Nhờ vậy, AI có đủ "tài liệu học tập" để phân tích đều đặn về mọi nhóm người, kể cả nhóm phổ biến nhất hay nhóm hiếm hoi nhất, mà không đưa ra những dự đoán sai lệch vì thiếu kinh nghiệm.

