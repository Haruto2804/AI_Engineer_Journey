## Bài 32: Dữ liệu mất cân bằng
[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets)

## 1. Dữ liệu cân bằng vs. Mất cân bằng

* **Dữ liệu cân bằng (Class-balanced datasets):** Số lượng mẫu giữa các nhóm (classes) gần bằng nhau. Ví dụ: Tập dữ liệu có 235 ca dương tính và 247 ca âm tính.
* **Dữ liệu mất cân bằng (Class-imbalanced datasets):** Một nhóm áp đảo hoàn toàn nhóm còn lại. Thực tế, dạng này phổ biến hơn rất nhiều. Ví dụ: Trong giao dịch thẻ tín dụng, giao dịch lừa đảo thường chiếm chưa tới 0.1%.
* **Nhóm đa số (Majority class):** Nhóm chiếm số lượng lớn (ví dụ: giao dịch bình thường).
* **Nhóm thiểu số (Minority class):** Nhóm chiếm số lượng rất nhỏ (ví dụ: giao dịch lừa đảo).



## 2. Tại sao huấn luyện dữ liệu mất cân bằng lại khó?

Khi huấn luyện (train), mô hình học qua từng đợt dữ liệu nhỏ gọi là **batch**. Để phân biệt tốt, mỗi batch cần có đủ đại diện của cả hai nhóm.

Nếu dữ liệu quá mất cân bằng, các batch thường sẽ **không chứa bất kỳ mẫu nào của nhóm thiểu số**. Ví dụ, nếu bạn có 200 bông hướng dương và chỉ có 2 bông hồng, một batch size (kích thước đợt) là 20 mẫu nhiều khả năng sẽ toàn hướng dương. Mô hình sẽ không có cơ hội nhìn thấy bông hồng để học cách nhận diện nó.

> **Lưu ý quan trọng:** Với dữ liệu mất cân bằng, **Độ chính xác (Accuracy)** là một thước đo tồi. Nếu 99.9% giao dịch là bình thường, mô hình chỉ cần nhắm mắt đoán "bình thường" cho mọi trường hợp thì độ chính xác vẫn đạt 99.9%, nhưng mô hình đó hoàn toàn vô dụng vì bỏ lọt 100% ca lừa đảo.

## 3. Cách khắc phục: Kỹ thuật 2 bước

Để giúp mô hình vừa học được đặc điểm của từng nhóm, vừa hiểu được tỷ lệ phân bố thực tế, chúng ta dùng kỹ thuật kết hợp:

### Bước 1: Downsample (Giảm mẫu) nhóm đa số

Thay vì dùng toàn bộ dữ liệu của nhóm đa số, bạn chủ động **bỏ bớt** chúng.

* *Ví dụ:* Thay vì tỷ lệ 99% - 1%, bạn giảm nhóm đa số xuống 25 lần để tạo ra một tỷ lệ "giả" cân bằng hơn là 80% - 20%.
* *Tác dụng:* Đảm bảo mỗi batch giờ đây đều có cơ hội chứa các mẫu của nhóm thiểu số để mô hình học tập.

### Bước 2: Upweight (Tăng trọng số) nhóm vừa bị giảm

Việc giảm mẫu ở Bước 1 tạo ra một "thế giới giả" khiến mô hình bị sai lệch (prediction bias). Để đưa mô hình về thực tế, bạn cần **phạt nặng hơn** khi nó đoán sai ở nhóm đa số.

* *Cách làm:* Nếu bạn đã giảm mẫu nhóm đa số đi 25 lần (ở Bước 1), bạn phải nhân độ lỗi (loss) của nhóm này lên 25 lần. Tức là 1 lần đoán sai lúc này sẽ bị tính bằng 25 lần đoán sai bình thường.

## 4. Lợi ích của phương pháp này

* **Mô hình thông minh hơn:** Nó vừa hiểu mối liên hệ giữa các đặc trưng (features) và nhãn (labels), vừa không quên tỷ lệ phân bố thực tế của dữ liệu.
* **Hội tụ nhanh hơn (Faster convergence):** Do nhóm thiểu số xuất hiện thường xuyên hơn trong lúc train, mô hình sẽ học nhanh và hiệu quả hơn.