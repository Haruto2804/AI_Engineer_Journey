

## Bài 12: Chia để trị (Train/Test Split) – Bài kiểm tra năng lực thực sự

### 1. Ý nghĩa: Tại sao phải "chia" dữ liệu?

Như chúng ta vừa phân tích ở bài trước, nếu bạn lấy toàn bộ dữ liệu ra để dạy AI, rồi lại lấy chính đống đó ra để thi, AI sẽ **Học vẹt (Overfitting)**. Nó chỉ nhớ thuộc lòng đáp án của những dữ liệu cũ mà không hề có khả năng khái quát hóa quy luật cho những khách hàng mới trong tương lai.

Quy trình chuẩn mực để huấn luyện AI mà mọi tập đoàn lớn đều làm là:

1. Giao toàn bộ dữ liệu bạn có cho hàm `train_test_split`.
2. Hàm này sẽ xáo trộn ngẫu nhiên và chặt dữ liệu ra làm 2 phần:
* **Tập Train (Khoảng 70% - 80%):** Đưa cho mô hình học (`model.fit()`).
* **Tập Test (Khoảng 20% - 30%):** Cất vào két sắt, tuyệt đối không cho mô hình nhìn thấy lúc học. Học xong mới lôi ra bắt nó làm bài kiểm tra (`model.predict()` và `accuracy_score`).



### 2. Thực hành: Nhát chém ngẫu nhiên bằng `train_test_split`

Scikit-Learn thiết kế hàm này cực kỳ thông minh. Bạn truyền vào danh sách Đặc trưng (`X`) và Nhãn (`Y`), nó sẽ trả về cho bạn **4 biến** tương ứng cùng một lúc.

Hãy xem cách viết chuẩn xác:

```python
from sklearn.model_selection import train_test_split

# Giả sử ta có dữ liệu của 100 khách hàng (X: đặc trưng, y: nhãn)
# Cú pháp chia dữ liệu:
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2,     # Cắt 20% dữ liệu ra để làm bài Test (80% để Train)
    random_state=42    # Ghi nhớ cách xáo trộn (để lần sau chạy lại code không bị đổi kết quả)
)

print(f"Số lượng dữ liệu mang đi dạy: {len(X_train)}")  # Output: 80
print(f"Số lượng dữ liệu mang đi thi: {len(X_test)}")   # Output: 20

```

*(Mẹo nhỏ cho kỹ sư: Con số `random_state=42` là một "meme" kinh điển trong giới lập trình, lấy từ cuốn tiểu thuyết "The Hitchhiker's Guide to the Galaxy". Nó có nghĩa là lời giải đáp cho mọi thứ trong vũ trụ. Bạn dùng số 0, 1 hay 99 đều được, nhưng 99% tài liệu AI trên mạng đều dùng số 42 để làm hạt giống ngẫu nhiên).*

---

### 3. Thử thách thực chiến số 12: Đập đi xây lại quy trình AI

Lần này, chúng ta sẽ làm một quy trình chuẩn từ A đến Z, không bỏ sót bước nào.

Giả sử bạn có dữ liệu của **10 khách hàng** (gồm số giờ online và số tin nhắn) cùng với đáp án thực tế xem họ có mua Premium hay không.

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# --- BƯỚC 1: DỮ LIỆU GỐC ---
X_tong = [
    [1, 10], [2, 15], [20, 100], [25, 120], [5, 20], 
    [18, 90], [3, 10], [22, 110], [6, 30], [30, 150]
]
Y_tong = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1] 
# (Nhìn bằng mắt ta thấy quy luật: Cứ số to là 1, số nhỏ là 0)

```

**Yêu cầu Thử thách:**
Bạn hãy viết tiếp đoạn code để hoàn thiện quy trình huấn luyện này:

1. Dùng `train_test_split` để chia `X_tong` và `Y_tong` thành 4 biến (`X_train`, `X_test`, `y_train`, `y_test`) với tỷ lệ test là **0.3** (30%), và `random_state=42`.
2. Khởi tạo `DecisionTreeClassifier()` và dạy nó (fit) bằng **tập Train** (`X_train` và `y_train`).
3. Lấy mô hình vừa dạy xong, dự đoán (predict) trên **tập Test** (`X_test`). Đặt tên kết quả là `y_pred`.
4. Cuối cùng, dùng `accuracy_score` chấm điểm giữa `y_test` (sự thật) và `y_pred` (AI đoán), sau đó in kết quả ra màn hình.

Đây là bài kiểm tra tổng hợp cực kỳ quan trọng. Bạn hãy code và gửi lên đây, chúng ta sẽ xem con AI này thi được bao nhiêu điểm khi không được học vẹt nữa nhé!