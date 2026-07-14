Tụi mình cùng làm một bài tập thực tế mang tên **"Bản đồ Embedding phim ảnh"** nhé. Bài tập này sẽ giúp bạn hiểu chính xác cách các hệ thống như Netflix hay YouTube chuyển đổi sở thích của bạn thành các con số toán học để gợi ý video.

---

## 🎬 Đề bài: Xây dựng Không gian Embedding 2 chiều cho Phim

Giả sử bạn là kỹ sư AI tại một nền tảng xem phim trực tuyến. Bạn cần biểu diễn các bộ phim dưới dạng một chuỗi gồm **2 con số** (Vectơ 2 chiều): `[Trục X, Trục Y]`.

Chúng ta quy ước ý nghĩa của 2 trục tọa độ này như sau (giá trị chạy từ `-1.0` đến `1.0`):

* **Trục X (Hành động vs. Tâm lý):**
* Càng gần `-1.0`: Phim thuần tâm lý, tình cảm nhẹ nhàng, ít cháy nổ.
* Càng gần `1.0`: Phim hành động dồn dập, kỹ xảo hoành tráng, bắn nhau đùng đoàng.


* **Trục Y (Hài hước vs. Nghiêm túc):**
* Càng gần `-1.0`: Phim cực kỳ nghiêm túc, giật gân, u tối hoặc hàn lâm.
* Càng gần `1.0`: Phim hài hước, giải trí, lầy lội, xem để cười.



---

## 🛠️ Nhiệm vụ 1: Định vị tọa độ (Tự tạo Embedding)

Dựa vào quy ước trên, bạn hãy thử đoán hoặc tự gán tọa độ Embedding `[X, Y]` phù hợp cho 4 bộ phim dưới đây (không cần chính xác tuyệt đối, chỉ cần đúng logic hướng đi của số âm/dương):

1. **Phim A: Tom & Jerry** (Hoạt hình, cực kỳ hài hước, có hành động rượt đuổi vui nhộn nhưng không phải bắn nhau u tối)
2. **Phim B: John Wick** (Hành động bắn súng siêu dồn dập, cốt truyện nghiêm túc, ngầu lòi, u tối)
3. **Phim C: Titanic** (Phim tâm lý tình cảm kinh điển, lãng mạn, nghiêm túc và lấy đi nhiều nước mắt)
4. **Phim D: Mr. Bean / Phim hài tình cảm nhẹ nhàng** (Thuần hài hước, nhẹ nhàng, không có đấm đá cháy nổ)

> ✍️ **Bạn hãy lấy giấy bút hoặc gõ thẳng ra câu trả lời:** Dự đoán tọa độ `[X, Y]` cho từng phim A, B, C, D (Ví dụ: `Phim A = [0.5, 0.8]`).

---

## 🧠 Nhiệm vụ 2: Suy luận kiểu Machine Learning

Sau khi đã có tọa độ của 4 phim trên, hãy trả lời câu hỏi sau:

> Nếu một người dùng vừa xem xong phim **John Wick**, hệ thống Machine Learning của bạn nên tự động gợi ý bộ phim nào tiếp theo trong 3 phim còn lại (Tom & Jerry, Titanic, hay Mr. Bean)? **Tại sao dựa vào các con số tọa độ (Embedding)?**

---

Bạn cứ thử đưa ra các con số và câu trả lời theo suy nghĩ của mình nhé, sai cũng không sao hết. Mình sẽ cùng bạn phân tích xem kết quả của bạn khớp với cách thuật toán máy tính tính toán như thế nào!