[Xem chi tiết bài học tại đây](https://developers.google.com/machine-learning/crash-course/categorical-data/one-hot-encoding)
---
[Xem thêm về Kĩ thuật Embedding ](https://youtu.be/jhvQNXYMdVI?si=gu1JNUDFcRmKMFYc)
# BÀI 27: CATEGORICAL DATA – VOCABULARY & ONE-HOT ENCODING

*(Dữ liệu phân loại: Từ vựng và Mã hóa One-hot)*

### 📌 Khái niệm cốt lõi (Core Concepts)

* **Dimension (Số chiều):** Trong Machine Learning, số chiều đồng nghĩa với số lượng phần tử nằm trong một vectơ đặc trưng (feature vector).
* **Categorical Feature (Đặc trưng phân loại):** Dữ liệu dạng chữ/danh mục (Ví dụ: Thứ trong tuần, màu sắc, quốc gia). Được chia làm 2 nhóm:
* *Low dimensional (Ít nhóm):* Số lượng danh mục nhỏ (Ví dụ: `season` có 4 nhóm: Xuân, Hạ, Thu, Đông).
* *High dimensional (Nhiều nhóm):* Số lượng danh mục cực lớn (Ví dụ: `words_in_english` có ~500,000 từ).



---

## I. Tại sao không thể nạp trực tiếp dữ liệu chữ (String)?

1. **Mô hình chỉ hiểu số:** Các mô hình Machine Learning thực chất là những phép toán số học nâng cao, chúng **chỉ có thể xử lý số thực (floating-point numbers)**.
2. **Lỗi gán nhãn sai lệch (Index Trap):** Nếu chỉ chuyển chữ thành số thứ tự tăng dần (Ví dụ: `Orange = 1`, `Blue = 2`, `Purple = 6`), mô hình sẽ hiểu nhầm rằng `Purple` có giá trị lớn gấp 6 lần `Orange`. Điều này hoàn toàn sai lệch vì đây là mối quan hệ phân loại, các danh mục có vai trò bình đẳng nhau.

---

## II. Quy trình 3 bước xử lý dữ liệu phân loại ít nhóm

```
[Dữ liệu chữ dạng thô] ──> [Bảng từ vựng / Index] ──> [Vectơ One-hot]

```

### Bước 1: Tạo bảng từ vựng (Vocabulary & Index)

Gom tất cả các danh mục độc nhất lại và đánh số thứ tự từ $0$ đến $N-1$ (với $N$ là tổng số danh mục).

> *Ví dụ:* `car_color` có 3 màu: Red (0), Orange (1), Blue (2).

### Bước 2: Mã hóa One-hot (One-hot Encoding)

Chuyển đổi số thứ tự ở Bước 1 thành một vectơ (mảng) gồm $N$ phần tử. Trong đó:

* Chỉ có **duy nhất một vị trí** có giá trị `1.0` (tại vị trí index của danh mục đó).
* Tất cả các vị trí còn lại đều là `0.0`.

**Bảng minh họa mã hóa One-hot:**

| Tính chất (Feature) | Red | Orange | Blue |
| --- | --- | --- | --- |
| **"Red"** | **1** | 0 | 0 |
| **"Orange"** | 0 | **1** | 0 |
| **"Blue"** | 0 | 0 | **1** |

> 💡 **Mở rộng:** Biến thể **Multi-hot encoding** cho phép nhiều hơn một vị trí có giá trị `1.0` (Ví dụ: Một chiếc xe có hai màu sơn song song).

### Bước 3: Tối ưu bộ nhớ với Sparse Representation (Biểu diễn thưa)

* **Vấn đề:** Vectơ One-hot chứa quá nhiều số `0`, gây lãng phí bộ nhớ khi dữ liệu lớn.
* **Giải pháp:** Thay vì lưu cả mảng `[0, 0, 1, 0, 0, 0, 0, 0]`, *Sparse Representation* chỉ lưu lại **vị trí (index) nơi số 1 xuất hiện** (ở đây là số `2`).
* **Lưu ý:** Dù lưu trữ ở dạng rút gọn để tiết kiệm bộ nhớ, nhưng khi đưa vào huấn luyện, mô hình vẫn phải tính toán dựa trên cấu trúc của vectơ One-hot gốc.

---

## III. Xử lý các trường hợp đặc biệt ngoài thực tế

### 1. Dữ liệu ngoại lai (Outliers trong Categorical Data)

* Khi xuất hiện các danh mục cực kỳ hiếm gặp (Ví dụ: Màu xe hiếm như `Mauve` hoặc `Avocado`), thay vì tạo riêng một cột cho chúng, hệ thống sẽ gom tất cả vào một thùng chứa chung gọi là **OOV (Out-of-Vocabulary)**. Mô hình sẽ chỉ học một trọng số duy nhất cho thùng chứa OOV này.

### 2. Khi dữ liệu có quá nhiều nhóm (High-dimensional)

* Nếu số lượng danh mục lên tới hàng chục ngàn hay hàng triệu (như Mã bưu chính, Họ tên...), việc dùng One-hot Encoding sẽ làm vectơ phình to khủng khiếp, gây chậm hệ thống.
* **Giải pháp thay thế:**
* **Embeddings (Nhúng dữ liệu):** Giúp giảm số chiều đáng kể, giúp mô hình huấn luyện nhanh hơn và giảm độ trễ (latency) khi dự đoán.
* **Hashing (Kỹ thuật băm):** Một cách tiếp cận ít phổ biến hơn để ép giảm số chiều dữ liệu.



---

## 📋 Câu hỏi trắc nghiệm ôn tập (Check your understanding)

**Câu hỏi:** *True or False: A machine learning model can train directly on raw string values, like "Red" and "Black", without converting these values to numerical vectors.*

* **Đáp án:** **False**
* **Giải thích:** Mô hình không thể học trực tiếp trên chuỗi chữ thô, bắt buộc phải qua các bước chuyển đổi thành vectơ số (numerical vectors) như quy trình One-hot Encoding ở trên.