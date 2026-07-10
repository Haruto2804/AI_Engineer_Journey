Tuyệt vời! Chúng ta tiến tới "vũ khí" thứ ba: **Tỷ lệ Logarit (Log Scaling)**.

Phương pháp này giống như một chiếc kính lúp ma thuật dành riêng cho những dữ liệu có độ chênh lệch cực kỳ khủng khiếp.

### 3. Tỷ lệ Logarit (Log Scaling)

Thay vì cộng, trừ hay chia tỷ lệ, phương pháp này sẽ tính logarit (thường là logarit tự nhiên - $\ln$) của giá trị thô ban đầu.

**Công thức toán học:**

$$x' = \ln(x)$$

---

#### Khi nào nên dùng?

Log Scaling sinh ra để trị những dữ liệu tuân theo **Phân phối hàm mũ (Power law distribution)** - hay còn gọi nôm na là dữ liệu "đuôi dài". Dấu hiệu nhận biết:

* Phần lớn các giá trị tụ tập ở mức rất thấp (tần suất cực cao).
* Có một số ít giá trị vươn tới mức khổng lồ, xa tít tắp (tần suất rất thấp).

**Ví dụ kinh điển: Lượt bán sách hoặc Lượt xem video**

* Hầu hết các cuốn sách xuất bản chỉ bán được lác đác khoảng **100 - 200** cuốn.
* Một số ít sách nổi tiếng bán được vài chục ngàn cuốn.
* Và chỉ có đếm trên đầu ngón tay những cuốn best-seller bán được **1,000,000** cuốn.

#### Tại sao Log Scaling lại kỳ diệu?

Nếu bạn đưa thẳng dữ liệu thô vào mô hình học máy, khoảng cách giữa 100 và 1,000,000 là **10,000 lần**. Mô hình sẽ bị "ngợp" trước con số 1 triệu và gần như phớt lờ hoàn toàn những cuốn sách bán được 100 cuốn.

Nhưng hãy xem phép màu của Logarit tự nhiên ($\ln$):

* Giá trị gốc $100 \rightarrow \ln(100) \approx 4.6$
* Giá trị gốc $1,000,000 \rightarrow \ln(1,000,000) \approx 13.8$

Sau khi đi qua hàm Log, giá trị 1 triệu giờ đây chỉ còn lớn gấp khoảng **3 lần** so với giá trị 100 (13.8 so với 4.6). Khoảng cách khổng lồ đã được thu hẹp lại thành một tỷ lệ hợp lý, giúp mô hình dễ dàng học hỏi hơn mà không bị sai số trầm trọng.

---

#### Trải nghiệm trực quan về Log Scaling

Để thấy rõ sức mạnh "nén" dữ liệu của hàm Log, bạn hãy xem biểu đồ dưới đây. Trục trên là dữ liệu gốc, nơi các con số nhỏ bị số 1 triệu chèn ép đến mức dính chặt vào nhau. Trục dưới là sau khi đã áp dụng Log Scaling, các khoảng cách đã được dàn trải hợp lý hơn rất nhiều:
