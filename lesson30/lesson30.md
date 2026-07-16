## BÀI 30: ĐẶC TRƯNG VÀ CHẤT LƯỢNG CỦA DỮ LIỆU

[Xem thêm tại đây](https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics)
## 📌 Các Điểm Cốt Lõi Bạn Cần Nhớ

### 1. Số lượng dữ liệu (Quantity)

* **Quy tắc ngón tay cái:** Số lượng ví dụ (examples) để huấn luyện nên lớn hơn số lượng tham số (trainable parameters) của mô hình từ **1 đến 2 bậc đại lượng** (gấp 10 - 100 lần trở lên).
* Dữ liệu lớn + ít đặc trưng (features) thường cho ra mô hình tốt hơn là dữ liệu ít mà lại quá nhiều đặc trưng phức tạp.

### 2. Chất lượng và Độ tin cậy (Quality & Reliability)

Một tập dữ liệu không đáng tin cậy thường do các nguyên nhân:

* **Omitted values:** Bị thiếu dữ liệu (ví dụ: người dùng quên nhập tuổi).
* **Duplicate examples:** Dữ liệu bị trùng (ví dụ: lỗi server upload log 2 lần).
* **Bad values/labels:** Giá trị lỗi (gõ thừa số, cảm biến hỏng) hoặc gán nhãn sai.

### 3. Xử lý dữ liệu bị thiếu (Incomplete Examples)

Tuyệt đối **không đưa dữ liệu thiếu vào huấn luyện**. Bạn có 2 cách xử lý:

* **Xóa (Delete):** Xóa luôn dòng dữ liệu bị thiếu đó (nếu bạn có dư thừa dữ liệu sạch khác).
* **Bù đắp dữ liệu (Imputation):** Tự điền vào chỗ trống bằng các suy luận logic, khoa học (ví dụ: lấy giá trị trung bình - mean, hoặc trung vị - median).

---

## 📝 Giải bài tập ở cuối trang (Exercise)

**Đề bài:** Dữ liệu được sắp xếp theo thời gian (Timestamp) và bị thiếu nhiệt độ lúc 11:00:

* 09:00 $\rightarrow$ 12°C
* 10:00 $\rightarrow$ 18°C
* **11:00 $\rightarrow$ missing (Đang thiếu)**
* 12:00 $\rightarrow$ 24°C
* 13:00 $\rightarrow$ 38°C

*Hỏi: Giá trị nào hợp lý nhất để điền vào chỗ trống? (23, 51, 31)*

**Đáp án đúng:** **23** (hoặc một số nằm trong khoảng từ 18 đến 24).

> **Giải thích:**
> Dữ liệu thời tiết thường thay đổi tuần tự và liên tục theo thời gian. Nhìn vào xu hướng, nhiệt độ tăng dần từ 12°C (9h) $\rightarrow$ 18°C (10h) $\rightarrow$ **?** $\rightarrow$ 24°C (12h). Do đó, giá trị hợp lý nhất phải nằm giữa 18 và 24.
> * **23** là lựa chọn logic nhất (nằm ngay sát 24 trước khi tăng mạnh lên 38 vào buổi trưa).
> * **51** và **31** quá cao so với tiến trình tăng nhiệt độ tại thời điểm đó.
> 
> 

---

> **Lưu ý quan trọng khi train model:** Sau khi bạn dùng mẹo sắp xếp theo thời gian để điền dữ liệu thiếu (Imputation) xong, bạn **bắt buộc phải xáo trộn ngẫu nhiên (randomize/shuffle)** lại tập dữ liệu trước khi bỏ vào huấn luyện để tránh mô hình bị thiên vị học theo thứ tự thời gian (trừ các bài toán chuyên biệt về chuỗi thời gian - Time Series).
