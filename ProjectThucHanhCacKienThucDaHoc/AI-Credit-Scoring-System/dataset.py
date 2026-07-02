import os
import pandas as pd


# Định nghĩa hàm đọc dữ liệu
def load_credit_data():
    # Lấy đường dẫn tuyệt đối để tránh lỗi FileNotFoundError khi gọi từ file khác
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_csv = os.path.join(current_dir, "du_lieu_tin_dung_augmented.csv")

    # Đọc file CSV
    df = pd.read_csv(file_csv)

    # Trích xuất dữ liệu
    ten_cot_tinh_nang = ["Tuổi", "Thu nhập", "Điểm tín dụng", "Số lần nợ xấu"]
    X_ngan_hang = df[ten_cot_tinh_nang].values.tolist()
    Y_phe_duyet = df["Phe_duyet"].values.tolist()

    # Trả về dữ liệu sau khi trích xuất
    return X_ngan_hang, Y_phe_duyet


# Định nghĩa thêm biến tên cột nếu cần dùng bên ngoài
ten_cot_ngan_hang = ["Tuổi", "Thu nhập", "Điểm tín dụng", "Số lần nợ xấu"]

# --- KIỂM TRA NGAY TẠI FILE DATASET (CHỈ CHẠY KHI BẤM RUN FILE NÀY) ---
if __name__ == "__main__":
    X, Y = load_credit_data()
    print("✅ Kiểm tra hàm load_credit_data() chạy thử:")
    print("X_ngan_hang (2 dòng đầu):", X[:2])
    print("Y_phe_duyet (2 dòng đầu):", Y[:2])
