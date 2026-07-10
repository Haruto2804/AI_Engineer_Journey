
## BÀI 19: LOG LOSS 
#### [Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/logistic-regression/loss-regularization?hl=vi)
---
### PHẦN 1: Ý NGHĨA (Log Loss là gì? Tại sao cần nó?)

* **Ẩn dụ thực tế:** Hãy quay lại ví dụ bạn là Bác sĩ.
* Nếu bạn chẩn đoán: *"Tôi tin chắc **99%** anh này bị Sốt"*, và kết quả khám ra anh ta Sốt thật $\rightarrow$ Bạn chẩn đoán quá chuẩn, bạn chẳng bị phạt lỗi nào (Điểm phạt = 0).
* Nhưng nếu bạn mạnh miệng phán: *"Tôi tự tin **99.9%** anh này Sốt"*, nhưng hóa ra anh ta **KHỎE RE** $\rightarrow$ Bạn chẩn đoán sai một cách đầy tự tin và chủ quan! Sự "tự tin mù quáng" này trong ngành Y là cực kỳ nguy hiểm, bạn sẽ bị tước bằng (Điểm phạt cao chót vót).


* **Ứng dụng trong AI:** **Log Loss (hay Cross-Entropy Loss)** chính là "hệ thống điểm phạt" dành cho con AI. Nó không chỉ quan tâm AI đoán đúng hay sai (nhãn 0 hay 1), mà nó còn đo lường xem **AI có quá tự tin vào một quyết định sai lầm hay không**. Mục tiêu của AI Engineer là huấn luyện cho AI sao cho điểm Log Loss này càng gần 0 càng tốt.

---

### PHẦN 2: THỰC HÀNH (Code tính điểm phạt)

Chúng ta sẽ dùng thư viện `log_loss` của Sklearn để tính điểm phạt của mô hình. Bạn hãy xem (hoặc chạy thử) đoạn code cực ngắn này:

```python
from sklearn.metrics import log_loss

# Thực tế (Sự thật bệnh án): 1 là Sốt, 0 là Khỏe
y_thuc_te = [1, 0] 

# Tình huống 1: AI dự đoán rất sát sự thật (90% sốt, 10% sốt - tức là 90% khỏe)
AI_du_doan_tot = [0.90, 0.10] 
diem_phat_1 = log_loss(y_thuc_te, AI_du_doan_tot)
print(f"Điểm phạt khi AI đoán giỏi: {diem_phat_1:.4f}") 
# Kết quả ra rất thấp (khoảng 0.1)

# Tình huống 2: AI "tự tin mù quáng" (Bệnh nhân 1 đoán có 10% sốt, Bệnh nhân 2 đoán 99% sốt)
AI_du_doan_te = [0.10, 0.99]
diem_phat_2 = log_loss(y_thuc_te, AI_du_doan_te)
print(f"Điểm phạt khi AI tự tin mù quáng: {diem_phat_2:.4f}") 
# Kết quả phạt cực kỳ nặng (hơn 3.0, cao gấp mấy chục lần!)

```

---

### PHẦN 3: THỬ THÁCH NHỎ KIỂM TRA LOGIC

Bây giờ bạn đã biết AI sẽ dùng thuật toán Hồi quy Logistic để ép kết quả về 0-1, và dùng Log Loss để tự chấm điểm phạt cho mình trong quá trình học.

> **Câu hỏi:** Giả sử bạn đang huấn luyện một con AI lọc Email Spam. Bạn có 2 mô hình (Model A và Model B) cùng đoán đúng 90/100 email. Nhưng:
> * Model A có điểm Log Loss là `0.15`
> * Model B có điểm Log Loss là `0.80`
> 
> 
> Nếu chỉ được chọn 1 mang đi ứng dụng thực tế vào sản phẩm của công ty, **bạn sẽ chọn Model nào làm AI Engineer chính? Tại sao?**

Hãy suy luận và trả lời thử nhé, hoặc hỏi tôi nếu bạn thấy mông lung!

