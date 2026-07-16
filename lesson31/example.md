## Ví dụ thực tế

Mục tiêu tối thượng của công ty là: **Bán được nhiều mũ bảo hiểm xe đạp nhất có thể bằng cách gửi mã giảm giá (coupon).**

Để gửi đúng người, mô hình cần tìm ra: **Ai là người đang sở hữu xe đạp?**

Nhưng trong dữ liệu không có nhãn trực tiếp này, nên họ định dùng nhãn thay thế (proxy) là: **Người vừa mới mua xe đạp gần đây**.

Lý do nhãn này bị đánh giá là **Poor proxy label (Nhãn thay thế tồi)** nằm ở 2 điểm cốt lõi sau:

### 1. Bỏ sót lượng khách hàng khổng lồ (False Negative)

Nếu mô hình chỉ học dựa trên nhãn *"vừa mới mua xe"*, nó sẽ nghĩ rằng chỉ có những người này mới là chủ xe đạp. Kết quả là nó sẽ **bỏ qua hoàn toàn** những người đã mua xe đạp từ 1 năm, 2 năm trước.

* Những người đi xe đạp lâu năm đó thực chất lại là những người **có nhu cầu thay mũ bảo hiểm mới cao nhất** vì mũ cũ của họ đã bị mòn hoặc hỏng. Dùng nhãn này sẽ làm công ty mất đi một lượng lớn khách hàng tiềm năng.

### 2. Gửi sai thời điểm (False Positive)

Thông thường, khi một người quyết định xuống tiền mua một chiếc xe đạp mới tại cửa hàng, họ sẽ có xu hướng **mua luôn mũ bảo hiểm và phụ kiện đi kèm ngay lúc đó**.

* Nếu họ vừa mua xe xong và đã có mũ rồi, việc công ty gửi thêm một cái coupon giảm giá 15% mua mũ bảo hiểm sau đó vài ngày sẽ trở nên vô nghĩa với họ.

---

> **Tóm lại:** Một nhãn proxy tốt phải phản ánh được chính xác hành vi của mục tiêu. Trong trường hợp này, việc *"vừa mới mua xe"* không đại diện tốt cho tệp *"những người sở hữu xe đạp cần mua mũ"*, vì vậy nó là một **Proxy tồi**.
> Để giải quyết bài toán này, các nhãn proxy khác như: *Người hay mua phụ kiện xe đạp, người tham gia các câu lạc bộ đạp xe, hoặc người hay tìm kiếm đường đi cho xe đạp trên bản đồ...* sẽ có tính liên kết chặt chẽ và thực tế hơn nhiều.
