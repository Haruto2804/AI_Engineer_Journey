
## Thử thách thực chiến số 17: AI "Giữ chân nhân tài" (Employee Retention)

### 1. Tình huống doanh nghiệp

Bạn là Kỹ sư AI tại một tập đoàn công nghệ lớn. Gần đây, công ty liên tục bị mất các nhân sự giỏi vào tay đối thủ. Mỗi lần một nhân viên cứng nghỉ việc, công ty phải tốn hàng trăm triệu đồng để tuyển dụng và đào tạo người mới thay thế.

Giám đốc Nhân sự (HR Director) đưa cho bạn dữ liệu của 12 nhân viên cũ. Dữ liệu gồm 3 thông tin: **[Mức lương (Triệu VNĐ), Số giờ OT (Làm thêm) mỗi tuần, Điểm hài lòng về Sếp (Từ 1 đến 10)]**.

Giám đốc yêu cầu bạn:

1. Xây dựng một con AI tốt nhất có thể để nhận diện xem ai sắp nộp đơn xin nghỉ việc.
2. Trích xuất bản báo cáo chiến lược để trả lời câu hỏi: *"Rốt cuộc nhân viên nghỉ việc chủ yếu là do Lương thấp, do Bắt làm thêm giờ quá nhiều, hay do Sếp tồi?"*

### 2. Dữ liệu gốc (Bạn copy vào IDE nhé)

```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- DỮ LIỆU GỐC ---
# Đặc trưng: [Lương (Triệu), Số giờ OT/tuần, Điểm hài lòng sếp (1-10)]
X_nhan_su = [
    [15, 20, 4], [30, 5, 8], [12, 25, 3], [40, 0, 9],
    [10, 15, 5], [25, 10, 7], [14, 22, 2], [35, 2, 8],
    [18, 18, 5], [20, 8, 6], [11, 28, 4], [50, 0, 10]
]
# Nhãn: 1 = Đã nộp đơn nghỉ việc, 0 = Vẫn đang cống hiến
Y_nghi_viec = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

ten_cac_cot = ["Mức lương", "Số giờ OT", "Điểm hài lòng Sếp"]

```

### 3. Yêu cầu nhiệm vụ (Combo tất cả kỹ năng):

1. **Chuẩn bị:** Dùng `train_test_split` chia dữ liệu (`test_size=0.3`, `random_state=42`).
2. **Triệu hồi Robot:** * Tạo `danh_sach_thong_so` để thử nghiệm `n_estimators`: `[10, 50, 100]` và `max_depth`: `[2, 3, None]`.
* Khởi tạo `GridSearchCV` với `RandomForestClassifier(random_state=42)` và `cv=2`. Cho nó học (`fit`) trên tập Train.


3. **Khai thác AI:**
* In ra màn hình cấu hình tốt nhất.
* Lấy bản báo cáo độ quan trọng: `diem_quan_trong = robot.best_estimator_.feature_importances_`
* In ra tỷ lệ phần trăm (%) sức nặng của cả 3 yếu tố: Mức lương, Số giờ OT, Điểm hài lòng Sếp.


4. **Phân tích Kinh doanh (Bắt buộc):** Dựa vào 3 con số phần trăm in ra, bạn hãy viết comment trả lời Giám đốc HR: Yếu tố nào là nguyên nhân cốt lõi khiến nhân viên bỏ công ty? Giám đốc nên ra quyết định gì (Tăng lương, Giảm giờ làm, hay Đuổi mấy ông Sếp tồi)?

Hãy mở trình soạn thảo, hoàn thành siêu bài tập này và gửi toàn bộ code cùng lời tư vấn của bạn cho Sếp HR lên đây nhé!