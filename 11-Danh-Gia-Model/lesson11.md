

## Bài 11: Đánh giá mô hình (Model Evaluation) – AI của bạn khôn hay "ngu"?

### 1. Ý nghĩa: Tại sao phải đánh giá?

Ở bài trên, model dự đoán cho "Bùi Xuân Huấn" hay "Haruto" ra nhãn `1`. Nhưng làm sao bạn dám mang báo cáo này lên nộp cho sếp và bảo: *"Sếp cứ tin em, AI dự đoán chuẩn đấy!"*? Lỡ nó đoán bừa thì sao?

Trong AI, chúng ta không bao giờ mù quáng tin vào kết quả dự đoán nếu chưa **kiểm tra độ chính xác (Accuracy)** của nó.

Nguyên tắc vàng: **Không bao giờ mang đề thi (dữ liệu test) ra để dạy (train) AI.** Bạn phải dạy nó bằng sách giáo khoa (Train Data), rồi chấm điểm nó bằng một bài thi hoàn toàn độc lập (Test Data).

---

### 2. Thực hành: Chấm điểm AI với `accuracy_score`

Scikit-Learn cung cấp sẵn một "giám khảo" để tự động so sánh kết quả dự đoán của AI với đáp án thực tế.

```python
from sklearn.metrics import accuracy_score

# 1. Đáp án thực tế (Sự thật mà chúng ta đã biết)
# Ví dụ: Thực tế 3 khách hàng này có mua Premium hay không?
y_true = [1, 0, 1] 

# 2. Đáp án do AI dự đoán ra
y_pred = [1, 1, 1] # AI đoán sai người thứ 2

# 3. Gọi giám khảo ra chấm điểm
diem_so = accuracy_score(y_true, y_pred)

print(f"Độ chính xác của mô hình là: {diem_so * 100}%")
# Output: Độ chính xác của mô hình là: 66.66666666666666%

```

---

### 3. Thử thách thực chiến số 11: Tự làm "Giám khảo"

Quay trở lại với bảng dữ liệu 5 idol `df_customer` của bạn ở trên. Giả sử sau 1 tháng theo dõi, bạn có được **kết quả mua Premium thực tế** (Ground Truth) của 5 người này.

Sự thật là:

* Gia Bảo: **0** (Không mua)
* Huấn: **0** (Không mua - Mõm thôi)
* Haruto: **1** (Có mua)
* Khá Bảnh: **1** (Có mua)
* Thầy Ông Nội: **0** (Không mua)

Tức là danh sách đáp án chuẩn (y_true) sẽ là: `[0, 0, 1, 1, 0]`.
Trong khi đó, cột AI của bạn dự đoán (y_pred) đang là: `[0, 1, 1, 1, 1]`.

**Yêu cầu:** Bạn hãy viết tiếp một đoạn code nhỏ (dựa trên format ở bài trên):

1. Import `accuracy_score` từ `sklearn.metrics`.
2. Truyền 2 mảng đáp án thật (`y_true`) và mảng dự đoán (`y_pred`) vào để tính điểm.
3. In ra màn hình xem con AI "học non" của bạn đạt được độ chính xác bao nhiêu phần trăm nhé!