import numpy as np

# Có một danh sách Python thuần chứa độ sáng của 3 pixel ảnh
pixel_list = [120, 255, 80]
# Biến nó thành Mảng NumPy siêu tốc độ bằng hàm np.array()
pixel_array = np.array(pixel_list)
# Thử tăng độ sáng của TẤT CẢ các pixel lên gấp đôi
# Với Python thuần bạn phải dùng vòng lặp for. Với NumPy, bạn chỉ cần gõ:
new_pixels = pixel_array * 2
print(new_pixels)
