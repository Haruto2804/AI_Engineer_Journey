

### Thử thách: "Dữ liệu nhiễu" – Khi thực tế không như mơ

Trong thực tế, dữ liệu không bao giờ sạch sẽ và rõ ràng. Hãy thử tưởng tượng 3 nhân viên sau đây vừa mới gia nhập hệ thống của bạn:

* **Nhân viên A:** Lương cực cao (50 triệu), OT cực thấp (0h), nhưng vẫn **Nghỉ việc** (Nhãn 1) -> *Đây là "nhiễu" vì lương cao, nhàn hạ sao lại nghỉ?*
* **Nhân viên B:** Lương thấp (10 triệu), OT cực cao (30h), điểm hài lòng Sếp 9/10, nhưng vẫn **Ở lại** (Nhãn 0) -> *Đây cũng là "nhiễu" vì điều kiện tệ sao lại ở lại?*

Hãy thêm 3 người này vào dữ liệu cũ để xem con AI của bạn phản ứng ra sao.

```python
# Dữ liệu cũ + Dữ liệu nhiễu
X_nhan_su = [
    [15, 20, 4], [30, 5, 8], [12, 25, 3], [40, 0, 9],
    [10, 15, 5], [25, 10, 7], [14, 22, 2], [35, 2, 8],
    [18, 18, 5], [20, 8, 6], [11, 28, 4], [50, 0, 10],
    # 3 người nhiễu mới thêm vào:
    [50, 0, 5], [10, 30, 9], [45, 5, 2]
]
Y_nghi_viec = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] 

```

### Nhiệm vụ của bạn:

1. Chạy lại toàn bộ code với bộ dữ liệu mới này.
2. Kiểm tra lại `accuracy_score` và `feature_importances_`.
3. **Quan sát:** Độ chính xác có bị giảm xuống không? Bản báo cáo `feature_importances_` có bị thay đổi "đột ngột" so với trước không?

**Câu hỏi cốt lõi:** Sau khi thêm dữ liệu nhiễu, con AI của bạn còn giữ được độ chính xác 100% không? Và tại sao việc thêm chỉ 3 người "bất thường" lại có thể làm đảo lộn báo cáo của cả một tập đoàn?

Hãy chạy thử và cho tôi biết cảm nhận của bạn! Đây chính là lúc bạn hiểu vì sao các Kỹ sư AI cần phải có kỹ năng **Làm sạch dữ liệu (Data Cleaning)** trước khi đưa vào mô hình đấy.