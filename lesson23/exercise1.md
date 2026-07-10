

Giả sử bạn đang tối ưu hóa chiến thuật và phân tích đội hình trong FC Online (ví dụ như khi đang build team AC Milan hoặc Chelsea). Bạn có danh sách 9 cầu thủ với chỉ số tổng quát (OVR) đang lộn xộn như sau:

**Dữ liệu gốc (Chỉ số OVR):**
`102, 95, 118, 97, 106, 122, 105, 112, 96`

**Nhiệm vụ của bạn:**
Hãy áp dụng phương pháp **Phân vị (Quantile Bucketing)** để chia 9 cầu thủ này thành **3 giỏ (3 nhóm)** để hệ thống có thể đánh giá đồng đều.

**Gợi ý các bước để bạn giải:**

1. **Bước 1:** Trước tiên, bạn cần làm gì với mớ dữ liệu lộn xộn này? (Nhớ lại câu chuyện xếp hàng ở trường học nhé).
2. **Bước 2:** Với tổng cộng 9 cầu thủ và cần chia làm 3 nhóm, mỗi nhóm sẽ có bao nhiêu người? Hãy thực hiện "cắt" hàng.
3. **Bước 3:** Trình bày kết quả của bạn.

**Mẫu trình bày kết quả (bạn hãy điền vào chỗ trống nhé):**

* **Nhóm 1 (Dự bị):** Gồm các cầu thủ `[..., ..., ...]` ➔ Khoảng OVR từ ... đến ...
* **Nhóm 2 (Đội hình 2):** Gồm các cầu thủ `[..., ..., ...]` ➔ Khoảng OVR từ ... đến ...
* **Nhóm 3 (Đá chính):** Gồm các cầu thủ `[..., ..., ...]` ➔ Khoảng OVR từ ... đến ...

Bạn hãy lấy giấy nháp ra sắp xếp lại rồi gõ kết quả của 3 nhóm lên đây. Mình sẽ đóng vai thầy giáo chấm điểm xem bạn đã nắm chuẩn khái niệm chưa nhé!