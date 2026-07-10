
Chúc mừng bạn đã "phá đảo" thuật toán Rừng Ngẫu Nhiên (Random Forest) ở Bài 14. Bạn đã biết gọi thư viện, biết bắt nó học và đưa ra dự đoán. Tuy nhiên, nếu chỉ dừng ở đó, bạn mới chỉ là người "biết lái xe" chứ chưa phải là "tay đua chuyên nghiệp".

Đó là lý do chúng ta bước sang **Bài 15**.

---

## Bài 15 - Part 1 - Nghệ thuật "Độ xe" AI (Hyperparameter Tuning)

### 1. Ý nghĩa: "Siêu tham số" là cái gì?

Hãy tưởng tượng bạn vừa mua một chiếc siêu xe Random Forest từ showroom về. Theo mặc định của nhà sản xuất (Scikit-Learn), xe của bạn được thiết lập sẵn với **100 cái cây** và **chiều cao cây không giới hạn**. Cứ cắm chìa khóa vào chạy (`model.fit()`) là xe tự đi rất mượt.

Nhưng nếu bạn mang chiếc xe này đi đua giải vô địch (giải quyết bài toán thực tế của công ty), thông số mặc định chắc chắn không thể giúp bạn đạt Top 1. Bạn cần một người thợ máy mở nắp capo lên, vặn lại tỷ lệ xăng gió, chỉnh lại phuộc nhún... để ép con xe đạt công suất tối đa.

Trong AI, những "núm vặn" cấu hình này được gọi là **Siêu tham số (Hyperparameters)**. Và hành động vặn đi vặn lại để tìm ra tổ hợp ngon nhất gọi là **Tuning (Tinh chỉnh)**.

### 2. Hai "núm vặn" quyền lực nhất của Rừng Ngẫu Nhiên

Để độ một con AI Random Forest, các Kỹ sư thường tập trung vặn 2 núm chính sau:

* **`n_estimators` (Số lượng cây):** Mặc định là 100. Bạn có thể vặn lên 200, 300 hoặc 500. Số cây càng nhiều, AI đoán càng ổn định, nhưng bù lại máy tính sẽ chạy chậm hơn.
* **`max_depth` (Chiều cao tối đa của cây):** Mặc định là tự do. Nếu để tự do, cây mọc chi chít rễ và rất dễ mắc bệnh **Học vẹt (Overfitting)**. Bạn phải lấy kéo "cắt tỉa" bằng cách ép nó chỉ được cao tối đa 3 tầng (`max_depth=3`) hoặc 5 tầng (`max_depth=5`) để nó học được quy luật tổng quát nhất.

### 3. Vấn đề của sự "Mò mẫm"

Nếu làm thủ công, bạn sẽ phải thử tổ hợp (100 cây, cao 3), chạy thử xem được mấy điểm. Xong lại sửa code thành (200 cây, cao 5), chạy thử xem điểm có tăng không. Nếu bạn có chục cái núm vặn, số lần thử có thể lên tới hàng ngàn lần. Bạn sẽ ngồi gõ code đến sáng mai!

Để giải quyết sự đau khổ này, Scikit-Learn đã chế tạo ra một "Con Robot" mang tên **GridSearchCV**. Nhiệm vụ của nó là tự động lấy AI của bạn, thử nghiệm hàng trăm tổ hợp núm vặn ngầm bên trong, và cuối cùng nhổ ra cho bạn cấu hình có điểm số cao nhất.

---

