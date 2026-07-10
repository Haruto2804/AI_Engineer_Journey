Tiếp theo, chúng ta sẽ đi sâu vào phương pháp thứ hai: **Tỷ lệ điểm Z (Z-score Scaling)**, hay còn gọi là **Standardization (Chuẩn hóa chuẩn)**.

Nếu như *Linear Scaling* cố gắng ép dữ liệu vào một cái khung cố định từ 0 đến 1, thì *Z-score Scaling* lại tiếp cận theo một cách thông minh hơn: Nó đo lường xem một điểm dữ liệu **nằm cách giá trị trung bình bao xa**, tính theo đơn vị là **độ lệch chuẩn**.

### 2. Tỷ lệ điểm Z (Z-score Scaling)

**Công thức toán học:**

$$z = \frac{x - \mu}{\sigma}$$

*Trong đó:*

* $x$: Giá trị thô ban đầu.
* $\mu$ (Mu): Giá trị trung bình (Mean) của toàn bộ tập dữ liệu.
* $\sigma$ (Sigma): Độ lệch chuẩn (Standard Deviation) – đại diện cho mức độ phân tán hoặc "co giãn" của dữ liệu.
* $z$: Giá trị mới sau khi chuẩn hóa (Điểm Z).

---

#### Ý nghĩa thực tế của Điểm Z (Z-score)

Khi một đặc trưng được chuyển đổi sang Z-score, tập dữ liệu mới sẽ luôn có **giá trị trung bình bằng 0** và **độ lệch chuẩn bằng 1**.

* Nếu $z = 0$: Điểm dữ liệu đó **bằng đúng** mức trung bình của cả tập hợp.
* Nếu $z = 1.5$: Điểm dữ liệu đó **cao hơn** mức trung bình 1.5 lần độ lệch chuẩn.
* Nếu $z = -2.0$: Điểm dữ liệu đó **thấp hơn** mức trung bình 2 lần độ lệch chuẩn.

#### Tại sao Z-score lại "trị" được Outlier tốt hơn Linear Scaling?

Hãy nhớ lại điểm yếu của Linear Scaling: gặp một ông siêu giàu (outlier) là toàn bộ người nghèo và trung lưu bị "bóp nghẹt" về sát số 0.

Z-score giải quyết được việc này vì nó không dùng giá trị lớn nhất ($x_{max}$) làm mốc vạch biên. Nó dùng độ lệch chuẩn. Khi có một giá trị ngoại lai cực lớn xuất hiện, giá trị trung bình $\mu$ và độ lệch chuẩn $\sigma$ có tăng lên đôi chút, nhưng khoảng cách của các điểm dữ liệu bình thường khác vẫn được giữ khoảng cách an toàn với nhau, không hề bị dồn cục lại một chỗ. Các điểm bình thường sẽ loanh quanh dải từ **-3 đến +3**, còn ông outlier sẽ nhảy vọt hẳn lên thành **+10** hoặc **+20**, tách biệt hoàn toàn.

---

#### Trải nghiệm trực quan về Z-score

Để hiểu rõ hơn cách Z-score "co giãn" dữ liệu và đối phó với các giá trị ngoại lai, bạn hãy thử tương tác với biểu đồ mô phỏng dưới đây. Bạn có thể thêm các điểm dữ liệu mới hoặc bấm nút thêm một "Giá trị ngoại lai cực đại" để thấy sự khác biệt so với Linear Scaling nhé:

Khi bạn đã nắm vững cách Z-score hoạt động và tại sao nó lại là lựa chọn hàng đầu cho các dữ liệu dạng hình chuông (Normal Distribution), hãy cho tôi biết để chúng ta tiếp tục sang phương pháp thứ ba: **Tỷ lệ Logarit (Log Scaling)** nhé!