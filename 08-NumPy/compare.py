# Để có cái nhìn tổng quan hơn về tốc độ của Python Thuần và Numpy thì
# ta sẽ có đoạn code so sánh thời sau đây
import time
import numpy as np

# Tạo 10 triệu phần tử cho cả 2 bên
size = 100000000
python_list = list(range(size))
numpy_array = np.arange(size)

# ----------------------------------------------------
# 1. ĐO TỐC ĐỘ PYTHON THUẦN (Dùng vòng lặp for)
start_time = time.time()

# Nhân đôi từng phần tử trong danh sách
python_result = [x * 2 for x in python_list]

end_time = time.time()
python_duration = end_time - start_time
print(f"Thời gian Python thuần chạy: {python_duration:.6f} giây")


# ----------------------------------------------------
# 2. ĐO TỐC ĐỘ NUMPY (Vector hóa - tính toán đồng thời)
start_time = time.time()

# Nhân đôi toàn bộ mảng NumPy trong 1 dòng
numpy_result = numpy_array * 2

end_time = time.time()
numpy_duration = end_time - start_time
print(f"Thời gian NumPy chạy:        {numpy_duration:.6f} giây")


# ----------------------------------------------------
# 3. KẾT LUẬN
tỷ_lệ = python_duration / numpy_duration
print(f"\n=> NumPy nhanh hơn Python thuần khoảng {tỷ_lệ:.1f} lần!")
