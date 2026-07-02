Tinh thần dấn thân của bạn thực sự mang dáng dấp của một "chiến binh" công nghệ! Đã đến lúc rời khỏi thao trường và bước vào trận chiến thực sự.

Chào mừng bạn đến với **Dự án Tốt nghiệp: Hệ thống AI Phê duyệt Khoản vay Ngân hàng (Credit Scoring System)**.

Với tư cách là Giám đốc Dữ liệu, tôi sẽ cung cấp cho bạn Bộ dữ liệu, Bản thiết kế kiến trúc (Blueprint) và chiến lược làm Giao diện. Nhiệm vụ của bạn là ráp nối các dòng code để biến nó thành hiện thực.

---

### 1. Bộ dữ liệu (Dataset)

Dưới đây là lịch sử tín dụng của 20 khách hàng.
**4 Đặc trưng (Features):** `[Tuổi, Thu nhập hàng tháng (Triệu VNĐ), Điểm tín dụng (0-1000), Số lần từng nợ xấu]`
**Nhãn mục tiêu (Label):** `0` = Duyệt cho vay (Khách tốt), `1` = Từ chối (Nguy cơ bùng nợ)

*Bạn hãy copy khối dữ liệu này vào đầu file code của mình:*

```python
# --- DỮ LIỆU TÍN DỤNG NGÂN HÀNG ---
# [Tuổi, Thu nhập (Triệu), Điểm tín dụng, Số lần nợ xấu]
X_ngan_hang = [
    [25, 15, 600, 0], [45, 50, 800, 0], [30, 10, 450, 2], [50, 60, 850, 0],
    [22, 8, 300, 3],  [35, 25, 700, 0], [28, 20, 650, 1], [40, 40, 750, 0],
    [55, 12, 400, 2], [32, 30, 720, 0], [26, 12, 500, 1], [48, 45, 780, 0],
    [29, 18, 550, 2], [38, 35, 740, 0], [24, 9, 350, 2],  [52, 55, 820, 0],
    [31, 22, 680, 0], [42, 38, 760, 0], [27, 14, 480, 1], [36, 28, 710, 0]
]

# 0: Duyệt (Tốt), 1: Từ chối (Xấu)
Y_phe_duyet = [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]

ten_cot_ngan_hang = ["Tuổi", "Thu nhập", "Điểm tín dụng", "Số lần nợ xấu"]

```

---

### 2. Bản thiết kế 5 bước (Kiến trúc hệ thống)

Bạn hãy tự viết code theo đúng trình tự này (không được đốt cháy giai đoạn):

1. **Chuẩn bị Dữ liệu:** Dùng `train_test_split` chia dữ liệu ra với `test_size=0.3`, `random_state=42`.
2. **Tìm cấu hình vô địch (Tuning):** * Đừng dùng thuật toán mặc định. Hãy tạo `GridSearchCV` bọc ngoài `RandomForestClassifier`.
* Cho robot thử các núm vặn: `n_estimators: [10, 50, 100]`, `max_depth: [2, 3, None]`.
* Ép nó học trên tập Train.


3. **Đo lường & Giải trình (Explain):**
* Cho mô hình tốt nhất dự đoán trên tập Test. In ra `accuracy_score`.
* Dùng `feature_importances_` để in ra tỷ lệ % của 4 yếu tố. *Đánh giá xem điểm tín dụng hay số lần nợ xấu quan trọng hơn.*


4. **Đóng gói (Deploy):** * Dùng `joblib.dump` lưu con AI tốt nhất thành file `ai_bank_approval.pkl`.

---

### 3. Về phần Giao diện (Interface): Nên làm thế nào?

Vì bạn là một Kỹ sư AI đang xây dựng Portfolio, tôi khuyên bạn chia làm 2 giai đoạn làm giao diện:

#### Giai đoạn 1: Giao diện Console "Giả lập tương tác" (Làm ngay hôm nay)

Bạn không cần code giao diện đồ họa phức tạp vội. Hãy dùng hàm `input()` của Python để tạo ra một "Giao diện dòng lệnh" (CLI) giống như cách các hacker hay làm.
*Gợi ý code Giai đoạn 1 (viết ở cuối file):*

```python
# Mở file .pkl lên
# Dùng hàm input() để hỏi người dùng nhập từng thông số
print("--- HỆ THỐNG PHÊ DUYỆT TÍN DỤNG TỰ ĐỘNG ---")
tuoi = int(input("Nhập tuổi khách hàng: "))
thu_nhap = float(input("Nhập thu nhập (Triệu VNĐ): "))
diem_td = int(input("Nhập điểm tín dụng (0-1000): "))
no_xau = int(input("Nhập số lần nợ xấu: "))

# Đưa vào AI dự đoán và in kết quả IF/ELSE

```

#### Giai đoạn 2: Giao diện Web xịn xò với Streamlit (Mục tiêu tiếp theo)

Sau khi hoàn thành Giai đoạn 1 chạy mượt mà trên Terminal, công nghệ tiếp theo bạn **bắt buộc phải biết** là **Streamlit**.
Đây là "bảo bối" của dân AI. Bạn chỉ cần viết đúng 5 dòng code Python, nó sẽ tự động biến file `.pkl` của bạn thành một trang Web có nút bấm, có ô nhập liệu đẹp lung linh như một phần mềm thực sự mà không cần biết một chữ HTML/CSS nào!

---

**Nhiệm vụ của bạn bây giờ:** Hãy mở IDE lên, dựa vào dữ liệu và 4 bước yêu cầu ở trên, tự tay viết một kịch bản hoàn chỉnh (bao gồm cả phần giao diện Console bằng lệnh `input()`). Khi viết xong và chạy thành công, hãy gửi toàn bộ code lên đây để "Sếp" nghiệm thu nhé!