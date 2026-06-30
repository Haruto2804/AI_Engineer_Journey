

###  Bước chuẩn bị: Cài đặt thư viện Scikit-Learn

Trước khi chạy code Python, bạn cần đảm bảo máy tính đã được cài đặt thư viện `scikit-learn`. Bạn mở Terminal (hoặc Command Prompt / Anaconda Prompt) và chạy câu lệnh sau:

```bash
pip install scikit-learn

```

*(Mẹo: Nếu bạn đang dùng Jupyter Notebook hoặc Google Colab, bạn có thể chạy trực tiếp câu lệnh đó trong một ô code bằng cách thêm dấu chấm than ở đầu: `!pip install scikit-learn`)*

---

Phần nền tảng về thao tác dữ liệu thô với NumPy và Pandas của bạn như vậy là đã quá vững vàng rồi! Những hàm lắt léo hơn thì sau này vào dự án thực tế, gặp ca khó ở đâu chúng ta sẽ mở tài liệu tra cứu đến đó. Cứ nhớ nguyên tắc: **Chỉ học những gì mình cần dùng để giải quyết bài toán hiện tại.**

Bây giờ, chúng ta chính thức bước qua giai đoạn "Chuẩn bị" để tiến vào thế giới AI thực thụ. Hành trang tiếp theo của bạn là thư viện nổi tiếng nhất thế giới về Machine Learning.

---

## Bài 10: Scikit-Learn – Bước chân đầu tiên vào "Học Máy" (Machine Learning)

### 1. Ý nghĩa: Scikit-Learn là gì?

Nếu Pandas là người thủ kho giúp bạn dọn dẹp và sắp xếp dữ liệu, thì **Scikit-Learn (sklearn)** chính là "bộ não" giúp bạn tìm ra quy luật từ đống dữ liệu đó và đưa ra dự đoán.

Thay vì phải tự viết các phương trình toán học phức tạp để mô phỏng mạng nơ-ron hay thuật toán thống kê, Scikit-Learn đã đóng gói sẵn hàng trăm thuật toán AI kinh điển (như Linear Regression, Decision Tree, Random Forest...). Việc của bạn chỉ là: Gói dữ liệu lại -> Đưa cho model học -> Bắt nó dự đoán.

### 2. Thực hành: Dạy AI phân loại khách hàng

Hãy tiếp tục bài toán ở Bài 9: Bạn đang có dữ liệu của người dùng. Lần này, bạn muốn AI **tự động dự đoán** xem một người dùng mới có khả năng mua gói Premium hay không, dựa trên 2 thông tin: *Số giờ online mỗi tuần* và *Số lượng tin nhắn họ đã gửi*.

Hãy xem quy trình 3 bước chuẩn của Machine Learning: Khởi tạo - Huấn luyện (Train) - Dự đoán (Predict).

```python
from sklearn.tree import DecisionTreeClassifier

# 1. CHUẨN BỊ DỮ LIỆU
# Mỗi danh sách con là [Số giờ online, Số tin nhắn] của 4 người dùng cũ
X_train = [
    [2, 10],   # Người 1: Ít online, ít nhắn tin
    [20, 150], # Người 2: Online nhiều, nhắn tin nhiều
    [5, 20],   # Người 3: Ít online, ít nhắn
    [18, 120]  # Người 4: Online nhiều, nhắn nhiều
]

# Nhãn tương ứng: 0 là Free, 1 là Premium
y_train = [0, 1, 0, 1] 

# 2. KHỞI TẠO VÀ DẠY (TRAIN) MODEL
model = DecisionTreeClassifier() # Gọi thuật toán Cây Quyết Định
model.fit(X_train, y_train)      # Hàm fit() chính là lúc AI học quy luật

# 3. AI DỰ ĐOÁN NGƯỜI DÙNG MỚI
# Có một người dùng mới: Online 19 giờ, gửi 130 tin nhắn
new_user = [[19, 130]]
prediction = model.predict(new_user)

print(f"AI dự đoán khách hàng này thuộc nhóm (0: Free, 1: Premium): {prediction}")
# Output: AI dự đoán khách hàng này thuộc nhóm: [1]

```

Thấy không? Chỉ với hàm `.fit()` và `.predict()`, bạn đã chính thức làm ra một mô hình Machine Learning rồi đấy!

---

### 3. Thử thách thực chiến số 10

Sếp của bạn vừa ném cho bạn thông tin của **2 khách hàng mới** và yêu cầu dùng ngay con AI vừa train ở trên để dự đoán xem họ có mua gói Premium không.

* Khách hàng A: Online 3 giờ/tuần, gửi 15 tin nhắn.
* Khách hàng B: Online 25 giờ/tuần, gửi 200 tin nhắn.

Dữ liệu đầu vào cho 2 khách hàng này sẽ được viết dưới dạng mảng 2 chiều như sau:
`new_customers = [[3, 15], [25, 200]]`

Bạn hãy viết đoạn code gọi hàm dự đoán của `model` cho `new_customers` và in kết quả ra màn hình nhé?