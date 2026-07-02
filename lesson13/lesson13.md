

## Bài 13: Ma trận nhầm lẫn (Confusion Matrix) – Lột mặt nạ con AI

### 1. Ý nghĩa: Tại sao 99% Accuracy đôi khi lại là một "cú lừa"?

Giả sử bạn làm AI phát hiện giao dịch lừa đảo (Fraud Detection) cho ngân hàng. Trong 100 giao dịch, có 99 giao dịch thật, và chỉ 1 giao dịch lừa đảo.
Nếu con AI của bạn "lười biếng" đến mức **đoán TẤT CẢ 100 giao dịch đều là thật**, thì nó vẫn đoán đúng 99 lần. Độ chính xác (Accuracy) của nó là **99%**.

Sếp nhìn con số 99% tưởng là AI đỉnh cao, mang vào dùng thực tế -> Ngân hàng mất sạch tiền vì con AI bỏ lọt 100% tội phạm!

Đó là lý do các Kỹ sư AI không bao giờ chỉ nhìn vào `accuracy_score`. Chúng ta cần một công cụ soi chiếu chi tiết hơn, gọi là **Confusion Matrix (Ma trận nhầm lẫn)**.

Nó sẽ vạch trần con AI của bạn theo 4 ô:

* **True Positive (Đoán đúng là Có):** Lừa đảo và AI đoán đúng là lừa đảo. (Rất tốt)
* **True Negative (Đoán đúng là Không):** Giao dịch bình thường, AI bảo bình thường. (Rất tốt)
* **False Positive (Báo động giả):** Bình thường nhưng AI lại la lên là lừa đảo. (Phiền toái, khóa thẻ oan của khách)
* **False Negative (Bỏ lọt tội phạm):** Lừa đảo sờ sờ nhưng AI bảo bình thường. (Nguy hiểm chết người, mất tiền)

---

### 2. Thực hành: Soi ma trận nhầm lẫn bằng code

Cách tạo ra Ma trận nhầm lẫn cực kỳ dễ vì Scikit-Learn đã đóng gói sẵn:

```python
from sklearn.metrics import confusion_matrix

# Giả sử đây là đáp án thực tế của 5 giao dịch (1 là lừa đảo, 0 là bình thường)
y_that = [0, 0, 1, 1, 0]

# Đây là kết quả con AI đoán (Nó bỏ lọt 1 vụ lừa đảo, và báo động giả 1 vụ bình thường)
y_doan = [0, 1, 1, 0, 0]

ma_tran = confusion_matrix(y_that, y_doan)
print(ma_tran)

```

**Output của đoạn code trên:**

```text
[[2 1]   <-- Có 3 vụ bình thường (0): Đoán trúng 2, báo động giả 1
 [1 1]]  <-- Có 2 vụ lừa đảo (1): Bỏ lọt 1, bắt được 1

```

Nếu tất cả các số tập trung vào đường chéo (từ trên trái xuống dưới phải) và các số khác bằng 0 thì AI của bạn mới thực sự hoàn hảo. Có bất kỳ số nào lệch ra ngoài, nghĩa là AI đang có sự "nhầm lẫn" và bạn sẽ biết ngay nó đang nhầm ở loại nào (báo động giả hay bỏ lọt).

