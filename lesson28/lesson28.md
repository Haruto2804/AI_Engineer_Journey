#### [Xem thêm](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses)
## Bài 28: Một số vấn đề thường thấy khi làm việc với dữ liệu phân loại


### 1. Nhãn do con người gắn (Human Raters) – "Gold Labels"

Khi dữ liệu được phân loại thủ công bởi con người, trong ngành ML người ta gọi đó là **Gold Labels** (Nhãn vàng). Đây được coi là "chuẩn mực" vì con người có tư duy và hiểu ngữ cảnh tốt hơn máy.

* **Vấn đề lớn nhất – Bias & Sai sót:** Con người không phải lúc nào cũng đúng. Người gắn nhãn có thể mệt mỏi dẫn đến làm sai, hoặc mang định kiến cá nhân (bias), thậm chí là ác ý làm sai lệch dữ liệu.
* **Độ đồng thuận giữa các chuyên gia (Inter-rater agreement):** Nếu đưa cùng một tấm ảnh hay một câu nói cho hai người khác nhau, họ có thể gắn nhãn khác nhau.
* *Giải pháp:* Để kiểm tra xem dữ liệu có đáng tin không, người ta cho **nhiều người cùng gắn nhãn trên một mẫu** rồi dùng các số đo thống kê để xem họ đồng tình với nhau bao nhiêu phần trăm.



### 2. Nhãn do máy gắn (Machine Raters) – "Silver Labels"

Khi bạn dùng một mô hình ML này để đi gắn nhãn dữ liệu cho một mô hình ML khác học, nhãn đó gọi là **Silver Labels** (Nhãn bạc). Chất lượng của loại này thì "hên xui" và biến động rất lớn.

* **Vấn đề – Sai sót ngớ ngẩn (Thiếu logic thực tế):** Máy móc không có "Common sense" (lý trí thông thường).
* *Ví dụ nổi tiếng:* Một mô hình thị giác máy tính có thể nhầm lẫn tai hại giữa một chú chó Chihuahua và một chiếc bánh Muffin vì bề ngoài chúng có vài nét tương đồng. Nếu bạn lấy dữ liệu sai này đem đi dạy mô hình mới, mô hình mới sẽ bị "ngáo" theo.
* *Lỗi lệch hệ thống (Systemic Bias):* Một bộ phân tích cảm xúc đáng lẽ từ trung tính phải là `0.0`, nhưng nó lại chấm thành `-0.25`. Kết quả là toàn bộ tập dữ liệu bị kéo về hướng tiêu cực một cách vô lý.



### 3. Vấn đề bùng nổ chiều dữ liệu (High Dimensionality)

Đây là rắc rối kỹ thuật lớn nhất khi làm việc với dữ liệu phân loại.

* **Tại sao lại bị nhiều chiều?** Máy tính không hiểu chữ. Nếu bạn có danh sách 10.000 từ vựng, cách cơ bản nhất là biến mỗi từ thành một cột (Vector 10.000 chiều).
* **Hệ quả:** Dữ liệu càng nhiều chiều thì **chi phí huấn luyện càng đắt đỏ**, tốn RAM, tốn GPU và mô hình cực kỳ khó hội tụ (khó học tốt).
* **Giải pháp:** Với dữ liệu văn bản/ngôn ngữ tự nhiên, người ta sẽ dùng kỹ thuật **Embeddings** (Nhúng) để nén hàng vạn chiều đó xuống thành một vector ngắn hơn (ví dụ còn vài trăm chiều) nhưng vẫn giữ trọn vẹn ý nghĩa. (Đây là bài học nâng cao ở các chương sau).

---

**Tóm lại:** Dữ liệu phân loại rất "đỏng đảnh". Trước khi ném vào mô hình huấn luyện, bạn bắt buộc phải kiểm tra xem nhãn đó có bị sai lệch không (dù là người hay máy gắn) và phải tìm cách giảm chiều dữ liệu để tránh làm sập hệ thống.

