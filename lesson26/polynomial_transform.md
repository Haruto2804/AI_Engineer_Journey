# NUMBERIC DATA - Bài 26 - Polynomial Transform (Biến đổi đa thức)

## 1. Vấn đề: Đời không phải lúc nào cũng là đường thẳng

Khi mọi thứ là đường thẳng, đứa trẻ tính rất giỏi:

* **Ví dụ:** 1 bát phở giá 50k, 2 bát giá 100k, 3 bát 150k. Đứa trẻ chỉ cần lấy số lượng nhân với 50 là ra kết quả (Hồi quy tuyến tính).

Nhưng cuộc sống lại đầy rẫy những **đường cong**:

* **Ví dụ Bánh Pizza:** Bạn đi mua bánh Pizza. Cửa hàng bán size 15cm giá 100k. Bạn gọi size 30cm (đường kính gấp đôi). Đứa trẻ "nghĩ thẳng" sẽ tính: *"Đường kính gấp đôi thì giá gấp đôi, vậy là 200k!"*.
* **Sự thật:** Gấp đôi đường kính thì diện tích bánh tăng lên gấp 4 lần (do công thức diện tích có $r^2$). Giá đúng của chiếc Pizza khổng lồ đó phải là 400k! Đứa trẻ đã đoán sai hoàn toàn vì nó không biết vẽ đường cong.

## 2. Cách giải quyết: "Lừa" đứa trẻ bằng Biến đổi đa thức (Polynomial Transform)

Bạn không thể mổ não đứa trẻ ra và ép nó học những phương trình cong queo phức tạp được (bản chất thuật toán không cho phép). Vậy bạn làm gì? **Bạn dùng mẹo.**

Thay vì đưa cho đứa trẻ con số đường kính ban đầu (30cm), bạn tự nhẩm trong đầu $30 \times 30 = 900$.
Sau đó, bạn đưa con số $900$ này cho đứa trẻ và bảo: *"Đừng quan tâm đường kính nữa, chú có một thông tin mới tinh tên là X, giá trị của nó là 900, cháu tính tiền theo số này đi"*.

Thế là đứa trẻ lại vui vẻ áp dụng phép tính nhân thẳng băng của nó, và bùm – nó tính ra chính xác giá 400k!

**Hành động bạn vừa làm chính là Biến đổi đa thức:**

1. Bạn lấy dữ liệu gốc.
2. Bạn mang đi bình phương ($x^2$) hoặc lập phương ($x^3$) để tạo ra một **Đặc trưng nhân tạo (Synthetic Feature)** mới.
3. Nhờ cái bóng của con số mới này, mô hình (dù rất cứng nhắc) vẫn có thể uốn lượn và khớp hoàn hảo với các quy luật đường cong trong thực tế.

## 3. Ứng dụng thực tế: Từ sân cỏ đến vật lý

Biến đổi đa thức được dùng cực kỳ nhiều khi dữ liệu thực tế bị chi phối bởi các định luật tự nhiên:

* **Quỹ đạo trái bóng:** Hãy tưởng tượng một cú cứa lòng (finesse shot) hay cú nã đại bác sút xa trên sân cỏ. Nếu bóng bay theo đường thẳng (hàm bậc 1), nó sẽ bay thẳng tắp lên khán đài. Thực tế, bóng bị hút bởi trọng lực nên tạo thành quỹ đạo parabol. Để máy tính dự đoán được lúc nào bóng rơi xuống trúng góc chữ A, bạn không thể chỉ cung cấp cho nó biến thời gian $t$. Bạn **bắt buộc** phải tự tạo thêm một biến là thời gian bình phương $t^2$. Có $t^2$, máy tính mới bẻ cong được quỹ đạo bay.
* **Âm thanh & Ánh sáng:** Bạn càng đứng xa loa, âm thanh nghe càng nhỏ, nhưng nó nhỏ đi theo cấp số nhân (đường cong), chứ không phải chia đều đặn từng mét.

## 4. Chú ý cái "bẫy" khổng lồ

Có một lưu ý sống còn ở cuối tài liệu: Khi bạn mang các con số đi bình phương, chúng sẽ phình to lên một cách khủng khiếp.

* $10 \rightarrow 100$
* $1000 \rightarrow 1.000.000$

Nếu bạn ném những con số hàng triệu này vào mô hình, nó sẽ bị "ngợp" và tính toán loạn xạ. Vì vậy, sau khi biến đổi đa thức, bạn luôn phải làm một bước dọn dẹp là **Chuẩn hóa (Normalize)** – ép những con số khổng lồ đó về lại một giới hạn nhỏ gọn (như từ 0 đến 1) trước khi dạy cho mô hình.

---
# 1 Ví dụ khác
Thật sự khái niệm này rất "ảo", chúng ta hãy gác lại mọi lý thuyết toán học rườm rà và nhìn nó qua lăng kính của một lập trình viên nhé!

Hãy tưởng tượng bạn đang code một trò chơi trên web bằng JavaScript Canvas, trong đó có một con cua di chuyển.

