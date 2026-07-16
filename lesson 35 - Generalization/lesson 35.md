[Watch this video](https://youtu.be/TyT8i8YIcwI?si=PHRD4SmZAjjd9boy)


## Bài 35 - Generalization
Dưới đây là nội dung cốt lõi của bài học:
### 1. Câu chuyện về người ngoài hành tinh học ngoại ngữ

* Tưởng tượng bạn là một người ngoài hành tinh muốn học ngôn ngữ để giao tiếp [[00:05](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=5)].
* **Lần 1:** Bạn quyết định hòa nhập vào một cộng đồng nhỏ ở địa phương và học cách nói chuyện của riêng họ [[00:20](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=20)]. Dù bạn giao tiếp rất tốt với nhóm người này, nhưng khi bước ra thế giới thực, bạn hoàn toàn thất bại vì ngôn ngữ của bạn không áp dụng được với người khác [[00:41](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=41)].
* **Lần 2:** Nhận ra sai lầm, bạn thay đổi chiến thuật bằng cách lắng nghe nhiều người nói chuyện hơn từ các hoàn cảnh đa dạng hơn [[01:32](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=92)]. Nhờ vậy, kỹ năng giao tiếp của bạn mới có thể áp dụng thành công vào môi trường thực tế [[01:41](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=101)].

### 2. Liên hệ với Machine Learning: Overfitting và Generalization

Câu chuyện trên mô tả chính xác những gì xảy ra khi huấn luyện AI:

* **Học vẹt (Overfitting):** Khi bạn dạy mô hình AI bằng một tập dữ liệu (Training data), bạn đang dạy nó làm tốt trên tập dữ liệu cụ thể đó [[00:56](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=56)]. Tuy nhiên, nếu nó đoán cực kỳ chính xác trên tập dữ liệu cũ nhưng lại đoán rất tệ trên dữ liệu hoàn toàn mới, thì mô hình đã bị "Overfit" (Học vẹt/Quá khớp) [[01:10](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=70)]. Nó bị tinh chỉnh quá mức để bám chặt vào các chi tiết vụn vặt của dữ liệu cũ đến mức không thể nhận diện được các quy luật khi gặp dữ liệu mới [[01:18](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=78)].
* **Khái quát hóa (Generalization):** Mô hình AI không khái quát hóa được chính là mô hình giống như người ngoài hành tinh ở lần học đầu tiên [[01:10](https://www.youtube.com/watch?v=TyT8i8YIcwI&t=70)]. Mục tiêu tối thượng của mọi hệ thống Machine Learning là phải có tính **Generalization**, nghĩa là khả năng phân tích và đưa ra dự đoán chính xác trên những dữ liệu mới toanh mà nó chưa từng "nhìn thấy" bao giờ.

**Tóm lại:** Bài học này nhấn mạnh rằng điểm số (Accuracy) cao trên tập dữ liệu học (Training set) không có nhiều ý nghĩa. Sự thành công của AI phụ thuộc vào việc nó có khả năng "Khái quát hóa" quy luật để đối phó với thế giới thực đầy biến động hay không.