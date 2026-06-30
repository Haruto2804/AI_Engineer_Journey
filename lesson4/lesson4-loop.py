# 3. Thử thách thực chiến số 4: Lọc dữ liệu ảnh "rác"
# Bạn đang chuẩn bị dữ liệu để huấn luyện một mô hình AI nhận diện xe cộ.
# Model yêu cầu ảnh đầu vào phải có dung lượng lớn hơn 5MB thì mới đủ sắc nét để học.
# Những ảnh nhỏ hơn sẽ bị coi là ảnh rác và bị loại bỏ.

# Bạn có một danh sách dung lượng của các bức ảnh (đơn vị MB) như sau:
# photo_sizes = [2, 8, 1.5, 12, 6, 4.5]

# Yêu cầu: Hãy viết một vòng lặp for kết hợp với điều kiện if để duyệt qua danh sách
# photo_sizes. Nếu ảnh nào >= 5, hãy in ra màn hình:
# "Ảnh hợp lệ, giữ lại để train AI!". Nếu ảnh nào nhỏ hơn 5,
# in ra: "Ảnh quá nhỏ, loại bỏ!".
photo_sizes = [2, 8, 1.5, 12, 6, 4.5]
for photo in photo_sizes:
    if photo >= 5:
        print(f"Ảnh có kích thước {photo} MB hợp lệ. Giữ lại để train AI!")
        continue
    print("Ảnh quá nhỏ, loại bỏ!")
