

Bài toán này không chỉ đòi hỏi code chuẩn, mà còn đòi hỏi bộ não của một Giám đốc Kinh doanh thực thụ. Chào mừng bạn đến với chiến trường của các siêu ứng dụng!

---

## 🚕 Thử thách Trùm Cuối: AI Định Giá Cuốc Xe Động (Dynamic Pricing)

### 1. Bối cảnh "Ngàn cân treo sợi tóc"

Bạn là Giám đốc AI (Head of AI) của **X-Ride**, một ứng dụng gọi xe công nghệ đang cạnh tranh khốc liệt với Grab và Be.

**Vấn đề:** Ứng dụng của bạn đang dùng công thức tính tiền cứng ngắc: **12.000 VNĐ / 1 Km**.
Vào một chiều thứ Sáu, trời đổ mưa tầm tã đúng giờ tan tầm. Đường kẹt cứng. Với mức giá 12k/km, tài xế thà tắt App đi uống cà phê còn hơn là nhích từng mét trên đường mà không bõ tiền xăng. Kết quả: Khách hàng gào thét vì không gọi được xe, bực tức xóa App X-Ride và tải App đối thủ. Công ty mất doanh thu trầm trọng!

**Nhiệm vụ của Sếp giao:**
*"Tôi cần em làm ngay một con AI **Định giá động (Dynamic Pricing)**. Nó phải tự động tăng giá cuốc xe lên khi trời mưa hoặc kẹt xe để dụ tài xế bật App làm việc, nhưng không được tăng quá lố khiến khách hàng sợ hãi bỏ đi. Làm xong, đóng gói file `.pkl` gửi cho đội Mobile App ngay trong đêm nay!"*

### 2. Dữ liệu Lịch sử giao dịch (Dataset)

Đội Data đã gom được dữ liệu của 8 cuốc xe "bắt đáy/đu đỉnh" thành công trong tuần trước (Khách đồng ý trả tiền và Tài xế đồng ý chạy).

**Đặc trưng:** `[Khoảng cách (Km), Giờ cao điểm (1=Có, 0=Không), Thời tiết (1=Mưa ngập, 0=Đẹp)]`
**Nhãn:** `Giá cước chốt đơn (Nghìn VNĐ)`

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# --- DỮ LIỆU GỐC ---
X_cuoc_xe = [
    [2, 0, 0],  # 2km, Giờ bình thường, Trời đẹp
    [2, 1, 1],  # 2km, Giờ cao điểm, Mưa ngập
    [5, 0, 0],  # 5km, Giờ bình thường, Trời đẹp
    [5, 1, 0],  # 5km, Giờ cao điểm, Trời đẹp
    [5, 1, 1],  # 5km, Giờ cao điểm, Mưa ngập
    [10, 0, 0], # 10km, Giờ bình thường, Trời đẹp
    [10, 1, 0], # 10km, Giờ cao điểm, Trời đẹp
    [10, 1, 1]  # 10km, Giờ cao điểm, Mưa ngập
]

Y_gia_tien = [25, 70, 60, 95, 150, 120, 180, 280]
ten_cot = ["Khoảng cách", "Giờ cao điểm", "Thời tiết mưa"]

```

### 3. Sứ mệnh của bạn (Combo Tối thượng):

Để giải cứu công ty, bạn cần viết một kịch bản code thực hiện ĐỦ 3 BƯỚC sau:

1. **Học & Bức cung AI:** Train con `RandomForestRegressor`. Lôi `feature_importances_` ra để trả lời cho Sếp: *"Thưa sếp, giữa việc Kẹt xe và Mưa ngập, cái nào là lý do chính khiến giá cước đội lên cao nhất?"*.
2. **Đóng gói xuất xưởng:** Lưu con AI này thành file `ai_dinh_gia_xride.pkl`.
3. **Thực chiến hệ thống:** Tưởng tượng bạn là cái App điện thoại. Load file `.pkl` lên và dự đoán ngay giá tiền cho một cuốc xe khách vừa book: **"Khách đi 7Km, đang là Giờ cao điểm, Trời mưa ngập"** `([7, 1, 1])`. In giá tiền ra màn hình để App hiển thị cho khách!

