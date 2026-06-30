import pandas as pd
import numpy as np  # Import numpy để tạo ra các giá trị NaN (rỗng)

data_rac = {
    "Khach_Hang": ["Gia Bảo", "Huấn", "Haruto", "Gia Bảo", "Thầy Ông Nội"],
    "Tuoi": [25, np.nan, 22, 25, 85],  # Huấn bị quên nhập tuổi (NaN)
    "Luong_Trieu": [15, 40, np.nan, 15, 5],  # Haruto bị quên nhập lương (NaN)
}
df = pd.DataFrame(data_rac)
print("--- DỮ LIỆU GỐC TRƯỚC KHI DỌN ---")
print(df)
# 1. Loại bỏ kẻ mạo danh: Dòng số 0 và dòng số 3 giống hệt nhau ("Gia Bảo"). Hãy tìm cách xóa các dòng bị trùng lặp (Duplicate) trong bảng df. (Gợi ý: Tìm hiểu hàm .drop_duplicates())
df.drop_duplicates(inplace=True)
print("-----1. Loại bỏ kẻ mạo danh-------")
print(df)
# 2. Xử lý hố đen dữ liệu (Missing Data): AI không biết tính toán với chữ NaN. Hãy tìm cách điền số 0 vào TẤT CẢ những chỗ nào đang bị NaN trong bảng. (Gợi ý: Tìm hiểu hàm .fillna(...))
print("-----1. Xử lý hố đen dữ liệu-------")
df.fillna(0, inplace=True)
print(df)
# 3. Trích xuất dữ liệu sạch: Sau khi dọn xong, hãy tạo một dòng code để chỉ in ra những khách hàng có Tuoi lớn hơn 0 (để loại bỏ những người vừa bị điền tuổi bằng 0 ở bước trên).
print("-----1. Xử lý hố đen dữ liệu-------")
# điều kiện tuổi > 0
df_clean = df[df["Tuoi"] > 0]
print(df_clean)
