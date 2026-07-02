
## Thử Thách Thực Chiến Số 13: Trí tuệ nhân tạo mảng Tài chính (FinTech)

### Tình huống:

Bạn vừa được tuyển vào làm AI Engineer cho một công ty tài chính (Cho vay tiêu dùng). Mỗi ngày công ty nhận hàng ngàn hồ sơ xin vay vốn. Sếp yêu cầu bạn viết một con AI tự động **Duyệt hồ sơ (1)** hoặc **Từ chối (0)** dựa trên 2 thông tin cơ bản của khách hàng:

1. `Thu_Nhap` (Lương hằng tháng - tính bằng Triệu VNĐ)
2. `Diem_Tin_Dung` (Điểm uy tín tài chính, từ 0 đến 1000. Càng cao càng uy tín)

Sếp đưa cho bạn một tập dữ liệu lịch sử của 12 khách hàng cũ để AI học.

### Dữ liệu gốc (Bạn hãy copy đoạn này vào code):

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# --- DỮ LIỆU GỐC ---
# [Thu nhập (Triệu VNĐ), Điểm tín dụng]
X_khach_hang = [
    [15, 600], [8, 400], [30, 750], [22, 680], 
    [10, 500], [5, 350], [50, 800], [40, 720], 
    [12, 550], [18, 620], [25, 710], [9, 450]
]

# Nhãn tương ứng: 1 = Duyệt cho vay, 0 = Từ chối (Vì nợ xấu)
Y_quyet_dinh = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]

```

### Nhiệm vụ của bạn:

Hãy vận dụng kiến thức để viết tiếp đoạn code thực hiện các bước sau:

1. **Chia để trị:** Dùng `train_test_split` để chia `X_khach_hang` và `Y_quyet_dinh` với tỷ lệ test là **0.25** (tức là 25% mang đi thi) và `random_state=42`.
2. **Huấn luyện:** Khởi tạo `DecisionTreeClassifier()` và dạy nó bằng tập Train.
3. **Dự đoán:** Ép mô hình vừa học xong đưa ra dự đoán trên tập Test.
4. **Báo cáo Sếp:**
* In ra màn hình Độ chính xác (`accuracy_score`) tính bằng phần trăm.
* In ra màn hình Ma trận nhầm lẫn (`confusion_matrix`).


5. **Đọc vị Ma trận (Viết bằng dòng comment `#` trong code):** Dựa vào cái ma trận in ra, bạn hãy comment cho tôi biết:
* Con AI này có cấp vốn nhầm cho kẻ nợ xấu nào không (Bỏ lọt / False Positive)?
* Con AI này có từ chối oan người tốt nào không (Báo động giả / False Negative)?



Hãy mở trình soạn thảo lên, gõ code, phân tích ma trận và dán toàn bộ thành quả của bạn xuống đây.