### 1. Tại sao đường thẳng lại thất bại?

Giả sử bạn viết hàm cập nhật tọa độ cho con cua: `y = w * x` (với `x` là tọa độ ngang, `w` là một hằng số vận tốc). Khi hàm này chạy, con cua sẽ chỉ biết trượt đi theo một **đường chéo thẳng tắp** trên màn hình.

Mô hình Machine Learning Tuyến tính (Linear Model) cũng y hệt như vậy. Bộ não của nó bị "hardcode" đúng một công thức cơ bản: Tính tổng của (Đầu vào nhân với Trọng số). Nó chỉ có thể kẻ đường thẳng.

Nhưng bây giờ, bạn muốn mô phỏng con cua "nhảy" qua một tảng đá. Quỹ đạo nhảy phải là một đường vòng cung. Trong code, bạn bắt buộc phải đưa thêm phép bình phương vào: $y = w_1 \cdot x + w_2 \cdot x^2$. Phải có $x^2$ thì tọa độ nó mới bẻ cong được.

**Vấn đề lớn nhất là:** Mô hình Machine Learning tuyến tính rất "ngốc". Nó không có sẵn thuật toán để tự lấy `x` nhân với `x`. Nó chỉ biết há miệng chờ bạn đẩy dữ liệu vào và kẻ đường thẳng. Nếu bạn chỉ đưa cho nó biến `x`, nó vĩnh viễn sẽ đâm đầu vào tảng đá.

### 2. Trò ảo thuật (Bẻ cong dữ liệu chứ không bẻ cong mô hình)

Để giải quyết, chúng ta sẽ "hack" dữ liệu đầu vào.

* Thay vì chỉ gửi lên API một giá trị tọa độ `x = 2`, bạn viết code tự tính sẵn luôn một biến mới: `x_binh_phuong = 2 * 2 = 4`.
* Sau đó, bạn gửi **cả 2 biến** này vào mô hình: `[Feature1 = 2, Feature2 = 4]`.

Lúc này, điều kỳ diệu về mặt logic sẽ xảy ra:

1. **Góc nhìn của Mô hình:** Nó nhìn thấy 2 biến này và hoàn toàn không biết `Feature2` là do `Feature1` bình phương lên. Nó cứ ngây ngô coi đây là 2 luồng thông tin độc lập (giống như "Chiều cao" và "Cân nặng"). Nó vẫn áp dụng công thức cộng thẳng thắn của nó trong một không gian 3 chiều (3D). Đối với nó, nó đang dùng một tấm ván phẳng (mặt phẳng thẳng) để chia cắt dữ liệu.
2. **Góc nhìn của chúng ta:** Khi chiếu kết quả đó ngược lại lên màn hình Canvas 2D của chúng ta, vì cái `Feature2` thực chất là $x^2$, nên cái "mặt phẳng thẳng" của mô hình khi áp vào thế giới 2D đã tự động biến thành một **đường cong parabol**.

### 3. Ví dụ bằng Mảng (Array) để thấy rõ sự phân loại

Hãy nhìn cách dữ liệu bị "nhấc bổng" lên để dễ phân chia qua các mảng sau:

Giả sử bạn có mảng tọa độ X của các con vật: `[-2, -1, 0, 1, 2]`
Phân loại tương ứng: `[Cua đỏ, Mực xanh, Mực xanh, Mực xanh, Cua đỏ]`

Bạn muốn viết một lệnh `if...else` đơn giản (đại diện cho nhát cắt thẳng) để gom hết Cua đỏ về một bên, Mực xanh về một bên.
Nếu chỉ dùng mảng X, bạn không thể viết lệnh `if (X > ???)` nào để gom được 2 con Cua đỏ lại với nhau (vì nó nằm ở 2 đầu mút -2 và 2, bị kẹt bầy Mực xanh ở giữa). Mô hình thất bại.

**Bây giờ, áp dụng biến đổi đa thức (bình phương mảng X lên):**
Bạn có mảng mới: X_BinhPhuong = `[4, 1, 0, 1, 4]`

Hãy nhìn vào mảng mới này!

* Cua đỏ bây giờ có giá trị là **4**.
* Mực xanh bây giờ có giá trị là **0** và **1**.

Đột nhiên, bài toán trở nên quá dễ. Mô hình chỉ cần tạo ra một nhát cắt thẳng tắp: `if (X_BinhPhuong > 2) return Cua đỏ; else return Mực xanh;`.

**Bản chất của vấn đề:** Chúng ta không dạy máy cách bẻ cong con dao. Chúng ta tự tạo ra một hệ tọa độ mới ($x^2$), nhằm khuếch đại khoảng cách và "nhấc bổng" các dữ liệu ở rìa lên cao. Từ đó, lộ ra khoảng trống ở giữa để một con dao thẳng băng có thể dễ dàng cắt ngang qua!

---

Góc nhìn bằng cách biến đổi các phần tử trong Array như thế này đã giúp bạn hình dung rõ ràng hơn về từ "bẻ cong" chưa?