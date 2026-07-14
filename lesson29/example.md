Để bạn thực sự làm chủ khái niệm **Feature Cross** này, hãy cùng làm một ví dụ thực hành cực kỳ thực tế dưới đây.

---

## 🎯 Bài toán thực tế: Dự đoán xem khách có mua "Kem chống nắng" hay không?

Chúng ta có 2 cột đặc trưng ban đầu được chuyển về dạng số (One-hot encoding) như sau:

* **Thời tiết ($x_1$):** Gồm 2 giá trị: `[Nắng, Mưa]`
* **Mùa ($x_2$):** Gồm 2 giá trị: `[Mùa hè, Mùa đông]`

---

### ✍️ Đọc dữ liệu mẫu của 3 khách hàng:

1. **Khách hàng A:** Đi mua đồ vào một ngày **Nắng** của **Mùa hè**.
2. **Khách hàng B:** Đi mua đồ vào một ngày **Nắng** của **Mùa đông**.
3. **Khách hàng C:** Đi mua đồ vào một ngày **Mưa** của **Mùa hè**.

---

### 🧠 Thử thách dành cho bạn:

Nếu chúng ta thực hiện **Feature Cross** giữa hai đặc trưng **Thời tiết** và **Mùa**, chúng ta sẽ có tổng cộng **4 đặc trưng tổ hợp mới** ($2 \times 2 = 4$):

* `Nắng_Mùa-hè`
* `Nắng_Mùa-đông`
* `Mưa_Mùa-hè`
* `Mưa_Mùa-đông`

**Bạn hãy xác định xem giá trị (0 hay 1) của 4 đặc trưng tổ hợp này đối với Khách hàng A, B, và C sẽ như thế nào?**

Bạn có thể điền thử vào bảng sau:

| Khách hàng | Nắng_Mùa-hè | Nắng_Mùa-đông | Mưa_Mùa-hè | Mưa_Mùa-đông |
| --- | --- | --- | --- | --- |
| **A (Nắng + Mùa hè)** | ? | ? | ? | ? |
| **B (Nắng + Mùa đông)** | ? | ? | ? | ? |
| **C (Mưa + Mùa hè)** | ? | ? | ? | ? |

*(Gợi ý: Chỉ có duy nhất một ô có giá trị bằng `1` cho mỗi khách hàng, đại diện cho sự kết hợp đang diễn ra thực tế của họ!)*

Bạn hãy thử điền số `0` hoặc `1` vào các dấu `?` xem sao nhé!
---
### Lời giải:
Đáp án chính xác đây bạn nhé!

Mỗi khách hàng chỉ rơi vào đúng **một tổ hợp duy nhất** tại thời điểm đó, nên ô của tổ hợp đó sẽ bằng `1`, còn lại toàn bộ bằng `0`.

| Khách hàng | Nắng_Mùa-hè | Nắng_Mùa-đông | Mưa_Mùa-hè | Mưa_Mùa-đông |
| --- | --- | --- | --- | --- |
| **A (Nắng + Mùa hè)** | **1** | 0 | 0 | 0 |
| **B (Nắng + Mùa đông)** | 0 | **1** | 0 | 0 |
| **C (Mưa + Mùa hè)** | 0 | 0 | **1** | 0 |

---

> 💡 **Tại sao làm vậy mô hình lại thông minh hơn?**
> Nếu không dùng Feature Cross, mô hình tuyến tính chỉ thấy **Khách A** và **Khách B** đều có điểm chung là `Nắng` $\rightarrow$ nó sẽ đoán bừa là cả hai đều có khả năng mua kem chống nắng như nhau.
> Nhưng nhờ có cột Feature Cross, mô hình sẽ học được rằng: riêng cột `Nắng_Mùa-hè` của Khách A có trọng số (weight) cực kỳ cao, còn cột `Nắng_Mùa-đông` của Khách B thì trọng số bằng 0. Nhờ vậy mô hình dự đoán chuẩn xác hơn hẳn!
