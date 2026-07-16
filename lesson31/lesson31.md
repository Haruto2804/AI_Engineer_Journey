## Bài 31: Labels

[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/labels)
## 📌 Các Điểm Cốt Lõi Bạn Cần Nhớ

### 1. Nhãn trực tiếp (Direct labels) vs Nhãn thay thế (Proxy labels)

* **Direct labels (Nhãn trực tiếp):** Là nhãn trùng khớp hoàn toàn với mục tiêu mà mô hình muốn dự đoán.
* *Ví dụ:* Bạn muốn dự đoán một người có sở hữu xe đạp hay không, và trong database có sẵn cột dữ liệu `so_huu_xe_dap` (Đúng/Sai). Đây là lựa chọn tốt nhất.


* **Proxy labels (Nhãn thay thế):** Là loại nhãn gần giống, có mối liên hệ chặt chẽ nhưng **không hoàn toàn trùng khớp** với mục tiêu dự đoán. Chúng ta buộc phải dùng proxy khi dữ liệu thực tế không có nhãn trực tiếp hoặc nhãn trực tiếp không thể biểu diễn dưới dạng số (float) để tính toán.
* *Mối nguy:* Mô hình dùng nhãn proxy chỉ đạt hiệu quả tốt nếu mối liên hệ giữa nhãn proxy đó và mục tiêu thực tế đủ mạnh.



### 2. Dữ liệu do con người tạo ra (Human-generated data)

Khi gán nhãn dữ liệu, chúng ta thường phân vân giữa việc thuê người làm hay để máy tự động quét.

* **Ưu điểm của con người:** Có thể xử lý các tác vụ phức tạp, đòi hỏi tư duy sâu hoặc ngữ cảnh mà AI chưa đủ trình độ (ví dụ: thẩm định sắc thái ngôn ngữ, chẩn đoán hình ảnh y tế chuyên sâu). Quá trình này giúp chúng ta xây dựng bộ tiêu chí chấm điểm (criteria) rõ ràng.
* **Nhược điểm:** Tốn kém chi phí, mất thời gian và dễ có sai số (người chấm có lúc mệt mỏi, nhầm lẫn).
* *Giải pháp:* Thường phải cho nhiều người cùng chấm một tập dữ liệu để kiểm tra chéo, đồng thời bản thân người quản lý dự án nên tự tay gắn thử (khoảng 1000 mẫu) để đánh giá độ lệch.

---

## 📝 Giải bài tập tình huống (Exercise)

**Tình huống:**

* Công ty muốn gửi mã giảm giá 15% mua mũ bảo hiểm cho **những người sở hữu xe đạp**.
* Mục tiêu mô hình: Dự đoán xem ai đang sở hữu xe đạp.
* Dữ liệu **không có** cột `bike owner` (chủ xe đạp), nhưng **có** cột `recently bought a bicycle` (vừa mới mua xe đạp gần đây).

*Hỏi: Cột `recently bought a bicycle` là một nhãn thay thế tốt (Good proxy label) hay tồi (Poor proxy label) cho mô hình này?*

**Đáp án đúng:** **Poor proxy label** (Một nhãn thay thế tồi/không phù hợp).

> **Giải thích tại sao lại là "Poor":**
> Hãy chú ý kỹ đến **mục đích thương mại** của bài toán: Gửi coupon giảm giá mua **mũ bảo hiểm**.
> * Một người *vừa mới mua xe đạp* rất có khả năng họ chưa có mũ bảo hiểm, hoặc họ đang có nhu cầu mua sắm phụ kiện đi kèm ngay lập tức. Đây là đối tượng tiềm năng để gửi coupon.
> * Nhưng nếu bạn dùng nhãn `recently bought a bicycle` làm proxy đại diện cho *toàn bộ những người sở hữu xe đạp*, mô hình sẽ bỏ sót một lượng lớn khách hàng: những người **đã sở hữu xe đạp từ lâu** nhưng bây giờ mũ của họ bị hỏng/cũ và họ cần mua mũ mới.
> * Ngược lại, những người vừa mua xe có thể đã mua luôn combo mũ bảo hiểm lúc ở cửa hàng rồi. Vì vậy, nhãn này phản ánh sai lệch hành vi và nhu cầu thực tế của tệp "chủ sở hữu xe đạp", khiến việc gửi coupon giảm giá không tối ưu.
> 
> 

---

