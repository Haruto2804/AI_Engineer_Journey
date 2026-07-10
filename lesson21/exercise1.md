
### PHẦN 3: THỬ THÁCH TÌNH HUỐNG (Dành cho bạn)

Để kiểm tra xem bạn đã thực sự làm chủ kỹ thuật Clipping này chưa, hãy giải quyết bài toán thực tế sau bằng code.

**Tình huống:** Bạn đang làm hệ thống AI chấm điểm tín dụng để cho vay tiền tại một ngân hàng. Số điểm tín dụng hợp pháp của một người chỉ được phép nằm trong khoảng từ **300 điểm** (Rất xấu) đến **850 điểm** (Rất tốt). Tuy nhiên, do lỗi hệ thống đồng bộ dữ liệu, tập dữ liệu trả về bị xuất hiện vài con số dị thường:

```python
import pandas as pd
data_nganhang = {'diem_tin_dung': [720, 850, 150, 610, 9999, 450]}
df_bank = pd.DataFrame(data_nganhang)

```

**Nhiệm vụ của bạn:**
Hãy viết tiếp đoạn code Pandas sử dụng hàm `.clip()` để ép các giá trị lỗi kia về đúng khung quy định (Sàn là 300, Trần là 850) và lưu vào một cột mới tên là `diem_sach`.

Bạn hãy gõ đoạn code hoàn chỉnh đó ra đây để tôi kiểm tra xem đã chính xác chưa nhé! Chờ phản hồi từ bạn.