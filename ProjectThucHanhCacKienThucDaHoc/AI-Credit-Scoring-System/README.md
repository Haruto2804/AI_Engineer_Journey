
---

```markdown
# 🏦 Hệ Thống Phê Duyệt Tín Dụng Tự Động (Credit Scoring System)

Dự án này là một ứng dụng Web App hoàn chỉnh (MVP) hỗ trợ thẩm định và phê duyệt khoản vay ngân hàng tự động. Hệ thống kết hợp giữa mô hình học máy **Random Forest (Học có giám sát)** đã qua tối ưu và hệ thống **Luật loại trừ cứng (Knock-out Rules)** nhằm tối ưu hóa quy trình quản trị rủi ro tín dụng.

---

## 📁 Cấu Trúc Thư Mục Thực Tế

Cấu trúc thư mục hiện tại của dự án được tổ chức như sau:
```text
📂 AI-Credit-Scoring-System/
├── 📂 model/
│   └── 📄 credit_scoring_model.pkl          # Bộ não AI đã huấn luyện xong
├── 📄 train-model.py                         # Code huấn luyện và xuất file mô hình
├── 📄 dataset.py                             # Script quản lý/xử lý tập dữ liệu gốc
├── 📄 du_lieu_tin_dung_augmented.csv         # Tập dữ liệu tín dụng mở rộng
├── 📄 app_web.py                             # Giao diện Web ứng dụng (Streamlit)
└── 📄 README.md                              # Hướng dẫn này

```

> ⚠️ **Lưu ý kỹ thuật:** Trong file `app_web.py`, đường dẫn load mô hình bắt buộc phải trỏ chính xác vào thư mục con:
> `joblib.load('model/credit_scoring_model.pkl')`

---

## 🛠️ Hướng Dẫn Cài Đặt Môi Trường

Mở Terminal (hoặc Command Prompt / PowerShell) và chạy lệnh sau để cài đặt đầy đủ các thư viện cần thiết:

```bash
pip install scikit-learn joblib streamlit pandas

```

---

## 🚀 Hướng Dẫn Các Bước Khởi Chạy Ứng Dụng

### Bước 1: Di chuyển Terminal vào đúng thư mục dự án

Do thư mục dự án của bạn nằm trong thư mục con `AI-Credit-Scoring-System`, hãy dùng lệnh `cd` để di chuyển vào trước:

```bash
cd AI-Credit-Scoring-System

```

### Bước 2: Kích hoạt ứng dụng Web bằng Streamlit

Gõ chính xác dòng lệnh dưới đây vào Terminal và nhấn **Enter**:

```bash
streamlit run app_web.py

```

### Bước 3: Trải nghiệm trên trình duyệt

Hệ thống sẽ tự động kích hoạt một cổng Local Server và mở trình duyệt web tại địa chỉ:
👉 **`http://localhost:8501`**

*(Nếu trình duyệt không tự mở, hãy copy địa chỉ trên dán vào Google Chrome hoặc Edge).*

---

## 🕹️ Các Kịch Bản Kiểm Thử Cần Thử Nghiệm

Hệ thống đã được thiết kế một cơ chế lọc kép, bạn hãy thử nghiệm 3 nhóm khách hàng sau trên giao diện web để thấy rõ độ hiệu quả:

1. **Khách hàng VIP (Được duyệt ngay):** Kéo Tuổi = 35+, Thu nhập = 40tr+, Điểm tín dụng = 750+, Nợ xấu = 0.
* *Kết quả:* Hệ thống báo màu xanh **APPROVED** đi kèm hiệu ứng bóng bay!


2. **Khách hàng dính Tử Huyệt (Knock-out):** Chọn **Số lần từng có nợ xấu >= 1** (Ví dụ: 2 lần nợ xấu), giữ nguyên các thông số tốt khác.
* *Kết quả:* Hệ thống lập tức kích hoạt bộ lọc luật cứng, báo màu đỏ **REJECTED** ngay lập tức mà không cần chuyển cho AI xử lý sai.


3. **Khách hàng Mập mờ (AI phân tích hành vi):** Chọn Nợ xấu = 0, nhưng hạ thấp Thu nhập xuống tầm 10-12tr, Điểm tín dụng tầm 450-500.
* *Kết quả:* Hồ sơ vượt qua vòng gửi xe nhưng sẽ bị **AI tính toán và từ chối** do điểm uy tín quá thấp trong lịch sử.



